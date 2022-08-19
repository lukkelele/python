from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import mllib
import sys
import ml


path = './data/girls_height.csv'
data = ml.open_csv_file(path)

row_length = len(data[:,0][0].split())
X = np.zeros((len(data), row_length))
X0, X1, X2 = np.zeros((len(data), 1)), np.zeros((len(data), 1)), \
             np.zeros((len(data), 1))

# Fix the data format
i = 0 
for entry in data[:,0]:
    e = entry.split()
    X[i][0], X[i][1], X[i][2] = e[0], e[1], e[2]
    X0[i] = e[0]
    X1[i] = e[1]
    X2[i] = e[2]
    i += 1

plt.figure(figsize=(12,10))
# Extend matrix X1 and X2 by a single column of ones
X12 = np.c_[X1, X2]
Xe = ml.extend_matrix(X12)
Y = X[:,0]
# Calculate beta with extended parents matrix --> child height
beta = ml.calc_beta(Xe, X0)
parents = np.array([1, 65, 70])
print(f">> parents * beta == {parents.dot(beta)}")

# NORMALIZED
# Normalize the dataset
# Remove the first column and extend the last two with a single column of ones
# Calculate beta of the normalized X_e matrix with the Y as the girls height, not normalized
Xn = ml.normalize_matrix(X)
X12_n = np.c_[Xn[:,1], Xn[:,2]]
Yn = ml.normalize_column(Xn[:,0])
Xn_e = ml.extend_matrix(X12_n)
beta_normalized = ml.calc_beta(Xn_e, X[:,0])
mom_norm, dad_norm = ml.normalize_val(X, 1, 65), ml.normalize_val(X, 2, 70)
parents_n = np.array([1, mom_norm, dad_norm])
#print(f"Mom normalized -> {mom_norm}\nDad normalized -> {dad_norm}")

# COST FUNCTION
cost = ml.calc_cost(Xn_e, beta_normalized, Y)
print(f"cost ==> {cost}")
N = 10
a = 0.0001
grad_desc = ml.gradient_descent(Xe, Y, N, a)
print(parents.dot(grad_desc))
#plt.show()

