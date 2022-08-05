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
    """
    Get k closest neighbors to the point p in the dataset X
    """
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
    """
    Predict an y value for a point p with k neighbors in
    dataset X
    """
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
    """
    Normalize a column X with a standard deviation centered
    around 0
    """
    x_subt = np.subtract(X, np.mean(X))
    x_norm = np.divide(x_subt, np.std(X))
    return x_norm

# Normalize a single value
def normalize_val(X, i, val):
    """
    Normalize a single value in dataset X with corresponding
    values coming from the i'th column.
    """
    column = X[:,i]
    mean = np.mean(column) 
    std = np.std(column) 
    norm_val = (val-mean)/std
    return norm_val

# Extend matrix
def extend_matrix(X):
    """
    Extend the dataset X in the front with a single column containing ones
    """
    return np.c_[np.ones((len(X), 1)), X]

# Calculate beta
def calc_beta(Xe, y):
    """
    Returns the calculated beta from the normal equation for the 
    extended matrix Xe with the labeled data y
    """
    return np.linalg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(y)

# TODO: Consider removing
def calc_j(Xe, y, beta):
    """
    Calculate the 'j' of the cost function
    """
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


def polynomial(X, d):
    ones = np.ones((len(X),1))
    Xi = X
    for i in range(2, d+1):
        X = np.c_[X, Xi**i]
    X = np.c_[ones, X]
    return X

def sigmoid(X):
    """
    Returns the dataset X applied with the sigmoid function
    """
    return 1.0 / (1 + np.exp(-X))

def log_calc_cost(X, y, b):
    """
    Calculate the cost for the dataset X with y and beta 'b'
    """
    n = len(X)
    j = sigmoid(np.dot(X,b))
    J = -(y.T.dot(np.log(j)) + (1-y).T.dot(np.log(1-j))) / n
    return J

def log_gradient_descent(X, y, N=10, a=0.01, plot=False):
    """
    Logarithmic gradient descent
    """
    n = len(X)
    b = np.zeros((len(X[0]),))
    for i in range(N):
        s = sigmoid(np.dot(X, b)) - y
        grad = (a/n) * np.dot(X.T, s)
        b = b - grad 
        if plot:
            cost = log_calc_cost(X, y, b)
            plt.scatter(i, cost, s=3, color="k")
    return b

# TODO: CLEAN UP
def log_regression_predict(X):
    """
    y_hat = sigmoid(w.X + b)
    Predict y for X
    """
    predictions = sigmoid(X)
    return predictions

def plot_decision_boundary_logreg(X, b, y):
    """
    X: input data, extended matrix [ 1 , x1, x2 ]
    b: beta , gradients
    decision boundary --> y = mx + c
    c --> bias
    """
    x1 = [min(X[:,1]), max(X[:,1])]
    m, c = -b[1:], -b[0]
    x2 = m*x1 + c
    plt.plot(X[:,1][y==0], X[:,2][y==0], "r^") # points with y < 0.5
    plt.plot(X[:,1][y==1], X[:,2][y==1], "gs") # points with y > 0.5
    plt.xlim([-2.3, 2.3])
    plt.ylim([-2.3, 2.3])
    plt.plot(x1, x2, 'b')

