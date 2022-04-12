import numpy as np
import csv

def open_csv_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: # row[0] == x0_val  | row[1] == x1_val  | row[2] == y_val
                X.append([row[0], row[1]], row[2])
            return np.array(X, dtype=float)
    except: print("An error has occured!")
