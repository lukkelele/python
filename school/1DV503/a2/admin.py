import mysql.connector
import csv

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
        #database=""
        )

DB_name = "GUNNARSSON"      # last name

cursor = db.cursor()






def main_menu():
    print


def print_rows(csv_file):
    file = open(csv_file,'r')
    for row in file:
      print(row)
