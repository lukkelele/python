from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

K = [1, 3, 5, 7, 9, 11]
lim_offset = 4
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


def regression(X, y, k, step_size=0.1):
    x_min, x_max = np.min(X[:,0]), np.max(X[:,0])
    step_size = step_size
    x_range = x_max + 1
    line = []
    p = x_min   # Starting value
    while p < x_range:
        y_pred = ml.knn_regression(p, X, k)
        #plt.plot(p, y_pred, c='b')
        line.append([p, y_pred])
        p += step_size
    line = np.array(line)
    return line
    
def regression2(X, k):
    line = []
    x_vals = X[X[:,0].argsort()][:,0]   # Sort ascending order by x
    for p in x_vals:    # Pass the sorted x array to get predicted y values
        y_pred = ml.knn_regression(p, X, k)
        line.append([p, y_pred])
    line = np.array(line)
    return line


# Read data and shuffle it
data = ml.open_csv_file('./data/polynomial200.csv')
np.random.shuffle(data)
# Divide test set and train set
train_set, test_set = data[:100], data[100:]
X_train, Y_train, X_test, Y_test = train_set[:,0], train_set[:,1], test_set[:,0], test_set[:,1]
x_max_train, x_min_train = np.max(X_train), np.min(X_train)
x_max_test, x_min_test = np.max(X_test), np.min(X_test)

# Plot the test and training set
fig = plt.figure(figsize=(14,12))

# Train plot
plt.subplot(2,2,1)
#train_plot_MSE = ml.calc_MSE()
plt.xlabel('x'), plt.ylabel('y'), plt.xlim([x_min_train-lim_offset, x_max_train+lim_offset])
plt.scatter(X_train, Y_train, s=15, edgecolors='k')

# Test plot
plt.subplot(2,2,2)
plt.xlabel('x'), plt.ylabel('y'), plt.xlim([x_min_test-lim_offset, x_max_test+lim_offset])
plt.scatter(X_test, Y_test, s=15, edgecolors='k')

# Predicted regression values as well
plt.subplot(2,2,3)
plt.xlabel('x'), plt.ylabel('y'), plt.xlim([x_min_test-lim_offset, x_max_test+lim_offset])
plt.scatter(X_test, Y_test, s=10, edgecolors='k')
r1 = regression2(train_set, 3)
plt.plot(r1[:,0], r1[:,1], c='r')


plt.show()

