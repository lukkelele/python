from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np


def open_csv_file(path, header=0):
    if header == -1: header=None
    """Open CSV file using pandas"""
    data = pd.read_csv(path, header=header).values  # pyright: ignore
    return data

def select_column(dataset, col):
    return dataset[:,[col]]

def meshgrid( X, y, offset=1, step_size=0.05):
    """
    Create a meshgrid with a minimum of min(X, y)-h and
    a maximum of max(X, y)+h and a step size of z.
    """
    x_min, x_max, y_min, y_max = X.min()-(offset/4), X.max()+(offset/4), y.min()-offset, y.max()+(offset/4)
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step_size),
                         np.arange(y_min, y_max, step_size))
    return xx, yy

def euclidean_distance(p1, p2):
    """
    Calculate the euclidean distance between two point p1 and p2.
    Returns the squared distance.
    """
    d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    return sqrt(d)

def get_neighbors(p, X, k):
        """
        Get k closest neighbors for a passed point.
        Returns: 2D array with distance on index 0 and point on index 1
        """
        neighbors = []
        dist = np.zeros((len(X), 2), dtype=object)
        idx = 0
        for point in X:
            distance = euclidean_distance(p, point)
            dist[idx][0] = distance
            dist[idx][1] = point
            idx+=1
        dist = dist[dist[:,0].argsort()]
        for i in range(k):
            neighbors.append(dist[i])  # Get the k closest points
        return np.array(neighbors)

def get_neighbors_x(p, X, k):
    neighbors = []
    dist = np.zeros((len(X), 2), dtype=object)
    idx = 0
    for point in X:
        distance = point[0] - p
        distance_squared = distance**2
        dist[idx][0] = distance_squared
        dist[idx][1] = point
        idx += 1
    dist = dist[dist[:,0].argsort()]
    for i in range(k):
        neighbors.append(dist[i])
    return np.array(neighbors)

def knn_regression(p, X, k):
    neighbors = get_neighbors_x(p, X, k)
    y_sum = 0
    for neighbor in neighbors:
        y_sum += neighbor[1][1]
    average = y_sum / k
    return average

def knn_clf(p, k, X):
    """
    Column 0 -> distances
    Column 1 -> points in array
    """
    neighbor_sum = 0
    p_neighbors = get_neighbors(p, X, k)[:,1]
    #print(f"\nNeighbors for {p}:\n{p_neighbors}\n")
    for neighbor in p_neighbors:
        neighbor_sum += neighbor[2]
    if neighbor_sum > floor(k/2):
        return 1
    else:
        return 0

def normalize_column(X):
    x = X
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
def calc_cost(X, beta, y):
    n = len(X[:,0])
    j = np.dot(X, beta) - y
    J = (j.T.dot(j)) / n
    return J

# Calculate MSE error
def calc_MSE(Y, Y_pred):
    """MSE = (1/n) * sum(y - y_pred)**2"""
    mse = round(((Y - Y_pred)**2).mean(), 2)
    return mse

# Normalize a matrix
def normalize_matrix(X):
    rows, cols = len(X[:,0]), len(X[0])
    Xn = np.zeros((rows, cols))
    for i in range(cols):
        Xn[:,i] = normalize_column(X[:,i])
    return Xn

# Gradient descent
def gradient_descent(X, y, N=10, a=0.001, plot=False, output=False):
    cols = np.size(X, 1)
    n = len(X)     # Total rows
    b = np.zeros((cols,))
    for i in range(N):
        gradients = X.T.dot(X.dot(b)-y) / n
        #grad = -(X.T.dot(y - X.dot(b)) / n)
        b = b - a*gradients
        if plot:
            cost = calc_cost(X, b, y)
            plt.scatter(i, cost, s=10)
        if output:
            print(f"---------\n>> i == {i}")
            idx = 0 
            for beta in b:
                print(f"> b{idx}: {beta}")
                idx += 1
    return b


def polynomial2(X, d, n):
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


def polynomial(X, d):
    ones = np.ones((len(X),1))
    Xi = X
    for i in range(2, d+1):
        X = np.c_[X, Xi**i]
    X = np.c_[ones, X]
    return X


