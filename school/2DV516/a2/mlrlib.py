from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
import math

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

def extend_matrix(X):
    return np.c_[np.ones((len(X), 1)), X]

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
    rows = len(X)
    cols = np.size(X,1)
    Xn = normalize_matrix(X, rows, cols)
    Xe = extend_matrix(X)
    Xn_e = extend_matrix(Xn)
    return [Xn, Xe, Xn_e]

def log_gradient_descent(X, y, N=10, a=0.001, verbose=False, plot=False):
    n = X.shape[0]     # column length 
    cols = np.size(X, 1)
    b = np.zeros((cols,))
    for i in range(N):
        s = sigmoid(np.dot(X, b)) - y
        grad = (1/n) * np.dot(X.T, s)
        b = b - a*grad 
        cost = log_calc_cost(X,y,b)
        if verbose:
            print(f"COST: {cost}")
        if plot:
            plt.scatter(i, cost, s=3, color="k")
    return b

def log_compute_errors(X, y, b):
    z = np.dot(X, b)
    p = sigmoid(z)
    pp = np.round(p)
    errors = np.sum(y!=pp)
    return errors

def sigmoid(X):
    return 1 / (1 + np.exp(-X))

def log_calc_cost(X, y, b):
    n = len(X)
    j = sigmoid(np.dot(X,b))
    J = -(y.T.dot(np.log(j)) + (1-y).T.dot(np.log(1-j))) / n
    return J

def decision_boundary(X1, X2, d, beta):
    h = 0.005    # STEP SIZE
    offset = 0.1
    x_min, x_max = np.min(X1) - offset, np.max(X1) + offset
    y_min, y_max = np.min(X2) - offset, np.max(X2) + offset
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    x1, x2 = xx.ravel(), yy.ravel()
    XXe = map_features(x1,x2,d,ones=True)
    p = sigmoid(np.dot(XXe, beta)) # classify mesh
    classes = p>0.5
    clz_mesh = classes.reshape(xx.shape)
    cmap_bold = colors.ListedColormap(['#FF0000', '#00FF00', '#0000FF']) # mesh plot
    cmap_light = colors.ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF']) # mesh plot
    plt.pcolormesh(xx, yy, clz_mesh, cmap=cmap_light)
    plt.scatter(X1, X2, marker='.', cmap=cmap_bold)

def map_features(X1, X2, d, ones=True):
    if ones: 
        one = np.ones([len(X1), 1])
        Xe = np.c_[one, X1, X2]
    else:
        Xe = np.array([X1, X2])
    for i in range(2, d+1):
        for j in range(0, i+1):
            X_new = X1**(i-j)*X2**j
            X_new = X_new.reshape(-1,1)
            Xe = np.append(Xe, X_new, 1)
    return Xe 



