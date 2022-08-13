from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import warnings
import time

warnings.simplefilter("ignore")


def open_csv_file(path, header=0):
    if header == -1: header=None
    """Open CSV file using pandas"""
    data = pd.read_csv(path, header=header).values  # pyright: ignore
    return data

def select_column(dataset, col):
    return dataset[:,[col]]

def meshgrid(X, y, offset=1, step_size=0.05):
    """
    Create a meshgrid with a minimum of min(X, y)-h and
    a maximum of max(X, y)+h and a step size of z.
    """
    x_min, x_max, y_min, y_max = X.min()-(offset/4), X.max()+(offset/4), y.min()-(offset/4), y.max()+(offset/4)
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

# Normalize a matrix
def normalize_matrix(X):
    """
    X: input matrix containing all columns
    returns a normalized version
    """
    rows, cols = len(X), len(X[0])
    Xn = np.zeros((rows, cols))
    for i in range(cols):
        Xn[:,i] = normalize_column(X[:,i])
    return Xn

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

def polynomial(X1, X2, d, ones=True):
    """
    Non-linear two feature problems
    """
    if ones: Xe = np.c_[np.ones([len(X1),1]), X1, X2]
    else: Xe = np.c_[X1, X2]
    for i in range (2, d+1):
        for j in range(0, i+1):
            X_new = X1**(i-j)*X2**j
            X_new = X_new.reshape(-1, 1)
            Xe = np.append(Xe, X_new, 1) # 1 --> append column
            #print(f'<?> len Xe == {len(Xe)} |     i = {i} and j = {j}')
    return Xe

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

def log_gradient_descent(X, y, iterations, learning_rate):
    """
    Logarithmic gradient descent
    """
    betas = []
    n = len(X) # instances
    b = np.zeros((len(X[0]),))
    for i in range(iterations):
        s = sigmoid(np.dot(X, b)) - y
        grad = (1/n) * np.dot(X.T, s)
        b = b - learning_rate * grad 
        betas.append(b)
    return b, betas

def log_estimate_errors(Xe, y, beta):
    """
    Xe: extended matrix
    y:  real values
    beta: gradients
    """
    z = Xe.dot(beta).reshape(-1, 1) # (n, 1) matrix
    p = sigmoid(z)   # probability
    pp = np.round(p) # prediction -> 0 or 1
    yy = y.reshape(-1, 1) # (n, ) -> (n, 1)
    errors = np.sum(yy!=pp)
    return errors

def plot_linear_db(X, y, b):
    """
    X: input data, extended matrix [ 1 , x1, x2 ]
    b: beta , gradients
    decision boundary --> y = mx + c
    """
    x1 = [min(X[:,1]), max(X[:,1])]
    x2 = -(b[0] + np.dot(b[1], x1)) / b[2]
    plt.xlim([-2.3, 2.3]), plt.ylim([-2.2, 2.2])
    plt.plot(X[:,1][y==0], X[:,2][y==0], "r^") # points with y < 0.5
    plt.plot(X[:,1][y==1], X[:,2][y==1], "gs") # points with y > 0.5
    plt.plot(x1, x2, 'b')

def plot_nonlinear_db(X1, X2, y, b, d, h=0.005, lim_step=0.15):
    """
    X: input data, extended matrix [ 1 , x1, x2 ]
    b: beta , gradients
    d: degree of polynomial
    Nonlinear --> polynomial features
    """
    marker_0, marker_1 = 'X', 'v'
    x_min, x_max = X1.min() - lim_step, X1.max() + lim_step
    y_min, y_max = X2.min() - lim_step, X2.max() + lim_step
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    x1, x2 = xx.ravel(), yy.ravel()
    XXe = polynomial(x1, x2, d)
    p = sigmoid(np.dot(XXe, b))
    classes = p > 0.5
    clz_mesh = classes.reshape(xx.shape)
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF']) # mesh plot
    cmap_bold  = ListedColormap(['#FF0000', '#00FF00', '#0000FF']) # colors
    plt.pcolormesh(xx, yy, clz_mesh, cmap=cmap_light)
    plt.scatter(X1[y==0], X2[y==0], c='r', marker=marker_0, cmap=cmap_bold, edgecolors='k')
    plt.scatter(X1[y==1], X2[y==1], c='g', marker=marker_1, cmap=cmap_bold, edgecolors='k')

def log_find_best_polynomial_model(X1, X2, y, degree_range, iterations, learning_rate):
    """
    X1: first feature
    X2: second feature
    degree_range: maximum amount of degrees to test
    """
    results = []
    for d in range(1, degree_range+1):
        Xp = polynomial(X1, X2, d)
        beta = log_gradient_descent(Xp, y, iterations=iterations, learning_rate=learning_rate)[0]
        cost = log_calc_cost(Xp, y, beta)
        results.append(cost)
    results = np.array(results).reshape(-1, 1)
    best_result = np.min(results[:,0])
    idx = np.where(results == np.min(results[:,0]))[0][0]
    best_polynomial_degree = idx + 1
    return best_polynomial_degree

def log_find_best_learning_rate(Xe, y, iterations, learning_rate_range=np.arange(0, 1, 0.05)):
    """
    Xe: extended matrix
    iterations: gradient descent iterations
    learning_rate_range: array of learning rates to apply and test
    """
    costs = []
    for learning_rate in learning_rate_range:
        beta = log_gradient_descent(Xe, y, iterations, learning_rate)[0]
        cost = log_calc_cost(Xe, y, beta)
        costs.append(cost)
    results = np.array(costs) 
    best_result = np.where(results == np.min(results))
    idx = best_result[0]
    return learning_rate_range[idx]

def log_tune_polynomial_model(X1, X2, y, degree_range, iterations=10, learning_rate_range=np.arange(0, 1, 0.05)):
    """
    Tune the learning rate and the polynomial degree
    """
    results = []
    for learning_rate in learning_rate_range:
        for d in range(1, degree_range+1):
            Xp = polynomial(X1, X2, d)
            beta = log_gradient_descent(Xp, y, iterations=iterations, learning_rate=learning_rate)[0]
            cost = log_calc_cost(Xp, y, beta)
            results.append([cost, d, learning_rate])
    r = np.array(results)
    r = r[~np.isnan(r[:,0])]    # remove instances where cost == nan
    idx = np.where(r[:,0] == np.min(r[:,0]))[0]
    optimal_spec = r[idx]
    optimal_degree = optimal_spec[0][1]
    optimal_learn_rate = optimal_spec[0][2] 
    final_cost = optimal_spec[0][0]
    #print(r[r[:,0].argsort()][::-1])
    return optimal_degree, optimal_learn_rate, final_cost

def log_plot_twofeature(X1, X2, y, errors, title=True):
    """
    X1: first feature
    X2: second feature
    y:  labels
    """
    plt.xlabel('X1'), plt.ylabel('X2')
    plt.scatter(X1[y==1], X2[y==1], c='g', cmap='flag', s=35, marker='v', edgecolors='k', label='correct')
    plt.scatter(X1[y==0], X2[y==0], c='r', cmap='flag', s=35, marker='X', edgecolors='k', label='wrong')
    if title: plt.title(f"Training errors: {errors}")
    plt.legend()

def log_plot_cost(X, y, B):
    """
    X: feature matrix
    y: labels
    B: collection of betas
    NOTE: Call subplot BEFORE calling this function
    """
    s, c = 1, 'k'
    costs = []
    iterations = len(B)
    for i in range(iterations):
        cost = log_calc_cost(X, y, B[i])
        costs.append(cost)
    stabilized_cost = round((costs[-1:][0]), 6)
    x_axis = np.arange(0, iterations, 1)
    plt.scatter(x_axis, costs, s=s, c=c)
    plt.xlabel('Iterations'), plt.ylabel('Cost')
    return stabilized_cost

def log_plot_cost_db(X1, X2, y, polynomial_degree, iterations, learning_rate):
    plt.figure()
    Xp = polynomial(X1, X2, polynomial_degree)
    b, betas = log_gradient_descent(Xp, y, iterations, learning_rate)
    errors = log_estimate_errors(Xp, y, b)
    # Plot the cost 
    plt.suptitle(f'Polynomial degree: {polynomial_degree}\nIterations: {iterations}\nLearning rate: {learning_rate}')
    plt.subplot(121)
    stabilized_cost = log_plot_cost(Xp, y, betas)
    plt.title(f"Cost stabilizes at {stabilized_cost}")
    # Plot X1 and X2 with the decision boundary
    plt.subplot(122)
    log_plot_twofeature(X1, X2, y, errors)
    plot_nonlinear_db(X1, X2, y, b=b, d=polynomial_degree)
    plt.title(f"Training errors: {errors}")


def combination(arr, n):
    """
    arr: array with values
    n: subset size
    """
    if n == 0: return [[]]
    l = []
    for i in range(0, len(arr)):
        m = arr[i]
        rem = arr[i+1:]
        remCombo = combination(rem, n-1)
        for p in remCombo:
            l.append([m, *p])
    return l

def forward_selection(X, y):
    """
    Forward selection algorithm
    X: features
    y: results
    """
    Xn_e = extend_matrix(normalize_matrix(X))
    b = calc_beta(Xn_e, y)
    p = np.size(X[0]) + 1   # p features
    models = []
    mseTotal = []
    for i in range(0, p+1):
        combo = combination(b, i)
        for c in combo:
            "c: combination of beta values"
            print(c)
            models.append(c)
    print(f"Combinations: {len(models)}")
    return models


def plot_twofeature(X1, X2, y, cmap=None,s=12, markers=['o', 'o'], colors=['g', 'r'], edgecolors=[None, None]):
    """
    X1: first feature
    X2: second feature
    y:  labels
    """
    plt.xlabel('X1'), plt.ylabel('X2')
    plt.scatter(X1[y==1], X2[y==1], c=colors[0], cmap=cmap, s=s, marker=markers[0], edgecolors=edgecolors[0])
    plt.scatter(X1[y==0], X2[y==0], c=colors[1], cmap=cmap, s=s, marker=markers[1], edgecolors=edgecolors[1])

def plot_decision_boundary(clf, xx, yy, alpha=0.80, colors='k', linewidths=2.0, levels=[1.0]):
    """
    clf: trained classifier
    xx, yy: meshgrid
    """
    plt.contour(xx, yy, clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape), 
                colors=colors, alpha=alpha, linewidths=linewidths, levels=levels
                )

def plot_decision_boundary_shade(clf, xx, yy, alpha=0.80, cmap='plasma'):
    """
    clf: trained classifier
    xx, yy: meshgrid
    """
    plt.contour(xx, yy, clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape), 
                alpha=alpha, cmap=cmap
                )

def stopwatch(start=None):
    """Measure time taken"""
    if start == None:
        t_ms = time.time()
        return t_ms
    else:
        t_diff = round(time.time() - start, 5)
        print(f"[TIME] Time spent: {t_diff} s")





