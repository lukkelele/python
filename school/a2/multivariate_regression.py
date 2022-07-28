from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

bench_results = np.array([2432, 1607, 1683, 8, 8, 256, 1])

# The 7th column is the response y
# Find f(X) = B0 + B1*X1 + ... + B6*X6

def plot_features(X, y):
    features = len(X[0])
    plt.suptitle('Features vs Y', fontsize=17)
    for i in range(features):
        plt.subplot(2,3,i+1)
        plt.xlim(-2, 2)
        plt.title(f'X{i}')
        plt.scatter(X[:,i], y, edgecolors='k')
    plt.show()

np.set_printoptions(threshold=sys.maxsize)
data = ml.open_csv_file("./data/GPUbenchmark.csv")
fig = plt.figure(figsize=(12,12))
X, Y = data[:,[0,1,2,3,4,5]], data[:,6]

# Normalize X
Xn = ml.normalize_matrix(X)

# Plot features
#plot_features(Xn, Y)

# Extend normalized Xn
Xn_e = ml.extend_matrix(Xn)

# Normalize testing benchmark
bench_results_n = []
for i in range(7):
    norm_val = ml.normalize_val(data, i, bench_results[i])
    bench_results_n.append(norm_val)
bench_results_n = np.array(bench_results_n)

# Calc beta
b = ml.calc_beta(Xn_e, Y)
pred_result = bench_results_n.dot(b)
print(f">> Predicted result value for {bench_results}:\n   {pred_result}")
# Calculate cost
cost = ml.calc_cost(Xn_e, b, Y)
print(f">> Cost for using b == {b}\n\n   {cost}")

# Gradient descent
a = 0.001
N = 1000000
gradients = ml.gradient_descent(Xn_e, Y, N, output=False)

# Calc cost using gradients
cost_gradients = ml.calc_cost(Xn_e, gradients, Y)
print(f">> Cost when using gradient descent: {cost_gradients}")
print(f">> Cost when using normal equ: {cost}")

# Predict benchmark result
pred_result_gradient_descent = bench_results_n.dot(gradients)
print(f">> Predicted result when using gradient descent:\n   {pred_result_gradient_descent}")





