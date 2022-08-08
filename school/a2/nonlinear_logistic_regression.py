from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

#np.set_printoptions(threshold=sys.maxsize)

"""
Quadratic model, polynomial degree 2
"""

# Read the already normalized data
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,[0, 1]], data[:,2]
X1, X2 = X[:, 0], X[:, 1]
# Plot the initial data
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,10))
ax1.scatter(X1[y==1], X2[y==1], c='g', cmap='flag', s=35, marker='v', edgecolors='k', label='correct')
ax1.scatter(X1[y==0], X2[y==0], c='r', cmap='flag', s=35, marker='x', label='wrong')
ax1.set_xlabel('X1'), ax1.set_ylabel('X2'), ax1.set_title(f"Initial data")
ax1.legend()

# Gradient descent to find beta of the quadratic model
iterations = 10000
learning_rate = 0.1
X_p4 = ml.polynomial(X1, X2, 4)
beta, betas = ml.log_gradient_descent(X_p4, y, N=iterations, a=learning_rate)

# Plot the cost function over iterations
costs = []
for i in range(len(betas)):
    cost = ml.log_calc_cost(X_p4, y, betas[i])
    costs.append(cost)
x_iter = np.arange(0, iterations, 1)
ax2.scatter(x_iter, costs, s=4, c='k')
ax2.set_xlabel('iterations'), ax2.set_ylabel('cost'), ax2.set_title(f'Cost function J(B)')





plt.show()
