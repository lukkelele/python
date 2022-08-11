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


def combination(arr, n, start_arr):
    if n == 0: return [[]]
    l = []
    lst = [0, 0, 0, 0]
    for i in range(0, len(arr)):
        m = arr[i]
        m_last_idx = len(start_arr) - start_arr.index(m) 
        #print(f"mlast_idx = {m_last_idx}")
        rem = arr[i+1:]
        remCombo = combination(rem, n-1, start_arr)
        for p in remCombo:
            l.append([m, *p])
            if p != []:
                for k in p:
                    lst[start_arr.index(k)] = k
            print(f"lst => {lst}")
        #print(f"l: {l}")
        print()
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
    mseTotal = []
    for i in range(0, p+1):
        combo = combination(b, i, b)
        for c in combo:
            "c: combination of beta values"
            print(c)
            models.append(c)
    print(f"Combinations: {len(models)}")
    return models



a = [1, 2, 4, 8]
A = combination(a, 3, a)
print(f"\n\n{A}")

#M = ml.forward_selection(X, y)







