from sklearn.model_selection import train_test_split, GridSearchCV
from matplotlib import pyplot as plt
from sklearn import gaussian_process
from sklearn import metrics
from sklearn import svm 
from time import sleep
from time import time
import pandas as pd
import a3_lib as a3
import numpy as np

# Optimized parameters
# Linear ==> C=1
# Poly ==> C=1, degree=1, gamma=1
# RBF ==> C=1000, gamma=0.01
# 2D to determine a number (1, 3, 5, 9)

path = './data/mnistsub.csv'
# Linear: C | RBF: C, gamma | Poly: C, degree, gamma |
#   idx 0   |   idx 0, 1    |      idx 0, 1, 2       | 
param_linear = {'C': [0.1, 1, 5, 10, 50, 100, 1000],
                'kernel': ['linear']    }
param_rbf  = {'C': [0.1, 1, 10, 100, 1000, 10000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'kernel': ['rbf']      }
param_poly = {'C': [0.1, 1, 10, 100, 1000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'degree': [1, 2, 3, 4],
             'kernel': ['poly']     }

params = [param_linear, param_rbf, param_poly]
optimized_params = [[1], [1000, 0.01], [1, 1, 1]] 

class Kernel:

    def __init__(self, path, tune_params=False):
        data = pd.read_csv(path).values
        self.fig = plt.figure(figsize=(18,8))
        self.X = data[:,[0,1]] 
        self.Y = data[:,2]
        if tune_params: self.tune_hyperparams(X, Y)
        else: self.param_linear, self.param_rbf, self.param_poly = optimized_params[0], optimized_params[1], optimized_params[2]
        self.create_classifiers(verbose=True)
        print(self.X.shape)
        self.clf_linear.fit(self.X, self.Y), self.clf_rbf.fit(self.X, self.Y), self.clf_poly.fit(self.X, self.Y)

    def create_classifiers(self, verbose=False):
        self.clf_linear = svm.SVC(kernel='linear', C=self.param_linear[0])
        self.clf_poly = svm.SVC(kernel='poly', C=self.param_poly[0], degree=self.param_poly[1], gamma=self.param_poly[2])
        self.clf_rbf = svm.SVC(kernel='rbf', C=self.param_rbf[0], gamma=self.param_rbf[1])
        if verbose: print(f"All classifiers created!\nlinear: {self.clf_linear}\nrbf: {self.clf_rbf}\npoly: {self.clf_poly}")
        
    def tune_hyperparams(self, X, Y):
        for param in params:
            start = time()
            grid_search = GridSearchCV(svm.SVC(), param, refit=True)
            grid_search.fit(X, Y)
            time_spent = time() - start
            if time_spent > 60: print(f"Grid search for {param['kernel']} completed in {round((time_spent/60),2)} minutes")
            else: print(f"Grid search for {param['kernel']} completed in {time_spent} seconds")
            print(grid_search.best_params_)

    def plot_data(self, X, Y):
        xx, yy = a3.make_meshgrid(X, Y)
        plt.subplot(131)
        plt.scatter(X[:,0], X[:,1], s=12, edgecolors='k') 
        a3.plot_contour(self.clf_linear, xx, yy)
        plt.subplot(132)
        plt.scatter(X[:,0], X[:,1], s=12, edgecolors='k')
        a3.plot_contour(self.clf_rbf, xx, yy)
        plt.subplot(133)
        plt.scatter(X[:,0], X[:,1], s=12, edgecolors='k')
        a3.plot_contour(self.clf_poly, xx, yy)



k = Kernel(path)
k.plot_data(k.X, k.Y)
plt.show()
