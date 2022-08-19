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


def convert_points(points):
    """
    Point conversion
    points: list in a 2D format
    """
    points = np.array(points)
    if len(points.shape) == 1:
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
    center = np.mean(points, 0)
    sum_errors = np.sum(np.linalg.norm(points-center, axis=1, ord=2))
    return sum_errors 

def k_means(points, k):
    """
    Cluster points into k clusters
    k >= 2
    """
    points = typecheck(points) 
    assert len(points) >= 2, "error: k must be larger or equal to 2"
    









