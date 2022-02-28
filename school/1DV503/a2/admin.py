import mysql.connector
import csv


DB_name = "GUNNARSSON"

# Try to connect to a database that is named GUNNARSSON

def print_line(n):
    c = 0
    while c < n:
        print("=", end="")
        c += 1


def main_menu():
    print("\n")
    print_line(19)
    print(" MAIN MENU ", end="")
    print_line(19)
    print("\n")
    print("(1) LIST ALL PLANETS\n(2) SEARCH FOR PLANET DETAILS\n(3)"+
            " SEARCH FOR SPECIES ABOVE A CERTAIN HEIGHT\n(4) GUESS THE DESIRED CLIMATE\n(5) SHOW AVERAGE LIFESPAN PER SPECIES CLASSIFICATION\n")
    print_line(50)


def print_rows(csv_file):
    file = open(csv_file,'r')
    for row in file:
      print(row)



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

main_menu()







