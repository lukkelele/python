import csv
import mysql.connector


mysql.connector.connect(host='localhost',
                        database='database',
                        user='root',
                        password='your password')



def read_row(csv_file):
    reader = open(csv_file, 'r')
    for row in reader:
        print(row)


