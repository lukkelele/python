from sklearn.model_selection import train_test_split, GridSearchCV
from matplotlib import pyplot as plt
from keras.datasets import mnist
from sklearn import metrics
from sklearn import svm 
from time import time
import pandas as pd
import a3_lib as a3
import numpy as np

path = './data/mnistsub.csv'

# Optimized parameters
# Linear ==> C=1
# Poly ==> C=1, degree=1, gamma=1
# RBF ==> C=1000, gamma=0.01
# 2D to determine a number (1, 3, 5, 9)

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

class OneVersusAll:

    def __init__(self, path, tune_params=False):
        data = pd.read_csv(path).values
        self.fig = plt.figure(figsize=(20,11))
        self.X = data[:,[0,1]] 
        self.Y = data[:,2]
        self.divide_data(self.X, self.Y, 0.8)
        if tune_params: self.tune_hyperparams(X, Y)
        else: self.param_rbf = optimized_params[1]
        self.create_classifiers(verbose=False)
        self.clf_rbf.fit(self.X, self.Y)

    def divide_data(self, X, Y, training):
        test = 1 - training
        rows = np.size(X,0)
        idx = round(test*rows) - 1
        self.x_test = X[:idx]
        self.y_test = Y[:idx]
        self.x_training = X[idx:]
        self.y_training = Y[idx:]

    def create_classifiers(self, verbose=False):
        self.clf_rbf = svm.SVC(kernel='rbf', C=self.param_rbf[0], gamma=self.param_rbf[1])
        if verbose: print(f"All classifiers created!\nrbf: {self.clf_rbf}\n")
        
    def tune_hyperparams(self, X, Y):
        start = time()
        grid_search = GridSearchCV(svm.SVC(), param_rbf, refit=True)
        grid_search.fit(X, Y)
        time_spent = time() - start
        if time_spent > 60: print(f"Grid search for RBF completed in {round((time_spent/60),2)} minutes")
        else: print(f"Grid search for RBF completed in {time_spent} seconds")
        print(grid_search.best_params_)



one = OneVersusAll(path)
print(one.x_training.size)
print(one.x_test.size)
print(one.x_training.shape)
print(one.x_test.shape)
