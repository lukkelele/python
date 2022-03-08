import mysql.connector
import csv
import sql_statements as SQL
import ui
import lib


global db
DB_name = "lukas"
DEFAULT_DB_NAME = "lukas"


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
    cursor.execute(f"""INSERT INTO {target} SELECT {attributes} FROM {source};""")

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


# Take and sort multivalued attributes and insert them individually
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



def connect_db(user, passwd, addr, db_name):
    if db_name == "":
        db_name = DEFAULT_DB_NAME
    try: 
        db = mysql.connector.connect(
                host=addr,
                user=user,
                passwd=passwd,
                database=db_name
                )
    except:
        db = mysql.connector.connect(
                host=addr,
                user=user,
                passwd=passwd
                )
    return db


# Read CSV data and insert into a table
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
        db = connect_db("root", "root", "127.0.0.1", DB_name)
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
        #insert_to_table("Environment", csv_planets_table, "p_name, climate", cursor)
        #insert_to_table("Terrain",     csv_planets_table, "p_name, terrain", cursor)
        cursor.execute("INSERT INTO Environment SELECT p_name, climate FROM csv_planets WHERE NOT climate=\"NULL\";")
        cursor.execute("INSERT INTO Terrain     SELECT p_name, terrain FROM csv_planets WHERE NOT terrain=\"NULL\";")
        adjust_multivalued_entity("Environment", "climate", cursor)
        adjust_multivalued_entity("Terrain",     "terrain", cursor)
        cursor.execute("ALTER TABLE Environment ADD PRIMARY KEY (p_name, climate);")
        cursor.execute("ALTER TABLE Terrain     ADD PRIMARY KEY (p_name, terrain);")
        # Create the color entities
        cursor.execute(f"CREATE TABLE Hair_Color (s_name varchar(20), hair_color varchar(50));")
        cursor.execute(f"CREATE TABLE Eye_Color  (s_name varchar(20), eye_color  varchar(50));")
        cursor.execute(f"CREATE TABLE Skin_Color (s_name varchar(20), skin_color varchar(50));")
        # Move the data
        cursor.execute("INSERT INTO Hair_Color SELECT s_name, hair_color FROM csv_species WHERE NOT hair_color=\"NULL\";")
        cursor.execute("INSERT INTO Eye_Color  SELECT s_name, eye_color  FROM csv_species WHERE NOT eye_color=\"NULL\";")
        cursor.execute("INSERT INTO Skin_Color SELECT s_name, skin_color FROM csv_species WHERE NOT skin_color=\"NULL\";")

        adjust_multivalued_entity("Hair_Color", "hair_color", cursor)
        adjust_multivalued_entity("Eye_Color",  "eye_color",  cursor)
        adjust_multivalued_entity("Skin_Color", "skin_color", cursor)
        cursor.execute("ALTER TABLE Hair_Color ADD PRIMARY KEY (s_name, hair_color);")
        cursor.execute("ALTER TABLE Eye_Color  ADD PRIMARY KEY (s_name, eye_color );")
        cursor.execute("ALTER TABLE Skin_Color ADD PRIMARY KEY (s_name, skin_color);")
        # Create intended tables
        cursor.execute(SQL.duplicate_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.duplicate_table(csv_species_table, "Specie"))
        cursor.execute(SQL.copy_table(csv_planets_table, "Planet"))
        cursor.execute(SQL.copy_table(csv_species_table, "Specie"))
        drop_columns("Planet" , planet_csv_datatypes, lib.get_column_names("planet"), cursor)
        drop_columns("Specie" , specie_csv_datatypes, lib.get_column_names("specie"), cursor)
        
        print("Dropping excess tables..")
        cursor.execute(f"DROP TABLE {csv_planets_table};")
        cursor.execute(f"DROP TABLE {csv_species_table};")

        # Set references
        cursor.execute("ALTER TABLE Environment ADD FOREIGN KEY (p_name) REFERENCES Planet(p_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Terrain     ADD FOREIGN KEY (p_name) REFERENCES Planet(p_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Hair_Color ADD FOREIGN KEY haircolor (s_name)  REFERENCES Specie(s_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Eye_Color  ADD FOREIGN KEY eyecolor  (s_name)  REFERENCES Specie(s_name) ON DELETE CASCADE;")
        cursor.execute("ALTER TABLE Skin_Color ADD FOREIGN KEY skincolor (s_name)  REFERENCES Specie(s_name) ON DELETE CASCADE;")

        print("New database successfully created!")
        db.commit()
        cursor.close()
        db.close()
        return True
    except:
        print("\n| ERROR |\nA new database could not be created.")
#        cursor.execute("DROP SCHEMA {}".format(DB_name))  # Deletes schema so it hasn't to be deleted manually in MySQLWorkbench
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
            min_height = input("Enter a minimun height: ")
            cursor.execute(f"SELECT s_name FROM Specie WHERE average_height > {min_height};")
            for s in cursor:
                print(s)

        elif user == '4':
            searched_specie = input("Enter a specie: ")
            cursor.execute(f"SELECT S.s_name, E.climate FROM Environment AS E, Specie AS S WHERE S.s_name=\"{searched_specie}\" AND E.p_name=S.homeworld;")
            for result in cursor:
                print(result)

        elif user == '5':
            query = f"""SELECT S.classification, AVG(S.average_lifespan)
                        FROM Specie AS S
                        GROUP BY S.classification;
                     """
            cursor.execute(query)
            for k in cursor:
                print(k)
        ui.main_menu()
        user = input()
        
