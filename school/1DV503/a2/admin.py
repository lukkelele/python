import mysql.connector
import csv
import sql_statements as SQL
import ui
import lib



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

# TABLES TO CREATE:
# Planet, Specie, Environment, Color

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


def user_input():
    menu_input = input("ENTER A NUMBER: ")
    while menu_input.isnumeric == False:
        menu_input = input("ONLY numbers are allowed!\nENTER A NUMBER: ") 
    return menu_input


def add_FOREIGN_KEY(cursor, table, attr, target_table, target_key):
    query = f"ALTER TABLE {table} ADD FOREIGN KEY {attr}_FK ({attr}) REFERENCES {target_table}({target_key}) ON DELETE CASCADE;"
    cursor.execute(query)
    print(f"New foreign key on table {table} added onto {attr}!")

def list_planets(cursor):
    cursor.execute(SQL.list_planets())
    for planet in cursor:
        print(planet)


def drop_columns(table, table_columns, ignored_columns, cursor):
    for column in table_columns:
        col = column[0]
        flag = False
        for ignored_col in ignored_columns:
            if col == ignored_col: # if current column is one to be ignored
                flag = True
        if flag == False:   # If the column name doesn't match any column to be ignored, drop it
            print("DROPPING "+col)
            cursor.execute(SQL.drop_column(table, col))
        


def get_tables(cursor):
    cursor.execute("SHOW TABLES;")
    for table in cursor:
        print(table)


def parse_csv_file(cursor, path, target_table):
    with open(path, 'r') as file:
        file_data = csv.reader(file)
        print("File opened at path --> "+path)
        header = next(file_data)       # the attributes or column names
        query = f"INSERT INTO {target_table}({{0}}) VALUES ({{1}});"  
        value_query = f"INSERT INTO {target_table} VALUES ({{0}});"      
        query = query.format(','.join(header), ','.join('?' * len(header)))

        values = []
        for row in file_data:
            if row[0] == "NA":  # IF PRIMARY KEY IS NULL, SKIP
                pass
            else:
                for attribute in row:
                    if not attribute.isnumeric():
                        if attribute == "NA" or attribute == "indefinite":
                            attribute = "null"
                        else:
                            attribute = f"\"{attribute}\"" 
                    values.append(attribute)
                query = value_query.format(','.join(values))
                print(query)
                cursor.execute(query)
                values.clear()
        print(f"Parsing from file {path} done.")
                



def new_database(flag):
    try:
        print(f"\nNo database found going by name {DB_name}.\nConnecting without a specified database instead.")
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root"
            )
        cursor = db.cursor()
        print(f"Creating new database named {DB_name}.")
        cursor.execute("CREATE DATABASE {};".format(DB_name))
        cursor.execute("USE {}".format(DB_name))                # Set new database as default
        
        # Create temporary tables for parsing the CSV files
        csv_planets_table = "csv_planets"
        csv_species_table = "csv_species"
        cursor.execute(SQL.create_table(csv_planets_table, planet_csv_datatypes))
        cursor.execute(SQL.create_table(csv_species_table, specie_csv_datatypes))
        parse_csv_file(cursor, csv_planets_file, csv_planets_table)  # Read data into newly created tables
        print("CSV file data read and inserted csv_planets.")
        parse_csv_file(cursor, csv_species_file, csv_species_table)
        print("CSV file data read and inserted into CSV tables.")
        
        # Create the environment and terraint entity
        cursor.execute(SQL.duplicate_table(csv_planets_table, "Terrain"))
        cursor.execute(SQL.copy_table(csv_planets_table, "Terrain"))
        cursor.execute(SQL.duplicate_table(csv_planets_table, "Environment"))
        cursor.execute(SQL.copy_table(csv_planets_table, "Environment"))
        drop_columns("Terrain", planet_csv_datatypes, ["p_name", "terrain"], cursor)
        drop_columns("Environment", planet_csv_datatypes, ["p_name", "climate"], cursor)
        
        # Create the color entities
        cursor.execute(SQL.duplicate_table(csv_species_table, "Hair_Color"))
        cursor.execute(SQL.copy_table(csv_species_table, "Hair_Color"))
        cursor.execute(SQL.duplicate_table(csv_species_table, "Eye_Color"))
        cursor.execute(SQL.copy_table(csv_species_table, "Eye_Color"))
        cursor.execute(SQL.duplicate_table(csv_species_table, "Skin_Color"))
        cursor.execute(SQL.copy_table(csv_species_table, "Skin_Color"))
        drop_columns("Hair_Color", specie_csv_datatypes, ["s_name", "hair_color"], cursor)
        drop_columns("Skin_Color", specie_csv_datatypes, ["s_name", "skin_color"], cursor)
        drop_columns("Eye_Color" , specie_csv_datatypes, ["s_name", "eye_color"], cursor)

        # Create intended tables
        cursor.execute(SQL.duplicate_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.duplicate_table(csv_species_table, "Specie"))
        cursor.execute(SQL.copy_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.copy_table(csv_species_table, "Specie"))
        planet_columns = ["p_name", "rotation_period", "orbital_period", "diameter", "gravity", "surface_water", "population"]
        specie_columns = ["s_name", "classification", "designation", "average_height", "average_lifespan", "language", "homeworld"]
        drop_columns("Planet" , planet_csv_datatypes, planet_columns, cursor)
        drop_columns("Specie" , specie_csv_datatypes, specie_columns, cursor)
        print("Planet and Specie tables created.")

        # Set references
        #cursor.execute("ALTER TABLE Hair_Color ADD FOREIGN KEY haircolor (hair_color) REFERENCES Specie(s_name) ON DELETE CASCADE;")
        #cursor.execute("ALTER TABLE Eye_Color  ADD FOREIGN KEY eyecolor  (eye_color)  REFERENCES Specie(s_name) ON DELETE CASCADE;")
        #cursor.execute("ALTER TABLE Skin_Color ADD FOREIGN KEY skincolor (skin_color) REFERENCES Specie(s_name) ON DELETE CASCADE;")

        print("New database successfully created!")
        return True
    except:
        print("\n| ERROR |\nA new database could not be created.")
        cursor.execute("DROP SCHEMA {}".format(DB_name))  # Deletes schema so it hasn't to be deleted manually in MySQLWorkbench
        print("Schema dropped!\nShutting down..")
        return False

# ---------------------------------------------------------------------

flag = False
try:
    db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database=DB_name
            )
    print("Database named "+DB_name)
    flag = True
except:
    flag = new_database(flag)



if flag == False:
    print("error")

else:
    # If database doesn't exist, one is created with the same property DB_name
    # This makes it possible to reconnect the cursor with the database selected
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root",
        database=DB_name
        )
    cursor = db.cursor()    # Create cursor object
    cursor.execute("USE {}".format(DB_name))              
    ui.main_menu()
    user = input()
    while user != 'Q':      # Loop until Q is entered 
        if user == '1':
            cursor.execute("SELECT p_name FROM Planet;")
            for planet in cursor:
                print(planet)

        elif user == '2':
            print("Search for planet details")
            search = input("Search for:     (Planet) (Specie)")
            detail = input("Detail: ")
            query = ui.search_details(search, detail)
            print(query)
            if query != "":     # if a match was found
                cursor.execute(query)
                for result in cursor:
                    print(result)
        elif user == '3':
            print("3")
            drop_columns("Hair_Color", specie_csv_datatypes, ["s_name", "hair_color"], cursor)
        
        elif user == '4':
            print("4")
            
        elif user == '5':
            new_database(flag)

        ui.main_menu()
        user = input()
        

# SELECT S.s_name, C.hair_color
#FROM Specie AS S, Hair_Color AS C
#WHERE S.s_name = C.s_name;
