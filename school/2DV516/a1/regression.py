from matplotlib import pyplot as p
import numpy as np
import csv
import math


csv_path = "./A1_datasets/microchips.csv"


# Open a csv file and read the data in to the list 'values'
def open_csv_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            for row in r:
                # row[0] == x0_val  | row[1] == x1_val  | row[2] == y_val
            #    print(row)
                values.append([row[0], row[1], row[2]]) 
    except: print("An error has occured!")




