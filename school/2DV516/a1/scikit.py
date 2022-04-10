from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import numpy as np
import csv
import math





csv_path = "./A1_datasets/microchips.csv"

simulation_k = [1, 3, 5, 7]  # k's to be used when simulating

chip1 = [-0.3, 1]
chip2 = [-0.5, -0.1]
chip3 = [0.6, 0]
chips = []
test_chips = [chip1, chip2, chip3]
chips_result = []

# Open a csv file and read the data in to the list 'values'
def open_csv_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            y = []
            for row in r:
                # row[0] == x0_val  | row[1] == x1_val  | row[2] == y_val
            #    print(row)
                X.append([float(row[0]), float(row[1])])
                y.append(float(row[2]))
            return [np.array(X), np.array(y)]
    except: print("An error has occured!")

data = open_csv_file(csv_path)
X = data[0]
x0 = data[0][:, 0]
x1 = data[0][:, 1]
y = data[1]

n = KNeighborsClassifier(n_neighbors=3)
n.fit(X, y)
print(n)
