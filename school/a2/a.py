from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml


path = './data/girls_height.csv'
data = ml.open_csv_file(path)

row_length = len(data[:,0][0].split())
X = np.zeros((len(data), row_length))
X0, X1, X2 = np.zeros((len(data), 1)), np.zeros((len(data), 1)), \
             np.zeros((len(data), 1))

# Fix the data format
i = 0 
for entry in data[:,0]:
    e = entry.split()
    X[i][0], X[i][1], X[i][2] = e[0], e[1], e[2]
    X0[i] = e[0]
    X1[i] = e[1]
    X2[i] = e[2]
    i += 1


# Extend matrix X1 and X2 by a single column of ones
X12 = np.c_[X1, X2]
Xe = ml.extend_matrix(X12)

parents = np.array([1, 65, 70])
beta = ml.calc_beta2(Xe, parents)
print(beta)




