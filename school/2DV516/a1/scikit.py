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

# y --> y value for corresponding x0, x1 value
# X --> 2-dimensional array of x0 and x1
def plot_data(x0, x1, y, n, k):
    plt.subplot(2, 2, n)
    plt.title(f"k == {k}")
    idx = 0
    X = np.array([x0, x1])
    for x0 in X[0]:
        y_val = y[idx]
        if y_val == 0:
            point_color = "r"
        else: point_color = "g"
        x1 = X[1][idx]
        plt.scatter(x0,x1, color=point_color, s=12, alpha=0.5)
        idx += 1

def determine_chip_status(chip, chip_sum, k):
    if chip_sum < k - math.floor(k/2):
        print(f"{chip} --> Fail")
        plt.scatter(chip[0], chip[1], color="r", s=60, edgecolors="k")
    else:
        print(f"{chip} --> OK!")
        plt.scatter(chip[0], chip[1], color="g", s=60, edgecolors="k")

def run_test(k, data, n):
    print(f"\n----------\n| k == {k} |\n----------\n")
    X = data[0]
    y = data[1]
    x0 = X[:, 0] # select the first column in X
    x1 = X[:, 1] # select the second column in X
    plot_data(x0, x1, y, n, k)
    n = KNeighborsClassifier(n_neighbors=k)
    n.fit(X, y)
    neighbors = n.kneighbors(test_chips)
    indexes = neighbors[1]
    chip_sum = []
    i = 0
    for idx in indexes:
        #print(f"idx: {idx}")
        y_sum = sum(y[idx])
        determine_chip_status(test_chips[i], y_sum, k)
        i += 1



def simulate(k):
    data = open_csv_file(path)
    f = plt.figure(figsize=(12, 9.4))
    plt.suptitle("Scikit on task 1")
    n = 1 # number of subplot
    for i in k: # iterate the list
        run_test(i, data, n)
        n += 1
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.show()

simulate(simulation_k)
