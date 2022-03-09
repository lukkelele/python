import mysql.connector
import lib
import csv

DEFAULT_DB_NAME = "lukas"

planet_csv_datatypes = [["p_name", "varchar(20)", "PRIMARY KEY"], ["rotation_period", "int"], 
                       ["orbital_period", "int"], ["diameter","bigint"], ["climate", "varchar(50)"],
                       ["gravity", "varchar(50)"],     # temporarily change decimal(2,2) to varchar
                       ["terrain", "varchar(50)"], ["surface_water", "int"], ["population", "bigint"]]
# TERRAIN AND GRAVITY --> varchar(50) to make sure space is available

specie_csv_datatypes = [["s_name", "varchar(20)", "PRIMARY KEY"], ["classification", "varchar(15)"],
                        ["designation", "varchar(14)"] ,["average_height", "int"], ["skin_color", "varchar(50)"],
                        ["hair_color", "varchar(50)"], ["eye_color", "varchar(50)"], ["average_lifespan", "int"],
                        ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]



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


def drop_columns(cursor, table, table_columns, ignored_columns):
    for column in table_columns:
        col = column[0]
        flag = False
        for ignored_col in ignored_columns:
            if col == ignored_col: # if current column is one to be ignored
                flag = True
        if flag == False:   # If the column name doesn't match any column to be ignored, drop it
            cursor.execute(f"ALTER TABLE {table} DROP COLUMN {col};")


def create_Environment(cursor):
    cursor.execute(f"CREATE TABLE Environment (p_name varchar(20), climate varchar(50));")
    cursor.execute("INSERT INTO Environment SELECT p_name, climate FROM csv_planets WHERE NOT climate=\"NULL\";")
    adjust_multivalued_entity("Environment", "climate", cursor)
    cursor.execute("ALTER TABLE Environment ADD PRIMARY KEY (p_name, climate);")

def create_Terrain(cursor):
    cursor.execute(f"CREATE TABLE Terrain     (p_name varchar(20), terrain varchar(50));")
    cursor.execute("INSERT INTO Terrain     SELECT p_name, terrain FROM csv_planets WHERE NOT terrain=\"NULL\";")
    adjust_multivalued_entity("Terrain",     "terrain", cursor)
    cursor.execute("ALTER TABLE Terrain     ADD PRIMARY KEY (p_name, terrain);")

def create_Hair_Color(cursor):
    cursor.execute(f"CREATE TABLE Hair_Color (s_name varchar(20), hair_color varchar(50));")
    cursor.execute("INSERT INTO Hair_Color SELECT s_name, hair_color FROM csv_species WHERE NOT hair_color=\"NULL\";")
    adjust_multivalued_entity("Hair_Color", "hair_color", cursor)
    cursor.execute("ALTER TABLE Hair_Color ADD PRIMARY KEY (s_name, hair_color);")

def create_Eye_Color(cursor):
    cursor.execute(f"CREATE TABLE Eye_Color  (s_name varchar(20), eye_color  varchar(50));")
    cursor.execute("INSERT INTO Eye_Color  SELECT s_name, eye_color  FROM csv_species WHERE NOT eye_color=\"NULL\";")
    adjust_multivalued_entity("Eye_Color",  "eye_color",  cursor)
    cursor.execute("ALTER TABLE Eye_Color  ADD PRIMARY KEY (s_name, eye_color );")

def create_Skin_Color(cursor):
    cursor.execute(f"CREATE TABLE Skin_Color (s_name varchar(20), skin_color varchar(50));")
    cursor.execute("INSERT INTO Skin_Color SELECT s_name, skin_color FROM csv_species WHERE NOT skin_color=\"NULL\";")
    adjust_multivalued_entity("Skin_Color", "skin_color", cursor)
    cursor.execute("ALTER TABLE Skin_Color ADD PRIMARY KEY (s_name, skin_color);")

def duplicate_entity(cursor, source, target):
    cursor.execute(f"CREATE TABLE {target} LIKE {source};")
    cursor.execute(f"INSERT INTO {target} SELECT * FROM {source};")

def reference_table(cursor, source, target, pk):
    cursor.execute(f"ALTER TABLE {source} ADD FOREIGN KEY ({pk}) REFERENCES {target} ON DELETE CASCADE;")

def create_Table(cursor, name, datatypes):
    cursor.execute(new_table(name, datatypes))

def drop_table(cursor, name):
    cursor.execute(f"DROP TABLE {name};")

def copy_table(source_table, target_table):
    query = f"INSERT INTO {target_table} SELECT * FROM {source_table};"
    return query


def duplicate_table(source_table, new_table):
    query = f"CREATE TABLE {new_table} LIKE {source_table};"
    return query

def create_new_database(cursor, db_name):
    print(f"Creating new database named {db_name}.")
    cursor.execute("CREATE DATABASE {};".format(db_name))
    cursor.execute("USE {}".format(db_name))                # Set new database as default
    print(f"New database named {db_name} has been created.\n{db_name} set to default schema.")

def new_table(table, attributes):
    len_attributes = len(attributes)
    query = f"CREATE TABLE {table} (\n"
    for attribute in attributes:
        name = attribute[0]
        attr_type = attribute[1]
        constraint = ""
        key_property = ""
        if len(attribute) > 2:
            constraint = attribute[2]
            if len(attribute) > 3:                  # if primary key notation as an example
                key_property = attribute[3]
        if attributes.index(attribute) == (len_attributes - 1):     # if last attribute, dont add a ','
            query += f"{name} {attr_type} {constraint} {key_property} \n);"
            break
        else:
            query += f"{name} {attr_type} {constraint} {key_property},\n"
    return query 


def add_FOREIGN_KEY(cursor, table, attr, target_table, target_key):
    query = f"""ALTER TABLE {table}
                ADD FOREIGN KEY {attr}_FK ({attr})
                REFERENCES {target_table}({target_key})
                    ON DELETE CASCADE;"""
    cursor.execute(query)


def insert_to_table(cursor, target, source, attributes):
    cursor.execute(f"INSERT INTO {target} SELECT {attributes} FROM {source};")


def display_avg_lifespan(cursor):
    cursor.execute(f"""SELECT S.classification, AVG(S.average_lifespan)
                       FROM Specie AS S
                       GROUP BY S.classification;""")
    for row in cursor:
        print(row)

def estimate_climate(cursor, specie):
    cursor.execute(f"""SELECT S.s_name, E.climate
                       FROM Environment AS E, Specie AS S
                       WHERE S.s_name=\"{specie}\" AND E.p_name=S.homeworld;""")
    for row in cursor:
        print(row)

def display_min_height(cursor, min_height):
    cursor.execute(f"SELECT s_name FROM Specie WHERE average_height > {min_height};")
    for row in cursor:
        print(row)

def search_detail(cursor, query):
    cursor.execute(query)
    for row in cursor:
        print(row)

def list_planets(cursor):
    cursor.execute("SELECT p_name FROM Planet;")
    for planet in cursor:
        print(planet)
