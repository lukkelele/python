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
                X.append([row[0], row[1]])
                y.append(row[2])
            return [np.array(X, dtype=float), np.array(y, dtype=float)]
    except: print("An error has occured!")

data = open_csv_file(csv_path)
X = data[0]
x0 = data[0][:, 0]
x1 = data[0][:, 1]
y = data[1]
test_x0 = np.arange(0, 118, 1)
test_x1 = np.arange(0, 118, 1)
test_set = np.matrix([test_x0, test_x1])
test_set = np.reshape(test_set, (118,2))

print(f"len_y: {len(y)}\nlen_x0: {len(x0)}\nlen_x1: {len(x1)}\nlen_X: {len(X)}")

k = 3
i = 0
n = KNeighborsClassifier(n_neighbors=k)
n.fit(X, y)
print(f"test set: \n{test_set}")
close = n.kneighbors(test_set)
plt.plot(x0,x1, color="r")
while i < k:
    print(f"distances: {close[0][i]}\nindexes: {close[1][i]}")
    i += 1
plt.show()



