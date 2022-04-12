import numpy as np
import csv

#path = "./data/girls_height.csv"

path = "./data/girls_height.csv"


def open_csv_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: 
                row = row[0].split('\t')
                #print(f"{row[0]}\n{row[1]}\n{row[2]}")
                X.append([row[0], row[1], row[2]])
            return np.array(X, dtype=float)
    except: print("An error has occured!")

data = open_csv_file(path)
print(data)
