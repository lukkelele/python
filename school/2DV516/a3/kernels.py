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

path = './data/mnistsub.csv'
SAMPLE_SIZE = 5000

param_linear = {'C': [0.1, 1, 5, 10, 50, 100, 1000],
                'kernel': ['linear']        
             }
param_rbf  = {'C': [0.1, 1, 10, 100, 1000, 10000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'kernel': ['rbf']
             }
param_poly = {'C': [0.1, 1, 10, 100, 1000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'degree': [1, 2, 3, 4],
             'kernel': ['poly']
             }

params = [param_linear, param_rbf, param_poly]

class Kernel:

    def __init__(self, path):
        data = pd.read_csv(path).values
        self.fig = plt.figure(figsize=(18,8))
        self.X = data[:,[0,1]] 
        self.Y = data[:,2]

    def create_classifiers(self, ):
        clf_linear = a3.get_classifier(kernel='linear')

    def tune_hyperparams(self, X, Y, verbose=0):
        for param in params:
            start = time()
            grid_search = GridSearchCV(svm.SVC(), param, refit=True)
            grid_search.fit(X, Y)
            time_spent = time() - start
            if time_spent > 60: print(f"Grid search for {param['kernel']} completed in {round((time_spent/60),2)} minutes")
            else: print(f"Grid search for {param['kernel']} completed in {time_spent} seconds")
            print(grid_search.best_params_)

    def tune_linear(self, X, Y):
        linear_grid_search = GridSearchCV(svm.SVC(), param_linear, refit=True)
        linear_grid_search.fit(X, Y)
        self.linear_params = linear_grid_search.best_params_
        print(linear_grid_search.best_params_)

    def tune_poly(self, X, Y):
        poly_grid_search = GridSearchCV(svm.SVC(), param_poly, refit=True)
        poly_grid_search.fit(X, Y)
        self.poly_params = poly_grid_search.best_params_
        print(poly_grid_search.best_params_)

    def tune_rbf(self, X, Y):
        rbf_grid_search = GridSearchCV(svm.SVC(), param_rbf, refit=True)
        rbf_grid_search.fit(X, Y)
        self.rbf_params = rbf_grid_search.best_params_
        print(rbf_grid_search.best_params_)



k = Kernel(path)
k.tune_hyperparams(k.X, k.Y)

