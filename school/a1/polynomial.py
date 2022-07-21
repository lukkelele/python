from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

K = [1, 3, 5, 7, 9, 11]
np.set_printoptions(threshold=sys.maxsize)

def y_func(x):
    """y = f(x) = 5 + 12x - x**2 + 0.025x**3 + normrnd(0.5)"""
    y = 5 + 12*x - (x**2) + 0.025*(x**3) + np.random.randint(0, 5)
    return y

def y_func_matrix(X):
    Y = np.zeros_like(X)
    Y = np.add(np.add(Y, 5), np.multiply(12, X))
    Y = np.add(Y, np.multiply(12, X))
    Y = np.subtract(Y, np.multiply(0.025, np.power(X, 3)))
    Y = np.add(Y, np.random.randint(0, 5))
    return Y


def plot(X, y, k, step_size=0.1):
    step_size = step_size
    x_min, x_max, y_min, y_max = np.min(X), np.max(X), np.min(y), np.max(y)
    x_range, y_range = x_max-x_min, y_max-y_min
    i = 0
    offset = 1
    while i < x_range:
        p = i + offset
        y_pred = ml.knn_regression(p, X, k)
        plt.scatter(p, y_pred, c='b', s=8)
        i += step_size


# Read data and shuffle it
data = ml.open_csv_file('./data/polynomial200.csv')
np.random.shuffle(data)
# Divide test set and train set
train_set, test_set = data[:100], data[100:]
X_train, Y_train, X_test, Y_test = train_set[:,0], train_set[:,1], test_set[:,0], test_set[:,1]
X_max = np.max(X_train)

# Plot the test and training set
fig = plt.figure(figsize=(14,12))

# Train plot
plt.subplot(2,2,1)
plt.xlabel('x'), plt.ylabel('y')
plt.scatter(X_train, Y_train, s=10, edgecolors='k')
# Test plot
plt.subplot(2,2,2)
plt.xlabel('x'), plt.ylabel('y')
plt.scatter(X_test, Y_test, s=10, edgecolors='k')

# Predicted regression values as well
plt.subplot(2,2,3)
plt.xlabel('x'), plt.ylabel('y'), plt.xlim([0, X_max])
plt.scatter(X_test, Y_test, s=10, edgecolors='k')
plot(train_set, Y_train, 3, step_size=0.8)



plt.show()



