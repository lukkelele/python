from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from math import sqrt, floor
from sklearn.svm import SVC
import numpy as np
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)

# Clustering
# Implement 'Bisecting k-Means'
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,:2], data[:,2]
fig = plt.figure(figsize=(12,12))

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
    pidx = 0
    for centroid in centroids:
        centroid_idx = np.where(centroids == centroid)[0][0]
        for point in points:
            point_idx = np.where(points == point)[0][0]
            dist = ml.euclidean_distance(point, centroid)
            distances.append([dist, pidx, centroid_idx])
            pidx += 1

    # Sort the distances array by the point indexes
    distances = np.array(distances)
    distances = distances[distances[:,1].argsort()]
    print(distances.shape)
    #for dist in distances: print(f"dist: {dist}")

    # Determine the shortest distance for each entry with same point index
    cpoints = []
    entries = int(len(distances) / 2)
    # Distances: [ distance, point_index, cluster_index ] 
    p_idx = 0
    for i in range(entries):
        p1, p2 = distances[p_idx], distances[p_idx]
        # if p1 distance is less than p2
        if p1[0] < p2[0]:
            cpoints.append(p1)
        else:
            cpoints.append(p2)
        p_idx += 1

    # cpoints now hold point indexes with their assigned cluster and distance
    # Color each point according to its cluster index
    cpoints = np.array(cpoints)
    cpoints = cpoints[cpoints[:,1].argsort()]
    idx = 0

    # Plot the centroids
    centroids_ = np.arange(0, len(centroids), 1)
    plt.scatter(centroids[:,0], centroids[:,1], s=280, cmap='summer',
                c=centroids_, edgecolors='k', alpha=0.55)
    # Plot the points with their assigned cluster labels 
    print(entries)
    plt.scatter(points[:,0], points[:,1], c=cpoints[:,2], s=80, cmap='Set3_r', edgecolors='k')

# NORMALIZED DATA
lst = [ [0.45, 0.6], [0.4, 0.3] , [0.1, -0.32] , [-0.24, 0.42]]
k_means(X, 3)

plt.show()
