import mysql.connector
import csv
import sql_statements as SQL
import ui


DB_name = "GUNNARSSON"

# Try to connect to a database that is named GUNNARSSON



def read_multivalued_attribute(path, table):
    with open(path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row_split = row['climate'].split(",")
            if len(row_split) > 1:          # if multivalued attribute
                for attribute in row_split:
                    s = f"INSERT INTO {table}"
                    print(s)





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


cursor = db.cursor()    # Create cursor object
attr = [["f_name", "varchar(20)"], ["l_name", "varchar(20)"]]
SQL.create_table("Migge-Mike Kingen", attr)

ui.main_menu()


# MULTIVALUED ATTRIBUTES INCLUDE:
# Planets.csv ==> climate, terrain
# Species.csv ==> skin_colors, hair_colors, eye_colors

# TABLES TO CREATE:
# Planet, Specie, Environment, Color


