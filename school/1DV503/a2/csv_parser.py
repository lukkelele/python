import csv


def read_row(csv_file):
    reader = open(csv_file, 'r')
    for row in reader:
        print(row)


