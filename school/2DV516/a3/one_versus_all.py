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
param_rbf  = {'C': [0.1, 1, 10, 100, 1000, 10000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'kernel': ['rbf']      }

class OneVersusAll:

    def __init__(self, path, tune_params=False):
        self.fig = plt.figure(figsize=(20,11))
        self.load_mnist_data()
        self.clf_rbf = svm.SVC(kernel='rbf', C=1000, gamma=0.01)
        self.clf_rbf.fit(self.x_training, self.y_training)

    def load_mnist_data(self):
        (self.x_training, self.y_training), (self.x_test, self.y_test) = mnist.load_data()
        print(self.x_training.shape)
        n, nx, ny = self.x_training.shape
        self.x_training = self.x_training.reshape((n,nx*ny))
        print(self.x_training.shape)

    def divide_data(self, X, Y, training):
        test = 1 - training
        rows = np.size(X,0)
        idx = round(test*rows) - 1
        self.x_test = X[:idx]
        self.y_test = Y[:idx]
        self.x_training = X[idx:]
        self.y_training = Y[idx:]

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
