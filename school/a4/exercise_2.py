from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from math import sqrt, floor
from sklearn.svm import SVC
import numpy as np
import sys
import ml

#np.set_printoptions(threshold=sys.maxsize)

# Clustering
# Implement 'Bisecting k-Means'
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,:2], data[:,2]
X1, X2 = X[:,0], X[:,1]

def calc_distance(v1, v2):
    """
    Calculate distance between vector 1 and vector 2
    """
    difference = np.subtract(v1, v2)
    return np.linalg.norm(v1 - v2)

def reduce_dim(X, d):
    """
    Reduce 'd' dimension of data X
    """
    kmeans = KMeans(n_clusters=d).fit(X)
    X_transform = kmeans.transform(X)
    return X_transform

def sammon(X, X_old):
    inv = np.divide(1, sum(X_old))
    #print(inv)
    e = ( ( X_old - X )**2 / X_old )
    E = inv * e
    print(E)
    return E

lst = [[3, 0.25], [2.9,0.8]]
arr = np.array(lst)

reduced = reduce_dim(X, 1)
new_dist = calc_distance(X, reduced)
sammon(X, reduced)
