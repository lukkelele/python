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

def forward_selection(X, y):
    """
    Forward selection algorithm
    X: features
    y: results
    """
    Xn_e = ml.extend_matrix(ml.normalize_matrix(X))
    b = ml.calc_beta(Xn_e, y)
    null_model = []
    models = []
    p = np.size(X[0]) + 1   # p features
    for j in range(p):
        for i in range(j, p):
            m = []
            m.append(b[i])
            for k in range(i, p):
                if i != k:
                    m.append(b[k])
            models.append(m)

    return models


M = forward_selection(X, y)

for m in M:
    print(m)
print(len(M))
