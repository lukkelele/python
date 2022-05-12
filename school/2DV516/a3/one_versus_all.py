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
        self.load_mnist_data(train=0.05, test=0.02)
        self.clf_rbf = svm.SVC(kernel='rbf', C=1000, gamma=0.01)
        self.clf_rbf.fit(self.x_train, self.y_train)

    def load_mnist_data(self, train=0.10, test=0.05, verbose=False):
        start = time()
        (X, y), (x_test, y_test) = mnist.load_data()
        x_train, x_test, y_train, self.y_test = train_test_split(
            X, y, train_size=train)
        n, nx, ny = x_train.shape
        self.x_train = x_train.reshape((n,nx*ny))
        n, nx, ny = x_test.shape
        self.x_test = x_test.reshape((n, nx*ny))
        self.y_train = y_train
        if verbose: print(f"Time spent loading MNIST dataset ==> {round((time()-start), 2)} seconds")

    def evaluate_model(self):
        pred = self.clf_rbf.predict(self.x_test)
        actual = self.y_test
        conf_matrix = metrics.confusion_matrix(actual, pred)
        clf_report = metrics.classification_report(actual, pred)
        print(conf_matrix)
        print(clf_report)

    def tune_hyperparams(self, X, Y):
        start = time()
        grid_search = GridSearchCV(svm.SVC(), param_rbf, refit=True)
        grid_search.fit(X, Y)
        time_spent = time() - start
        if time_spent > 60: print(f"Grid search for RBF completed in {round((time_spent/60),2)} minutes")
        else: print(f"Grid search for RBF completed in {time_spent} seconds")
        print(grid_search.best_params_)


one = OneVersusAll(path)
one.evaluate_model()
