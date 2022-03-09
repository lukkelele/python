import mysql.connector
import csv
import sql_statements as SQL
import ui
import lib
import tools


global db
global db_flag

DB_name = "lukas"

csv_planets_file = lib.get_file("planets.csv", "linux")
csv_species_file = lib.get_file("species.csv", "linux")
# Schema
# =======================================
# Planet(attributes)    
# Specie(attributes)
# Environment(p_name PRIMARY KEY, climate)
# Terrain(p_name PRIMARY KEY, terrain)
# Hair_Color(s_name PRIMARY KEY, color)
# Skin_Color(s_name PRIMARY KEY, color)
# Eye_Color(s_name PRIMARY KEY, color)
# =======================================

# MULTIVALUED ATTRIBUTES INCLUDE:
# Planets.csv ==> climate, terrain
# Species.csv ==> skin_colors, hair_colors, eye_colors

# Fetch the attribute names and datatypes for the table creations
planet_csv_datatypes = lib.get_datatypes("planet_csv")
specie_csv_datatypes = lib.get_datatypes("specie_csv")
planet_datatypes = lib.get_datatypes("planet")
specie_datatypes = lib.get_datatypes("specie")
environment_datatypes = lib.get_datatypes("environment")
terrain_datatypes = lib.get_datatypes("terrain")
hair_color_datatypes = lib.get_datatypes("hair_color")
eye_color_datatypes = lib.get_datatypes("eye_color")
skin_color_datatypes = lib.get_datatypes("skin_color")



def connect_db(user, passwd, addr, db_name):
    try: 
        print(f"Connecting to {db_name} at {addr} as {user}.")
        db = mysql.connector.connect(
                host=addr,
                user=user,
                passwd=passwd,
                database=db_name
                )
        print(f"Connection successful.")
        db_flag = True
    except:
        print(f"Connection unsuccesful, provided database not available.")
        db = mysql.connector.connect(
                host=addr,
                user=user,
                passwd=passwd
                )
        db_flag = False
    return [db, db_flag]



def new_database():
    try:
        print(f"\nNo database found going by name {DB_name}.")
        print(f"New database being created...")
        db = connect_db("root", "root", "127.0.0.1", DB_name)[0]    # index 0 --> from connect_db
        cursor = db.cursor()
        tools.create_new_database(cursor, DB_name) 

        # Create temporary tables for parsing the CSV files
        csv_planets_table = "csv_planets"
        csv_species_table = "csv_species"
        tools.create_Table(cursor, csv_planets_table, planet_csv_datatypes)
        tools.create_Table(cursor, csv_species_table, specie_csv_datatypes)

        # Read the CSV files and move the corresponding data to the new tables
        print("Parsing files..")
        tools.parse_csv_file(cursor, csv_planets_file, csv_planets_table)  
        tools.parse_csv_file(cursor, csv_species_file, csv_species_table)
        
        print("Creating environment and terrain entities...")
        tools.create_Environment(cursor)
        tools.create_Terrain(cursor)
        # Create the color entities
        print("Creating color entities...")
        tools.create_Hair_Color(cursor)
        tools.create_Eye_Color(cursor)
        tools.create_Skin_Color(cursor)

        # Create intended tables
        tools.duplicate_entity(cursor, csv_planets_table, "Planet")
        tools.duplicate_entity(cursor, csv_species_table, "Specie")
        tools.drop_columns(cursor, "Planet", lib.get_column_names("csv_planet"), lib.get_column_names("planet")) 
        tools.drop_columns(cursor, "Specie", lib.get_column_names("csv_specie"), lib.get_column_names("specie")) 
        tools.drop_table(cursor, csv_planets_table)
        tools.drop_table(cursor, csv_species_table)

        # Set references
        print("Referencing entities..")
        tools.reference_table(cursor, "Environment", "Planet(p_name)", "p_name")
        tools.reference_table(cursor, "Terrain",     "Planet(p_name)", "p_name")
        tools.reference_table(cursor, "Hair_Color",  "Specie(s_name)", "s_name")
        tools.reference_table(cursor, "Eye_Color",   "Specie(s_name)", "s_name")
        tools.reference_table(cursor, "Skin_Color",  "Specie(s_name)", "s_name")

        db.commit()
        cursor.close()
        db.close()
        return True
    except:
        print("A new database could not be created.")
        cursor.execute("DROP SCHEMA {}".format(DB_name))  
        print("Schema dropped!\nShutting down..")
        return False

# ---------------------------------------------------------------------

# connect_db returns a list with the database object on index 0 
# and a boolean value on index 1. This boolean value sets the 
# db_flag. If no database is found, the flag is set to False and
# a new database is created.
db = connect_db("root", "root", "127.0.0.1", DB_name)
db_flag = db[1] # index 1 --> db_flag boolean value
db = db[0]      # index 0 --> set db to the newly created database object

if db_flag == False:
    # If connection failed from connect_db, create new database
    db_flag = new_database()

if db_flag == True:
    # If connection was successful, proceed to main menu
    cursor = db.cursor()
    cursor.execute(f"USE {DB_name};")
    ui.main_menu()
    user = input()

    while user != 'Q':
        # LIST ALL PLANETS
        if user == '1':
            tools.list_planets(cursor)

        # SEARCH FOR SPECIFIC DETAILS
        elif user == '2':
            print("Search for planet details")
            search = input("Search for:")
            detail = input("Detail: ")
            query = ui.search_details(search, detail)
            if query != "":     # if a match was found
                try:
                    tools.search_detail(cursor, query)
                except:
                    print("There was an error fetching details from your specific search.")

        elif user == '3':
            min_height = input("Enter a minimun height: ")
            if min_height.isalpha():
                print("A height can only contain numbers!")
            else:
                tools.display_min_height(cursor, min_height)

        elif user == '4':
            searched_specie = input("Enter a specie: ")
            tools.estimate_climate(cursor, searched_specie)

        elif user == '5':
            tools.display_avg_lifespan(cursor)

        ui.main_menu()
        user = input()
            
