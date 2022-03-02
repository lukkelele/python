import mysql.connector
import csv
import sql_statements as SQL
import ui


DB_name = "GUNNARSSON"


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


planet_datatypes = [["p_name", "varchar(20)"], ["rotation_period", "int"], ["orbital_period", "int"]
                   ,["diameter","long"], ["climate", "varchar(20)"], ["gravity", "decimal(2,2)"], 
                    ["terrain", "varchar(20)"], ["surface_water", "int"], ["population", "bigint"]]

planet_datatypes =  ["p_name varchar(20), rotation_period int, orbital_period int"+
                     "diameter long, climate varchar(20), gravity decimal(2,2)"+ 
                     "terrain varchar(20), surface_water int, population bigint"]


def user_input():
    menu_input = input("ENTER A NUMBER: ")
    while menu_input.isnumeric == False:
        menu_input = input("ONLY numbers are allowed!\nENTER A NUMBER: ") 
    return menu_input


def read_multivalued_attribute(path, table):
    with open(path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row_split = row['climate'].split(",")
            if len(row_split) > 1:          # if multivalued attribute
                for attribute in row_split:
                    s = f"INSERT INTO {table}"
                    print(s)


def check_data_exists(cursor, database):
    cursor.execute(SQL.get_tables(database))
    for table in cursor:
        query = SQL.check_data_exist(table)
        cursor.execute(query)
        if cursor == 0:
            return False
    return True             # If all tables have some data, set true


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
except:
    print(f"No database found going by name {DB_name}.\nConnecting without a specified database instead.")
    db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root"
            )
    flag = False


cursor = db.cursor()    # Create cursor object


if flag == False:
    print(f"Creating new database named {DB_name}.")
else:
    # DATABASE EXISTS, check if data exists in tables
    data_exist = check_data_exists(cursor, db)
    if data_exist:
        ui.main_menu()
        user = user_input()
        if user == 1:
            print("List all planets")
        elif user == 2:
            print("Search for planet details")
    





# Tests
attr = [["f_name", "varchar(20)"], ["l_name", "varchar(20)"]]
SQL.create_table("Migge-Mike Kingen", attr)


