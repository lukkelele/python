from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import numpy as np
import sys
import ml

data = ml.open_csv_file('./data/GPUbenchmark.csv')
X, y = data[:, :6], data[:, 6]

def forward_selection(X, y, d):
    # Normalize and extend X
    Xne = ml.extend_matrix(ml.normalize_matrix(X))
    y = ml.normalize_matrix(y)
    beta = ml.calc_beta(Xne, y)
    mse_tot, scores = [], []
    cv = KFold(n_splits=3, random_state=2, shuffle=True)
    print('>> testing models...')
    for i in range(d+1):
        x = X[:,:i]
        xne = ml.extend_matrix(ml.normalize_matrix(x))
        clf = LinearRegression().fit(xne, y)
        beta = ml.calc_beta(xne, y)
        y_pred = xne.dot(beta)
        mse = ml.calc_MSE(y, y_pred)
        mse_tot.append(mse)
        cv_sum = 0
        cross_val = cross_val_score(clf, xne, y, cv=cv)
        scores.append(cross_val)
        print(f">> features: {i}     mse : {mse}    cross_val_score: {cross_val}")
    mse_tot = np.array(mse_tot) 
    idx = np.where(mse_tot == min(mse_tot))[0]
    if len(idx) > 1: idx = idx[0]   # incase mse stabilizes
    print(f">> Best model(s) (according to MSE): {idx}    MSE: {mse_tot[idx]}")
    scores = np.array(scores)
    best_idx = np.where(scores == np.max(scores))[0]
    print(f">> Cross validation:\n   Best model: {best_idx}")
    count = 0
    for result in scores:
        cv_score_avg = result.mean()
        print(f">> Model {count} : {cv_score_avg}")
        count += 1
    

forward_selection(X, y, 8)
