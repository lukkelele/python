from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import sys
import ml

K = [1, 3, 5]
chip_1 = [-0.3,    1]
chip_2 = [-0.5, -0.1]
chip_3 = [ 0.6,    0]
X_test = [chip_1, chip_2, chip_3]

# Read data
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,[0,1]], data[:,2]
fig = plt.figure(figsize=(14,12))
plt.suptitle('Classification using KNN', fontsize=20)

for k in K:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X, y)
    Y_pred = clf.predict(X_test)
    idx = 0
    for y in Y_pred:
        print(f"> Chip {idx+1} => {X_test[idx]}")
        idx+=1
    print("------------------")





