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

def output_result(chip, y_pred: int):
    str_len = 14    # To make output consistent for the different cases
    msg_success, msg_fail = 'OK!', 'Fail'
    if y_pred == 0:
        msg_result = msg_success 
    else:
        msg_result = msg_fail
    print(f">> Chip {chip}" + (str_len-len(str(chip)))*" " + "=> " + msg_result)


# Read data
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,[0,1]], data[:,2]
fig = plt.figure(figsize=(14,12))
plt.suptitle('Classification using KNN', fontsize=20)

# Create the classifiers for the different k's
clf1 = KNeighborsClassifier(n_neighbors=1)
clf2 = KNeighborsClassifier(n_neighbors=3)
clf3 = KNeighborsClassifier(n_neighbors=5)

# Train the classifiers
clf1.fit(X, y), 
clf2.fit(X, y)
clf3.fit(X, y)

# Predict the values
prediction_k1 = clf1.predict(X_test)
prediction_k2 = clf2.predict(X_test)
prediction_k3 = clf3.predict(X_test)
predictions = [prediction_k1, prediction_k2, prediction_k3]

print(f"prediction -> {predictions}")
print(f">> PREDICTED VALUES")
for x in X_test:
    idx = X_test.index(x)
    y_pred = predictions[idx][idx]
    output_result(x, y_pred)




