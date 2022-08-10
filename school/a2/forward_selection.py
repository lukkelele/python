from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import numpy as np
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)


data = ml.open_csv_file('./data/GPUbenchmark.csv')
X, y = data[:, :6], data[:, 6]

def combination(arr, n):
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
    Xn_e = ml.extend_matrix(ml.normalize_matrix(X))
    b = ml.calc_beta(Xn_e, y)
    p = np.size(X[0]) + 1   # p features
    models = []
    for i in range(1, p+1):
        combo = combination(b, i)
        models.append(combo)
        print(combo)
        
    return models


M = forward_selection(X, y)


