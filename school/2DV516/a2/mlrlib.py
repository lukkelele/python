from matplotlib import pyplot as plt
import numpy as np
import math

# two columns only
def normalize_2D_matrix(X):
    x0_col, x1_col = X[:,0], X[:,1]
    x0_std, x1_std = np.std(x0_col), np.std(x1_col)
    x0_mean, x1_mean = np.mean(x0_col), np.mean(x1_col)
    x0_subt, x1_subt = np.subtract(x0_col, x0_mean), np.subtract(x1_col, x1_mean)
    x0_norm, x1_norm = np.divide(x0_subt, x0_std), np.divide(x1_subt, x1_std) 
    Xn = np.concatenate((x0_norm.reshape(len(x0_col), 1), x1_norm.reshape(len(x0_col), 1)), axis=1)
    return Xn

def normalize_matrix(X):
    rows, cols = np.size(X,0), np.size(X,1)
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

def extend_matrix(X):
    n = np.size(X,0)
    return np.c_[np.ones((n, 1)), X]

# Extend a matrix in its first column
def normalize_extend(X):
    Xn = normalize_matrix(X)
    Xn_e = extend_matrix(Xn)
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

def gradient_descent(Xe, y, N=10, a=0.001):
    cols = np.size(Xe, 1)
    n = len(Xe)     # column length 
    b = np.zeros((cols,))
    for i in range(N):
        grad = -(Xe.T.dot(y - Xe.dot(b)) / n)
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

def plot_features(X, y, r, row, col):
    if r == 1:
        current_column = X
        x_min, x_max = np.min(current_column) - 1, np.max(current_column) + 1
        plt.subplot(1,1,1)
        plt.xlim(x_min, x_max)
        plt.xlabel(f"x_1")
        plt.ylabel("y")
        plt.scatter(current_column, y, s=10, color="b")
    else: 
        for i in range(r):
            current_column = X[:,i]
            x_min, x_max = np.min(current_column) - 1, np.max(current_column) + 1
            plt.subplot(row, col, i+1)
            plt.xlim(x_min, x_max)
            plt.xlabel(f"x_{i}")
            plt.ylabel("y")
            plt.scatter(current_column, y, s=10, color="b")

def polynomial(X, d, n):
    if d == 1:
        X = np.c_[np.ones((n,1)),X]
    elif d == 2:
        X = np.c_[np.ones((n,1)),X,X**2]
    elif d == 3:
        X = np.c_[np.ones((n,1)),X,X**2,X**3]
    elif d == 4:
        X = np.c_[np.ones((n,1)),X,X**2,X**3,X**4]
    else: return 0  # if error
    return X

def create_extended_matrixes(X):
    cols = len(X)
    rows = X.shape[1]
    Xn = normalize_matrix(X)
    Xe = extend_matrix(X)
    Xn_e = extend_matrix(Xn)
    return [Xn, Xe, Xn_e]

def log_gradient_descent(X, y, N=10, a=0.001):
    cols = np.size(X, 1)
    b = np.zeros((cols,))
    n = X.shape[0]     # column length 
    for i in range(N):
        s = sigmoid(X.dot(b)) - y
        print(f"s: {s}\ns.reshape(-1,1):\n{s.reshape(-1,1)}")
        grad = (-1/n) * X.T.dot(s)
        b = b - a*grad 
    return b

def predict_score(a):
    X = np.array(a)
    Xn = normalize_matrix(X)

def log_compute_errors(X, y, b):
    z = np.dot(X, b)#.reshape(-1,1)
    p = sigmoid(z)
    pp = np.round(p)
    #yy = y.reshape(-1,1)
    print(pp)
    print("---")
    print(y)

def sigmoid2(X):
    z = -X
    g = 1 + np.e**z
    s = np.divide(1, g)
    return s

def sigmoid(X):
    return 1 / (1 + np.exp(-X))

def log_calc_cost(X, y, b):
    n = len(X)
    j = sigmoid(np.dot(X,b))
    J = -(y.T.dot(np.log(j)) + (1-y).T.dot(np.log(1-j))) / n
    return J

# X is the test dataset
def log_predict(X, x0, x1):
    X = np.array([x0, x1])
    Xn = normalize_matrix(X)
    Xn_e = extend_matrix(Xn)
    
