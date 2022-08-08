from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)

"""
Quadratic model, polynomial degree 2
"""
print('Running...')

# Read the already normalized data
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,[0, 1]], data[:,2]
X1, X2 = X[:, 0], X[:, 1]

# Gradient descent to find beta of the quadratic model
iterations = 10000
learning_rate = 0.1
poly_degree = 2
X_p = ml.polynomial(X1, X2, poly_degree)
beta, betas = ml.log_gradient_descent(X_p, y, iterations=iterations, learning_rate=learning_rate)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,10))
fig.suptitle('Microship dataset')

# Training errors
errors = ml.log_estimate_errors(X_p, y, beta)

ax2.scatter(X1[y==1], X2[y==1], c='g', cmap='flag', s=35, marker='v', edgecolors='k', label='correct')
ax2.scatter(X1[y==0], X2[y==0], c='r', cmap='flag', s=35, marker='x', label='wrong')
ax2.set_xlabel('X1')
ax2.set_ylabel('X2')
ax2.set_title(f"Training errors: {errors} with an polynomial degree of {poly_degree}")
ml.plot_nonlinear_db(X1, X2, y, b=beta, d=poly_degree, ax=ax2, h=0.0032)
ax2.legend()

# Plot the cost function over iterations
costs = []
for i in range(len(betas)):
    cost = ml.log_calc_cost(X_p, y, betas[i])
    costs.append(cost)
x_iter = np.arange(0, iterations, 1)
ax1.scatter(x_iter, costs, s=4, c='k')
ax1.set_xlabel('iterations')
ax1.set_ylabel('cost')
#stabilized_cost = round((costs[len(costs)-1]), 6)
stabilized_cost = round((costs[-1:][0]), 6)
ax1.set_title(f'Cost function J(B)\na == {learning_rate}\nN == {iterations}\nStabilizes at a cost around {stabilized_cost}')

# Polynomial of degree 5
X_p5 = ml.polynomial(X1, X2, 5)
beta_p5, betas_p5 = ml.log_gradient_descent(X_p5, y, iterations=iterations, learning_rate=learning_rate)
errors_p5 = ml.log_estimate_errors(X_p5, y, beta_p5)
#print(f"Errors poly degree 5: {errors_p5}")

lr = np.arange(0.1, 1.0, 0.001)
degrees = 30
iters = 1000

opt_d, opt_lr, cost = ml.log_tune_polynomial_model(X1, X2, y, degree_range=degrees, iterations=iters, learning_rate_range=lr)

print(f" Optimal degree: {opt_d}\n Optimal learning rate: {opt_lr}\n Cost: {cost}")





#plt.show()
