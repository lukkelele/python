from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import numpy as np
import csv
import math


path = "./A1_datasets/microchips.csv"

simulation_k = [1, 3, 5, 7]  # k's to be used when simulating

chip1 = [-0.3, 1]
chip2 = [-0.5, -0.1]
chip3 = [0.6, 0]
test_chips = [chip1, chip2, chip3]

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
                X.append([row[0], row[1]])
                y.append(row[2])
            return [np.array(X, dtype=float), np.array(y, dtype=float)]
    except: print("An error has occured!")

def load_data(path):
    data = open_csv_file(path)
    x0 = data[0][:, 0]
    x1 = data[0][:, 1]
    y = data[1]
    test_x0 = np.arange(0, 118, 1)
    test_x1 = np.arange(0, 118, 1)
    test_set = np.matrix([test_x0, test_x1])
    test_set = np.reshape(test_set, (118,2))
    print(f"len_y: {len(y)}\nlen_x0: {len(x0)}\nlen_x1: {len(x1)}")
    return test_set

def plot_data(data):
    x0 = data[0][:, 0]
    x1 = data[0][:, 1]
    Y = data[1]
    X = np.array([x0, x1])
    print(f"len_X: {len(X)}")
    idx = 0
    for x0 in X[0]:
        y = Y[idx]
        if y == 0:
            point_color = "r"
        else: point_color = "g"
        x1 = X[1][idx]
        plt.scatter(x0,x1, color=point_color)
        idx += 1
    plt.show()

def run_test(k, data):
    print(f"------\n| k == {k} |\n-------")
    X = data[0]
    x0, x1 = X[:, [0, 1]]
    y = data[1]
    n = KNeighborsClassifier(n_neighbors=k)
    n.fit(X, y)
    close = n.kneighbors(test_set)
    plt.plot(x0,x1, color="r")

def simulate(k, data):
    for i in k: # iterate the list
        run_test(i, data)


test_data = open_csv_file(path)
plot_data(test_data)


