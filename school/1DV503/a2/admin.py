from asyncio.windows_events import NULL
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from tkinter import E
import mysql.connector
import csv
import sql_statements as SQL
import ui
import lib

DB_name = "gunnarss2on"

#csv_planets_file = "C:/Users/lukkelele/Code/python/school/1DV503/a2/data/planets.csv"
#csv_planets_file = "C:\\Users\\lukkelele\\Code\\python\\school\\1DV503\\a2\\data\\planets.csv"
csv_planets_file = "data\planets.csv"
csv_species_file = "C:\\Users\\lukkelele\\Code\\python\\school\\1DV503\\a2\\data\\species.csv"

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


def get_tables(cursor):
    cursor.execute("SHOW TABLES;")
    for table in cursor:
        print(table)


def parse_csv_file(cursor, path, target_table):
    with open('data\planets.csv', 'r') as file:
        file_data = csv.reader(file)

       # print("file reader applied")
        header = next(file_data)       # the attributes or column names
        print(f"HEADER: {header}")
        query = f"INSERT INTO {target_table}({{0}}) VALUES ({{1}});"  
        org_query = query
        value_query = f"INSERT INTO {target_table} VALUES ({{0}});"      
        query = query.format(','.join(header), ','.join('?' * len(header)))

        values = []
        for row in file_data:
            for attribute in row:
                if not attribute.isnumeric():
                    if attribute == "NA":
                        attribute = 'null'
                    else:
                        attribute = f"'{attribute}'" 
                values.append(attribute)
            query = value_query.format(','.join(values))
            print(query)
            cursor.execute(query)
            print("query successfully executed")
            values.clear()
                



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

        #cursor.execute(SQL.create_table("Specie", specie_datatypes))    # Specie Entity
        #cursor.execute(SQL.create_table("Planet", planet_datatypes))
        cursor.execute(SQL.create_table("Environment", environment_datatypes))
        cursor.execute(SQL.create_table("Terrain", terrain_datatypes))
        cursor.execute(SQL.create_table("Hair_Color", hair_color_datatypes))
        cursor.execute(SQL.create_table("Eye_Color",  eye_color_datatypes))
        cursor.execute(SQL.create_table("Skin_Color", skin_color_datatypes))
        
        # Create temporary tables for parsing the CSV files
        csv_planets_table = "csv_planets"
        csv_species_table = "csv_species"
        cursor.execute(SQL.create_table(csv_planets_table, planet_csv_datatypes))
        cursor.execute(SQL.create_table(csv_species_table, specie_csv_datatypes))
        print("CSV tables created.\nTime to parse data...")
        parse_csv_file(cursor, "data\planets.csv", csv_planets_table)  # Read data into newly created tables
        print("CSV file data read and inserted csv_planets.")
        parse_csv_file(cursor, csv_species_file, csv_species_table)
        print("CSV file data read and inserted into CSV tables.")
        
        # skin_color, hair_color and eye_color columns shall be removed from csv_species
        # climate and terrain shall be removed from csv_planets
        cursor.execute(SQL.copy_column(csv_planets_table, "Terrain", "terrain", "p_name"))
        cursor.execute(SQL.copy_column(csv_planets_table, "Environment", "climate", "p_name"))

        cursor.execute(SQL.copy_column(csv_species_table, "Hair_Color", "hair_color", "s_name"))
        cursor.execute(SQL.copy_column(csv_species_table, "Eye_Color",  "eye_color",  "s_name"))
        cursor.execute(SQL.copy_column(csv_species_table, "Skin_Color", "skin_color", "s_name"))
        print("Columns copied temporary CSV tables to other tables")
        # Drop columns 
        cursor.execute(SQL.drop_column(csv_planets_table, "terrain"))
        cursor.execute(SQL.drop_column(csv_planets_table, "climate"))
        #
        cursor.execute(SQL.drop_column(csv_species_table, "hair_color"))
        cursor.execute(SQL.drop_column(csv_species_table, "eye_color "))
        cursor.execute(SQL.drop_column(csv_species_table, "skin_color"))
        print("Columns dropped from temporary CSV tables")
        # Create intended tables
        cursor.execute(SQL.duplicate_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.duplicate_table(csv_species_table, "Specie"))
        print("Planet and Specie tables created.")
        # Set references
        cursor.execute("ALTER TABLE Hair_Color ADD FOREIGN KEY haircolor (hair_color) REFERENCES Specie(s_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Eye_Color  ADD FOREIGN KEY eyecolor  (eye_color)  REFERENCES Specie(s_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Skin_Color ADD FOREIGN KEY skincolor (skin_color) REFERENCES Specie(s_name) ON DELETE CASCADE;")

        return True
    except:
        print("\nERROR |\nA new database could not be created.")
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
except:
    flag = new_database(flag)



if flag == False:
    print("error")

else:
    cursor = db.cursor()    # Create cursor object
    ui.main_menu()
    user = user_input()
    while user != 'Q':      # Loop until Q is entered 
        if user == 1:
            print("List all planets")
            list_planets(cursor) 

        elif user == 2:
            print("Search for planet details")
        
        elif user == 3:
            print("")
        
        elif user == 4:
            print("")
            
        elif user == 5:
            print("")

        ui.main_menu()
        user = user_input()
        

# SELECT S.s_name, C.hair_color
#FROM Specie AS S, Hair_Color AS C
#WHERE S.s_name = C.s_name;
