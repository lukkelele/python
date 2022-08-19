from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.neural_network import MLPClassifier
from matplotlib.ticker import MultipleLocator
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
from sklearn.svm import SVC
import numpy as np
import sys
import ml

# Clustering
# Implement 'Bisecting k-Means'
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,:2], data[:,2]

def convert_points(points):
    """
    Point conversion
    points: list in a 2D format
    """
    points = np.array(points)
    if len(points.shape) == 1:
        print('Reshaping')
        points = points.reshape(-1, 1) 
    return points

def typecheck(arr):
    """
    Typecheck for input data
    If 'arr' is a list, convert to a 2D numpy array
    Else, do nothing
    """
    if isinstance(arr ,list):
        arr = convert_points(arr)
    return arr

def calculate_sse(points):
    """
    Sum of squared errors
    """
    points = typecheck(points)
    centroid = np.mean(points, 0)
    sum_errors = np.sum(np.linalg.norm(points-centroid, axis=1, ord=2))
    return sum_errors 


def k_means(points, k):
    """
    Cluster points into k clusters, k >= 2
    k clusters means k centroids
    Initially place random centroids then,
    calculate labels, replace centroid --> repeat
    """
    points = typecheck(points) 
    print(f"Points shape: {points.shape}")
    assert len(points) >= 2, "error: k must be larger or equal to 2"
    
    centroids = []
    for i in range(k):
        centroid = np.random.random(size=(1,2))[0]
        centroids.append(centroid)
    centroids = np.array(centroids) 

    # Distances: [ distance, point_index, cluster_index ] 
    distances = []
    for centroid in centroids:
        centroid_idx = np.where(centroids == centroid)[0][0]
        for point in points:
            point_idx = np.where(points == point)[0][0]
            dist = ml.euclidean_distance(point, centroid)
            distances.append([dist, point_idx, centroid_idx])

    # Sort the distances array by the point indexes
    distances = np.array(distances)
    distances = distances[distances[:,1].argsort()]
    for dist in distances:
        print(f"dist: {dist}")

    print()
    # Determine the shortest distance for each entry with same point index
    cpoints = []
    entries = int(len(distances) / 2)
    for i in range(entries):
        points = np.where(distances[:,1] == i)[0]
        p1_idx, p2_idx = points[0], points[1]
        p1, p2 = distances[p1_idx], distances[p2_idx]
        # if p1 distance is less than p2
        if p1[0] < p2[0]: cpoints.append(p1)
        else: cpoints.append(p2)

    # cpoints now hold point indexes with their assigned cluster and distance

    for val in cpoints:
        print(val)


lst = [ [3,10], [6,2] , [29, 0.4] ]
k_means(lst, 2)

ml.plot_twofeature(X[:,0], X[:,1], y, edgecolors=['k','k'], s=20)

#plt.show()
