import mysql.connector
import csv
import sql_statements as SQL
import ui


DB_name = "gunnarss2on"

csv_planets = "./data/planets.csv"
csv_species = "./data/species.csv"

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

planet_csv_datatypes = [["p_name", "varchar(20)", "NOT NULL", "PRIMARY KEY"], ["rotation_period", "int"], 
                       ["orbital_period", "int"], ["diameter","long"], ["climate", "varchar(20)"],
                       ["gravity", "decimal(2,2)"],
                       ["terrain", "varchar(20)"], ["surface_water", "int"], ["population", "bigint"]]


specie_csv_datatypes = [["s_name", "varchar(15)", "NOT NULL", "PRIMARY KEY"], ["classification", "varchar(15)"],
                        ["designation", "varchar(14)"] ,["average_height", "int"], ["skin_colors", "varchar(14)"],
                        ["hair_colors", "varchar(12)"], ["eye_colors", "varchar(10)"], ["average_lifespan", "int"],
                        ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]


planet_datatypes = [["p_name", "varchar(20)", "NOT NULL", "PRIMARY KEY"], ["rotation_period", "int"], 
                    ["orbital_period", "int"], ["diameter","long"], ["gravity", "decimal(2,2)"],
                    ["surface_water", "int"], ["population", "bigint"]]

specie_datatypes = [["s_name", "varchar(15)", "NOT NULL", "PRIMARY KEY"], ["classification", "varchar(15)"],
                    ["designation", "varchar(14)"] ,["average_height", "int"], 
                    ["average_lifespan", "int"], ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]

environment_datatypes = [["p_name", "varchar(14)", "NOT NULL", "PRIMARY KEY"], ["terrain", "varchar(12)"]]
terrain_datatypes = [["p_name", "varchar(14)", "NOT NULL", "PRIMARY KEY"], ["terrain", "varchar(12)"]]      # FIX
hair_color_datatypes = [["s_name", "varchar(20)"], ["hair_color", "varchar(14)", "PRIMARY KEY"]]
eye_color_datatypes =  [["s_name", "varchar(20)"], ["eye_color",  "varchar(14)", "PRIMARY KEY"]]
skin_color_datatypes = [["s_name", "varchar(20)"], ["skin_color", "varchar(14)", "PRIMARY KEY"]]



def user_input():
    menu_input = input("ENTER A NUMBER: ")
    while menu_input.isnumeric == False:
        menu_input = input("ONLY numbers are allowed!\nENTER A NUMBER: ") 
    return menu_input


def parse_csv_file(cursor, path, target_table):
    with open (path, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        header = next(file_reader)       # the attributes or column names
        query = f"INSERT INTO {target_table}({{0}}) VALUES({{1}})"       # double curly braces because of string format
        query = query.format(','.join(header), ','.join('?' * len(header)))
        for row in file_reader:
            cursor.execute(query, row)
        cursor.commit()


def add_FOREIGN_KEY(cursor, table, attr, target_table, target_key):
    query = f"ALTER TABLE {table} ADD FOREIGN KEY {attr}_FK ({attr}) REFERENCES {target_table}({target_key}) ON DELETE CASCADE;"
    cursor.execute(query)
    print(f"New foreign key on table {table} added onto {attr}!")



def list_planets(cursor):
    query = f"""SELECT DISTINCT P.p_name
                FROM Planet AS P;"""    
    cursor.execute(query)



def read_multivalued_attribute(path, table, attr):
    with open(path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row_split = row[attr].split(",")
            if len(row_split) > 1:          # if multivalued attribute
                for attribute in row_split:
                    s = f"INSERT INTO {table}"
                    print(s)



def get_tables(cursor):
    cursor.execute("SHOW TABLES;")
    for table in cursor:
        print(table)


def new_database(flag):
    try:
        print(f"No database found going by name {DB_name}.\nConnecting without a specified database instead.")
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
        parse_csv_file(cursor, csv_planets, csv_planets_table)  # Read data into newly created tables
        parse_csv_file(cursor, csv_species, csv_species_table)
        # skin_color, hair_color and eye_color columns shall be removed from csv_species
        # climate and terrain shall be removed from csv_planets
        cursor.execute(SQL.copy_column(csv_planets_table, "Terrain", "terrain", "p_name"))
        cursor.execute(SQL.copy_column(csv_planets_table, "Environment", "climate", "p_name"))

        cursor.execute(SQL.copy_column(csv_species_table, "Hair_Color", "hair_color", "s_name"))
        cursor.execute(SQL.copy_column(csv_species_table, "Eye_Color",  "eye_color",  "s_name"))
        cursor.execute(SQL.copy_column(csv_species_table, "Skin_Color", "skin_color", "s_name"))
        # Drop columns 
        cursor.execute(SQL.drop_column(csv_planets_table, "terrain"))
        cursor.execute(SQL.drop_column(csv_planets_table, "climate"))
        #
        cursor.execute(SQL.drop_column(csv_species_table, "hair_color"))
        cursor.execute(SQL.drop_column(csv_species_table, "eye_color "))
        cursor.execute(SQL.drop_column(csv_species_table, "skin_color"))
        # Create intended tables
        cursor.execute(SQL.duplicate_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.duplicate_table(csv_species_table, "Specie"))
       
        # Set references
        cursor.execute("ALTER TABLE Hair_Color ADD FOREIGN KEY haircolor (hair_color) REFERENCES Specie(s_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Eye_Color  ADD FOREIGN KEY (p_name) REFERENCES Specie(p_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Skin_Color ADD FOREIGN KEY (p_name) REFERENCES Specie(p_name) ON DELETE CASCADE;")

        return True
    except:
        print("A new database could not be created.")
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


print("Creating cursor")
cursor = db.cursor()    # Create cursor object

if flag == False:
    print("error")

else:

    ui.main_menu()
    user = user_input()
    if user == 1:
        print("List all planets")
    
    elif user == 2:
        print("Search for planet details")
    
    elif user == 3:
        print("")
    
    elif user == 4:
        print("")
        
    elif user == 5:
        print("")
        

# SELECT S.s_name, C.hair_color
#FROM Specie AS S, Hair_Color AS C
#WHERE S.s_name = C.s_name;
