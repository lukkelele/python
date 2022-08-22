from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import numpy as np
import sys
import ml

data = ml.open_csv_file('./data/GPUbenchmark.csv')
X, y = data[:, :6], data[:, 6]
cv = 3
# Split data into three folds
t = round(len(X) / 3) - 1
X1, X2, X3 = X[:t,:], X[t:2*t,:], X[2*t:3*t,:]
d = 9
Xn1, Xn2, Xn3 = ml.extend_matrix(ml.normalize_matrix(X1)),\
                ml.extend_matrix(ml.normalize_matrix(X2)),\
                ml.extend_matrix(ml.normalize_matrix(X3))
XN = [Xn1, Xn2, Xn3]
#def forward_selection(X, y, d, cv=3):
# Normalize and extend X
Xne = ml.extend_matrix(ml.normalize_matrix(X))
y = ml.normalize_matrix(y)
y1, y2, y3 = y[:t,:], y[t:2*t,:], y[2*t:3*t]
Y = [y1, y2, y3]
beta = ml.calc_beta(Xne, y)
print('>> testing models...')

for i in range(1,d+1):
    mse_tot = []
    scores = []
    print(f">> features: {i}")           
    idx = 0
    for x in XN:
        y = Y[idx]
        xne = x #ml.extend_matrix(ml.normalize_matrix(x))
        beta = ml.calc_beta(xne, y)
        y_pred = xne.dot(beta)
        mse = ml.calc_MSE(y, y_pred)
        mse_tot.append(mse)
        print(f"==> mse: {mse}")
        score = 1 - mse
        scores.append(score) 
    idx+=1
    mse_tot = np.array(mse_tot) 
    idx = np.where(mse_tot == min(mse_tot))[0]
    if len(idx) > 1: idx = idx[0]   # incase mse stabilizes
    print(f">> Best model(s) (according to MSE): {idx}    MSE: {mse_tot[idx]}")
    avg_score = sum(scores) / t
    print(f">> Avg score: {avg_score}")
