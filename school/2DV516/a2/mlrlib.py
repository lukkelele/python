from matplotlib import pyplot as plt
import numpy as np



# two columns only
def normalize_matrix(X):
    x0_col, x1_col = X[:,0], X[:,1]
    x0_std, x1_std = np.std(x0_col), np.std(x1_col)
    x0_mean, x1_mean = np.mean(x0_col), np.mean(x1_col)
    x0_subt, x1_subt = np.subtract(x0_col, x0_mean), np.subtract(x1_col, x1_mean)
    x0_norm, x1_norm = np.divide(x0_subt, x0_std), np.divide(x1_subt, x1_std) 
    Xn = np.concatenate((x0_norm.reshape(len(x0_col), 1), x1_norm.reshape(len(x0_col), 1)), axis=1)
    return Xn

def normalize_column(X, col):
    x = X[:,col]
    x_std = np.std(x)
    x_mean = np.mean(x)
    x_subt = np.subtract(x, x_mean)
    x_norm = np.divide(x_subt, x_std)
    return x_norm

# Normalize a single value
def normalize_val(x, X):
    x_mean = np.mean(X)
    x_std = np.std(X)
    x_norm = (x-x_mean)/x_std
    return x_norm

def extend_matrix(X, n):
    return np.c_[np.ones((n, 1)), X]

# Extend a matrix in its first column
def normalize_extend(X):
    Xn = normalize_matrix(X)
    Xn_e = extend_matrix(Xn, len(Xn))
    return Xn_e

def calc_beta(Xe, y):
    B = np.linalg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(y)
    return B

def calc_j(Xe, y, beta):
    j = np.dot(Xe, beta) - y
    return j

def calc_cost(X, beta, y, n):
    j = np.dot(X, beta) - y
    J = (j.T.dot(j)) / n
    return J

def calc_height(beta, x0, x1):
    height = beta[0] + beta[1]*x0 + beta[2]*x1
    return height

def gradient_descent(Xe, y, b, N=10, a=0.001):
    n = len(Xe)     # column length 
    for i in range(N):
        grad = Xe.T.dot(y - Xe.dot(b)) / n
        b = b - a*grad
    return b

# Plot two subplots with different x values but same y values
def plot_subplot(x1, x2, y, i, c=['m', 'b']):
    j = 2
    I = int(f"{j}2{i}")
    plt.subplot(I)
    plt.scatter(x1, y, color=c[0], s=30, edgecolors='k', label='mom')
    I = int(f"{j}2{i+1}")
    plt.subplot(I)
    plt.scatter(x2, y, color=c[1], s=30, edgecolors='k', label='dad')
