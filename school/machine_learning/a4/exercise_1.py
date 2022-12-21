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
fig = plt.figure(figsize=(12,12))

def calculate_sse(points):
    """
    Sum of squared errors
    """
    centroid = np.mean(points, 0)
    sum_errors = np.sum(np.linalg.norm(points-centroid, axis=1, ord=2))
    return sum_errors 

def get_clusters(points):
    kmeans = KMeans(n_clusters=2).fit(points)
    labels = kmeans.labels_
    most_frequent = np.bincount(labels).argmax()     # pyright : ignore
    print(most_frequent)
    indices = np.where(labels == 1)[0]
    split1 = points[indices]
    split2 = np.delete(points, indices, axis=0)
    return split1, split2

def bkmeans(X, n, cmap='plasma'):
    """
    Bisect kmeans
    Create one cluster initially
    Sort the largest cluster in to two
    Take largest cluster and split it -> REPEAT
    Initially [ 0 ] 
    Then -> [0, 1] -> [0, 1, 2] -> [1, 2, 3, 4] etc..
    Should return the cluster indices for each observation
    """
    print(f"SIZE OF X: {len(X)}")
    c1, c2 = get_clusters(X)
    clusters = [c1, c2]
    for i in range(1, n):
        for cluster in clusters:
            sse_points = calculate_sse(cluster)            
        # Take cluster with largest error
        cluster = clusters.pop(np.argmax(sse_points))    #pyright: ignore
        c = get_clusters(cluster)
        clusters.extend(c)
    return clusters


clusters = bkmeans(X, 5)
cmap = 'plasma'
for cluster in clusters:
    plt.scatter(cluster[:,0], cluster[:,1], cmap=cmap, edgecolors='k', s=125)

plt.show()
