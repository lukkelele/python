from sklearn.model_selection import train_test_split, GridSearchCV
from matplotlib import pyplot as plt
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

class Kernel:

    def __init__(self, path, tune_params=False):
        data = pd.read_csv(path).values
        self.fig = plt.figure(figsize=(20,11))
        self.X = data[:,[0,1]] 
        self.Y = data[:,2]
        self.divide_data(self.X, self.Y, 0.8)
        if tune_params: self.tune_hyperparams(X, Y)
        else: self.param_linear, self.param_rbf, self.param_poly = optimized_params[0], optimized_params[1], optimized_params[2]
        self.create_classifiers(verbose=False)
        self.clf_linear.fit(self.x_training, self.y_training)
        self.clf_poly.fit(self.x_training, self.y_training)
        self.clf_rbf.fit(self.x_training, self.y_training)

    def divide_data(self, X, Y, training):
        test = 1 - training
        rows = np.size(X,0)
        idx = round(test*rows) - 1
        self.x_test = X[:idx]
        self.y_test = Y[:idx]
        self.x_training = X[idx:]
        self.y_training = Y[idx:]

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
        point_size = 15
        alpha = 0.5
        xx, yy = a3.make_meshgrid(self.x_test[:,0], self.x_test[:,1], h=12, step=0.1)
        plt.subplot(131)
        pred_lin = self.clf_linear.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        plt.contourf(xx, yy, pred_lin, alpha=alpha)
        scatter_linear = plt.scatter(X[:,0], X[:,1], s=point_size, c=Y, edgecolors='k')
        a3.set_lims(X)
        plt.legend(*scatter_linear.legend_elements(), loc="best", bbox_to_anchor=(0.5, 0., 0.5, 0.5), title="Linear")
        plt.subplot(132)
        pred_poly = self.clf_poly.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        plt.contourf(xx, yy, pred_poly, alpha=alpha)
        scatter_poly = plt.scatter(X[:,0], X[:,1], s=point_size, c=Y, edgecolors='k')
        a3.set_lims(X)
        plt.legend(*scatter_poly.legend_elements(), loc="best", bbox_to_anchor=(0.5, 0., 0.5, 0.5), title="Poly")
        plt.subplot(133)
        pred_rbf = self.clf_rbf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        plt.contourf(xx, yy, pred_rbf, alpha=alpha)
        scatter_rbf = plt.scatter(X[:,0], X[:,1], s=point_size, c=Y, edgecolors='k')
        a3.set_lims(X)
        plt.legend(*scatter_rbf.legend_elements(), loc="best", bbox_to_anchor=(0.5, 0., 0.5, 0.5), title="RBF")


k = Kernel(path)
k.plot_data(k.x_test, k.y_test)
plt.show()
