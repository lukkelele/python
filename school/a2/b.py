from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import mllib
import sys
import ml


path = './data/admission.csv'
data = ml.open_csv_file(path, header=-1)  # -1 to include row 0 in csv file
X, y = data[:,[0,1]], data[:,2]
plt.figure(figsize=(12,12))


# Normalize the features 
Xn = ml.normalize_matrix(X)
Xn0, Xn1 = Xn[:,0], Xn[:,1]

# Plot the normalized data
plt.subplot(111, facecolor='lightgray')
plt.scatter(Xn0, Xn1, c=y, cmap='gray', edgecolors='k')

# Apply the sigmoid function
mat2x2 = np.array([[0, 1], [2, 3]])
print(mat2x2.shape)
sigmoid_mat2x2 = ml.sigmoid(mat2x2)
print(sigmoid_mat2x2)

# Extend X
Xn_e = ml.extend_matrix(Xn)

# Test the cost function
b = [0, 0, 0]
cost = ml.log_calc_cost(Xn_e, y, b)
print(f">> Cost: {round(cost, 5)}")

# Test logarithmic gradient descent
a = 0.5
B = ml.log_gradient_descent(Xn_e, y, N=1, a=a)
B = np.round(B, 3)
print(f">> Beta after one iteration using logarithmic gradient descent: {B}")
print(f"   New cost: {round(ml.log_calc_cost(Xn_e, y, B), 4)}")

# Increase iterations to find a stabilized beta
N = 10000
B = ml.log_gradient_descent(Xn_e, y, N=100, a=a)
#B = np.round(B, 3)
print(f">> Beta after N={N} iterations using logarithmic gradient descent: {B}")
print(f"   New cost: {round(ml.log_calc_cost(Xn_e, y, B), 4)}")

#plt.show()


