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
    #print(f"New foreign key on table {table} added onto {attr}!")


def insert_to_table(target, source, attributes, cursor):
    print("entered insert")
    cursor.execute(f"""INSERT INTO {target} SELECT {attributes} FROM {source};""")
    print("exit insert")

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
            cursor.execute(SQL.drop_column(table, col))



def adjust_multivalued_entity(table, column, cursor):
        rows = []
        cursor.execute(f"SELECT * FROM {table};")
        for col in cursor:
            rows.append(col)
        for attribute in rows:
            key = str(attribute[0])
            attr = str(attribute[1])
            if len(attr.split(',')) > 1:
                # If attribute is a multivalued one
                for a in attr.split(","):
                    a = a.replace(" ", "")  # remove spaces
                    #print(f"INSERT INTO {table} values('{key}','{a}');")
                    cursor.execute(f"INSERT INTO {table} VALUES(\"{key}\",\"{a}\");")
                    cursor.execute(f"DELETE FROM {table} WHERE {column}=\"{attr}\";")


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
                cursor.execute(query)
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
        
        # Create temporary tables for parsing the CSV files
        csv_planets_table = "csv_planets"
        csv_species_table = "csv_species"
        cursor.execute(SQL.create_table(csv_planets_table, planet_csv_datatypes))
        cursor.execute(SQL.create_table(csv_species_table, specie_csv_datatypes))
        parse_csv_file(cursor, csv_planets_file, csv_planets_table)  # Read data into newly created tables
        parse_csv_file(cursor, csv_species_file, csv_species_table)
        print("CSV file data read and inserted into CSV tables.")
        
        cursor.execute(f"CREATE TABLE Environment (p_name varchar(20), climate varchar(50));")
        cursor.execute(f"CREATE TABLE Terrain     (p_name varchar(20), terrain varchar(50));")
        # Move the data
        insert_to_table("Environment", csv_planets_table, "p_name, climate", cursor)
        insert_to_table("Terrain",     csv_planets_table, "p_name, terrain", cursor)
        adjust_multivalued_entity("Environment", "climate", cursor)
        adjust_multivalued_entity("Terrain",     "terrain", cursor)
        # Create the color entities
        cursor.execute(f"CREATE TABLE Hair_Color (s_name varchar(15), hair_color varchar(50));")
        cursor.execute(f"CREATE TABLE Eye_Color  (s_name varchar(15), eye_color  varchar(50));")
        cursor.execute(f"CREATE TABLE Skin_Color (s_name varchar(15), skin_color varchar(50));")
        # Move the data
        insert_to_table("Hair_Color", csv_species_table, "s_name, hair_color", cursor)  
        insert_to_table("Eye_Color",  csv_species_table, "s_name, eye_color" , cursor)  
        insert_to_table("Skin_Color", csv_species_table, "s_name, skin_color", cursor)  
        adjust_multivalued_entity("Hair_Color", "hair_color", cursor)
        adjust_multivalued_entity("Eye_Color",  "eye_color",  cursor)
        adjust_multivalued_entity("Skin_Color", "skin_color", cursor)

        # Create intended tables
        cursor.execute(SQL.duplicate_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.duplicate_table(csv_species_table, "Specie"))
        cursor.execute(SQL.copy_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.copy_table(csv_species_table, "Specie"))
        planet_columns = ["p_name", "rotation_period", "orbital_period", "diameter", "gravity", "surface_water", "population"]
        specie_columns = ["s_name", "classification", "designation", "average_height", "average_lifespan", "language", "homeworld"]
        drop_columns("Planet" , planet_csv_datatypes, planet_columns, cursor)
        drop_columns("Specie" , specie_csv_datatypes, specie_columns, cursor)
        
        print("Dropping excess tables..")
        #cursor.execute(f"DROP TABLE {csv_planets_table};")
        #cursor.execute(f"DROP TABLE {csv_species_table};")

        # Set references
        #cursor.execute("ALTER TABLE Hair_Color ADD FOREIGN KEY haircolor (hair_color) REFERENCES Specie(s_name) ON DELETE CASCADE;")
        #cursor.execute("ALTER TABLE Eye_Color  ADD FOREIGN KEY eyecolor  (eye_color)  REFERENCES Specie(s_name) ON DELETE CASCADE;")
        #cursor.execute("ALTER TABLE Skin_Color ADD FOREIGN KEY skincolor (skin_color) REFERENCES Specie(s_name) ON DELETE CASCADE;")

        print("New database successfully created!")
        db.commit()
        cursor.close()
        db.close()
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
            cursor.execute("SELECT * FROM Hair_Color;")
            for l in cursor:
                print(l)
            
        elif user == '5':
            new_database(flag)

        ui.main_menu()
        user = input()
        

# SELECT S.s_name, C.hair_color
#FROM Specie AS S, Hair_Color AS C
#WHERE S.s_name = C.s_name;
