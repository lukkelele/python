from sklearn.model_selection import train_test_split, GridSearchCV
from matplotlib import pyplot as plt
from sklearn import gaussian_process
from sklearn import metrics
from sklearn import svm 
import pandas as pd
import a3_lib as a3
import numpy as np

path = './data/mnistsub.csv'
SAMPLE_SIZE = 5000

param_linear = {'C': [0.1, 1, 10, 100, 1000],
                'kernel': ['linear']        
             }
param_rbf  = {'C': [0.1, 1, 10, 100, 1000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'kernel': ['rbf']
             }
param_poly = {'C': [0.1, 1, 10, 100, 1000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'degree': [1, 2, 3, 4, 5],
             'kernel': ['poly']
             }

class Kernel:

    def __init__(self, path):
        data = pd.read_csv(path).values
        self.fig = plt.figure(figsize=(18,8))
        self.X = data[:,[0,1]] 
        self.Y = data[:,2]

    def create_classifiers(self, ):
        clf_linear = a3.get_classifier(kernel='linear')

    def tune_hyperparams(self, X, Y, verbose=0):
        linear_grid_search = GridSearchCV(svm.SVC(), param_linear, refit=True, verbose=verbose)
        poly_grid_search = GridSearchCV(svm.SVC(), param_poly, refit=True, verbose=verbose)
        rbf_grid_search = GridSearchCV(svm.SVC(), param_rbf, refit=True, verbose=verbose)
        linear_grid_search.fit(X, Y)
        poly_grid_search.fit(X, Y)
        rbf_grid_search.fit(X, Y)
        self.linear_params = linear_grid_search.best_params_
        self.poly_params = poly_grid_search.best_params_
        self.rbf_params = rbf_grid_search.best_params_
        print(f"Tuned hyperparameters:\n===> LINEAR\n{linear_grid_search.best_params_}\n"+
                f"===> POLY\n{poly_grid_search.best_params_}\n===> RBF\n{rbf_grid_search.best_params_}")


k = Kernel(path)
k.tune_hyperparams(k.X, k.Y)
