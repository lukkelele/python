import mysql.connector
import csv

DEFAULT_DB_NAME = "lukas"


def drop_columns(table, table_columns, ignored_columns, cursor):
    for column in table_columns:
        col = column[0]
        flag = False
        for ignored_col in ignored_columns:
            if col == ignored_col: # if current column is one to be ignored
                flag = True
        if flag == False:   # If the column name doesn't match any column to be ignored, drop it
            cursor.execute(f"ALTER TABLE {table} DROP COLUMN {col};")


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
                
