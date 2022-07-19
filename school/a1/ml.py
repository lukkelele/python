from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np

def normalize_matrix(X, rows, cols):
    Xn = np.zeros((rows, cols))
    for i in range(cols):
        Xn[:,i] = normalize_column(X, i)
    return Xn

def normalize_column(X, col):
    x = X[:,col]
    x_std = np.std(x)
    x_mean = np.mean(x)
    x_subt = np.subtract(x, x_mean)
    x_norm = np.divide(x_subt, x_std)
    return x_norm

# Normalize a single value
def normalize_val(X, col, val):
    column = X[:,col]
    mean = np.mean(column) 
    std = np.std(column) 
    norm_val = (val-mean)/std
    return norm_val

# Extend matrix
def extend_matrix(X):
    return np.c_[np.ones((len(X), 1)), X]

# Calculate beta
def calc_beta(Xe, y):
    B = np.linalg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(y)
    return B

# Calculate part of cost function
def calc_j(Xe, y, beta):
    j = np.dot(Xe, beta) - y
    return j

# Calculate cost
def calc_cost(X, beta, y, n):
    j = np.dot(X, beta) - y
    J = (j.T.dot(j)) / n
    return J

# Calculate MSE error
def calc_MSE(Y, Y_pred):
    """MSE = (1/n) * sum(y - y_pred)**2"""
    subtract = np.subtract(Y, Y_pred)
    print(f"Sum of subtract: {np.sum(subtract)}")
    mean = subtract.mean()
    print(f"Mean: {mean}")
    mse = np.mean(np.square(Y-Y_pred))
    return mse


