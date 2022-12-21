from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from math import sqrt, floor
from sklearn.svm import SVC
import numpy as np
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)

# Clustering
# Implement 'Bisecting k-Means'
data = ml.open_csv_file('./data/microchips.csv')
X = data[:,:2]
X1, X2 = X[:,0], X[:,1]


def reduce_dim(X, d):
    """
    Reduce 'd' dimension of data X using KMeans
    """
    kmeans = KMeans(n_clusters=d).fit(X)
    X_transform = kmeans.transform(X)
    return X_transform

def transform_pca(X, d):
    """
    X: data
    d: dimension
    """
    pca_ = PCA(n_components=d).fit(X)
    reduced_X = pca_.transform(X)
    return reduced_X 

def calc_distance(v1, v2):
    dist = np.linalg.norm(v1 - v2)
    return dist

def calc_error(X, X_new):
    d = calc_distance(X_new,X_new) + np.eye(X.shape[0])
    delta = X.sum() - d
    E = ((delta**2) * ( 1 / X.sum())).sum()
    return E

def sammon(X, d, iterations=100):
    """
    Sammon's Mapping
    """
    N = X.shape[0]
    scale = 0.5 / X.sum()
    D = X.sum() + np.eye(N)
    Dinv = 1 / D
    # Initial PCA transformation, could use a random init as well
    #y = transform_pca(X, d)
    y = np.random.normal(0.0,1.0,[N,d])
    ones = np.ones([N,d])
    d = calc_distance(y, y) + np.eye(N)
    dinv = 1.0 / d
    delta = D - d
    E = ((delta**2)*Dinv).sum()

    #H = np.dot(dinv3, y2) - deltaone - np.dot(2,y) * np.dot(dinv3,y) + y2 * np.dot(dinv3, ones)
    for i in range(iterations):
        delta = dinv - Dinv
        deltaone = delta.dot(ones)
        grad = np.nan_to_num(delta.dot(y) - (y * deltaone))
        y = y - grad
        d = calc_distance(y, y) + np.eye(N)
        dinv = 1 / d
        delta = D - d
        E_new = ((delta**2)*Dinv).sum()
        print(E_new)



    E = E * scale
    return y, E


yy, EE = sammon(X, 1, iterations=100)






