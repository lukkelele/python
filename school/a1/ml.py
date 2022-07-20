from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np


def open_csv_file(path):
    """Open CSV file using pandas"""
    data = pd.read_csv(path).values  # pyright: ignore
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

def get_neighbors(p, k, X):
        """
        Get k closest neighbors for a passed point.
        Returns: 2D array with distance on index 0 and point on index 1
        """
        neighbors = []
        dist = np.zeros_like(X[:,[0,1]], dtype=object)
        idx = 0
        for point in X:
            distance = euclidean_distance(p, point)
            dist[idx][0] = distance
            dist[idx][1] = point
            idx+=1
        dist = dist[dist[:,0].argsort()]
        #print(f"Dist:\n{dist}")
        for i in range(k):
            neighbors.append(dist[i])  # Get the k closest points
        return np.array(neighbors)

def knn_clf(p, k, X):
    """
    Column 0 -> distances
    Column 1 -> points in array
    """
    neighbor_sum = 0
    p_neighbors = get_neighbors(p, k, X)[:,1]
    #print(f"\nNeighbors for {p}:\n{p_neighbors}\n")
    for neighbor in p_neighbors:
        neighbor_sum += neighbor[2]
    if neighbor_sum > floor(k/2):
        return 1
    else:
        return 0


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
    mean = subtract.mean()
    mse = np.mean(np.square(Y-Y_pred))
    return mse





