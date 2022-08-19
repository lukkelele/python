from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import mllib
import sys
import ml


def normalize_features(X):
    Xn = ml.normalize_matrix(X)
    Xn0, Xn1 = Xn[:,0], Xn[:,1]
    return Xn, Xn0, Xn1

def plot_normalized_data(X0, X1):
    plt.subplot(111, facecolor='lightgray')
    plt.scatter(X0, X1, c=y, cmap='gray', edgecolors='k')

def apply_sigmoid_func(arr):
    sig_arr = ml.sigmoid(arr)
    print(f">> Sigmoid")


path = './data/admission.csv'
data = ml.open_csv_file(path, header=-1)  # -1 to include row 0 in csv file
X, y = data[:,[0,1]], data[:,2]
plt.figure(figsize=(12,12))


# Normalize the features 
Xn, Xn0, Xn1 = normalize_features(X)

# Plot the normalized data
#plot_normalized_data(Xn0, Xn1)

# Apply the sigmoid function
mat2x2 = np.array([[0, 1], [2, 3]])
print(mat2x2.shape)
sigmoid_mat2x2 = ml.sigmoid(mat2x2)
print(sigmoid_mat2x2)

# Extend X
Xn_e = ml.extend_matrix(Xn)
X_e = ml.extend_matrix(X)

# Test the cost function
b = [0, 0, 0]
cost = ml.log_calc_cost(Xn_e, y, b)
print(f">> Cost: {round(cost, 5)}")

# Test logarithmic gradient descent
a = 0.5
#B = np.round(B, 3)
#print(f">> Beta after one iteration using logarithmic gradient descent: {B}")
#print(f"   New cost: {round(ml.log_calc_cost(Xn_e, y, B), 4)}")

# Increase iterations to find a stabilized beta
N = 1000
B = ml.log_gradient_descent(Xn_e, y, iterations=N, learning_rate=a)[0]
cost = ml.log_calc_cost(Xn_e, y, B)
#plt.xlim(2, N)
print(f">> COST --> {cost}")
print(f">> Beta after N={N} iterations using logarithmic gradient descent: {B}")
print(f"   New cost: {round(ml.log_calc_cost(Xn_e, y, B), 4)}")

B = ml.log_gradient_descent(Xn_e, y, iterations=N, learning_rate=a)[0] # Index 0 for last beta, [1] --> all betas
plt.subplot(211)
# Plot the linear decision boundary
ml.plot_linear_db(Xn_e, y, B)

test_score = np.array([45, 85])
nx1 = ml.normalize_val(X, 0, 45)
nx2 = ml.normalize_val(X, 1, 85)
print(test_score)
test_n = np.array([[nx1, nx2],
                   [1.02,  -.94]])
test_ne = ml.extend_matrix(test_n)
#print(test_n)
#test_ne = np.c_[1, test_n[0], test_n[1]]
#print(test_ne)
prob = ml.sigmoid(np.dot(test_ne, B))
print(f"Adm. prob for scores {test_score[0]}, {test_score[1]} is {prob[0]}")
#print(f"\nNormalized 45, 85 --> {nx1} , {nx2}\n")
plt.scatter(nx1, nx2, s=50, edgecolors='k', color='y')
print('\n-------------------\n')

plt.subplot(212)
d = 2
X_2 = ml.polynomial(Xn0, Xn1, d)
b = ml.log_gradient_descent(X_2, y, iterations=N, learning_rate=a)[0]
ml.plot_nonlinear_db(Xn0, Xn1, y, b, d)

err = ml.log_estimate_errors(Xn_e, y, B)
print(f">> Training errors: {err}")

#plt.show()
