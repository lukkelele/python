import mysql.connector
import csv
import sql_statements as SQL
import ui


DB_name = "gunnarss2on"


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


planet_datatypes = [["p_name", "varchar(20)", "NOT NULL", "PRIMARY KEY"], ["rotation_period", "int"], 
                    ["orbital_period", "int"], ["diameter","long"], ["climate", "varchar(20)"],
                    ["gravity", "decimal(2,2)"], 
                    ["terrain", "varchar(20)"], ["surface_water", "int"], ["population", "bigint"]]

specie_datatypes = [["s_name", "varchar(15)", "NOT NULL", "PRIMARY KEY"], ["classification", "varchar(15)"],
                    ["designation", "varchar(14)"] ,["average_height", "int"], 
                    ["average_lifespan", "int"], ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]

environment_datatypes = [["p_name", "varchar(14)", "NOT NULL", "PRIMARY KEY"], ["terrain", "varchar(12)"]]

terrain_datatypes = [["p_name", "varchar(14)", "NOT NULL", "PRIMARY KEY"], ["terrain", "varchar(12)"]]      # FIX

hair_color_datatypes = [["s_name", "varchar(20)"], ["hair_color", "varchar(14)", "PRIMARY KEY hair_color_PK (hair_color)"]]
eye_color_datatypes =  [["s_name", "varchar(20)"], ["eye_color",  "varchar(14)", "PRIMARY KEY eye_color_PK  (eye_color)" ]]
skin_color_datatypes = [["s_name", "varchar(20)"], ["skin_color", "varchar(14)", "PRIMARY KEY skin_color_PK (hair_color)"]]


def user_input():
    menu_input = input("ENTER A NUMBER: ")
    while menu_input.isnumeric == False:
        menu_input = input("ONLY numbers are allowed!\nENTER A NUMBER: ") 
    return menu_input


def parse_csv_file(path, cursor):
    with open (path, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        header = next(file_reader)       # the attributes or column names
        query = "INSERT INTO Planet({0}) VALUES ({1})"
        query = query.format(','.join(header), ','.join('?' * len(header)))
        for row in file_reader:
            cursor.execute(query, row)
        cursor.commit()



def add_FOREIGN_KEY(cursor, table, attr):
    query = f"ALTER TABLE {table} ADD FOREIGN KEY {attr}_FK ({attr});"
    cursor.execute(query)
    print(f"New foreign key on table {table} added onto {attr}!")


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


def new_database():
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
    # Create all tables
    cursor.execute(SQL.create_table("Specie", specie_datatypes))    # Specie Entity
    cursor.execute(SQL.create_table("Planet", planet_datatypes))
    cursor.execute(SQL.create_table("Environment", environment_datatypes))
    cursor.execute(SQL.create_table("Hair_Color", environment_datatypes))
    cursor.execute(SQL.create_table("Eye_Color",  eye_color_datatypes))
    cursor.execute(SQL.create_table("Skin_Color", skin_color_datatypes))
    
    cursor.execute("ALTER TABLE Hair_Color ADD FOREIGN KEY (p_name) REFERENCES Specie(p_name) ON DELETE CASCADE;")
    cursor.execute("ALTER TABLE Eye_Color  ADD FOREIGN KEY (p_name) REFERENCES Specie(p_name) ON DELETE CASCADE;")
    cursor.execute("ALTER TABLE Skin_Color ADD FOREIGN KEY (p_name) REFERENCES Specie(p_name) ON DELETE CASCADE;")
    
    print("Getting tables")
    get_tables(cursor)



# Try to connect
# If database not found, create one
# Parse the CSV files and add to the tables accordingly

flag = True
try:
    db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database=DB_name
            )
    print("Database named "+DB_name)
except:
    print(f"No database found going by name {DB_name}.\nConnecting without a specified database instead.")
    db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root"
            )
    flag = False


print("Creating cursor")
cursor = db.cursor()    # Create cursor object

if flag == False:
    # LOTS OF TESTING
    print(f"Creating new database named {DB_name}.")
    cursor.execute("CREATE DATABASE {};".format(DB_name))
    cursor.execute("USE {}".format(DB_name))
    # Create all tables
    
    cursor.execute("""CREATE TABLE Specie (
	s_name varchar(20) PRIMARY KEY,
    classification varchar(18),
	designation    varchar(18),
    average_height   int,
    average_lifespan int,
    s_language     varchar(18),
    homeworld      varchar(18)
    );""")

    cursor.execute(SQL.create_table("Planet", planet_datatypes))
    cursor.execute(SQL.create_table("Specie", specie_datatypes))
    cursor.execute(SQL.create_table("Environment", environment_datatypes))
    cursor.execute("ALTER TABLE Environment ADD FOREIGN KEY (p_name) REFERENCES Planet(p_name);")
    print("Getting tables")
    get_tables(cursor)
    print("Parsing CSV file")
    #parse_csv_file("./data/planets.csv", cursor)


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
        
