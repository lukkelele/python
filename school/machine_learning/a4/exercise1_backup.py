from sklearn.model_selection import cross_val_score, GridSearchCV
from matplotlib.colors import ListedColormap
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


def k_means(points, k, n=5):
    """
    Cluster points into k clusters, k >= 2
    k clusters means k centroids
    Initially place random centroids then,
    calculate labels, replace centroid --> repeat
    """
    points = typecheck(points) 
    assert len(points) >= 2, "error: k must be larger or equal to 2"
    
    np.random.seed(4)
    np.random.shuffle(points)
    centroids = points[0:k, :]
    print(f">> Intiial centroids \n{centroids}\n\n")

    # Calculate points distance to each cluster
    clusters = k * [None]
    for i in range(1, k):
        for point in points:
            distances = []
            for centroid in centroids:
                dist = ml.euclidean_distance(centroid, point)
                #dist = ml.euclidean_distance(point, centroid)
                distances.append(dist)
            distances = np.array(distances)
            c_idx = np.where(distances == min(distances))[0][0] # cluster index
            if clusters[c_idx] is None:     # can't use '==' here because of numpy implementation
                clusters[c_idx] = point.reshape(1,2)
            else:
                clusters[c_idx] = np.vstack((clusters[c_idx], point))

        # Calculate the mean of the centroids in the clusters
        # Set this new mean to be the value for the centroids and recalculate distances
        centroids = np.array([np.mean(c, 0) for c in clusters])
    
    # Plot the data
    cmap = 'rainbow'
    centroids_ = np.arange(0, len(centroids), 1)

    for cluster in clusters:
        idx = clusters.index(cluster)
        plt.scatter(centroids[idx][0], centroids[idx][1], s=300, edgecolors='k', alpha=0.89)
        plt.plot(cluster[:,0], cluster[:,1], 'o')
    


# NORMALIZED DATA
lst = [ [0.45, 0.6], [0.4, 0.3] , [0.1, -0.32] , [-0.24, 0.42]]
k_means(X, 3)

plt.show()
