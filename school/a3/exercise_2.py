from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.datasets import fetch_openml, load_digits
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import numpy as np
import sys
import ml

#np.set_printoptions(threshold=sys.maxsize)

# ONE VERSUS ALL MNIST
# RBF kernel, 95% test accuracy

X, y = fetch_openml('mnist_784', version=1, data_home="~/Software/datasets/", return_X_y=True)
#X, y = mnist['data'], mnist['target']   # pyright: ignore
mnist = load_digits()
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.10)
train_size = len(X_train)
X_test, y_test = X_test[:train_size], y_test[:train_size]
print('>> Data read\n   Size of training set: %s' % train_size)
#C_arr = np.arange(0.1, 1, 0.01)
#gamma_arr = np.logspace(-10, 3, 12)
C_arr = np.arange(0.1, 1, 0.1)
gamma_arr = np.arange(0.10, 1, 0.1)
param_grid_rbf = {
         'C': C_arr,
         'gamma': gamma_arr,
         'kernel': ['rbf']
         }

clf = SVC()
grid = GridSearchCV(clf, param_grid_rbf)
grid.fit(X_train, y_train)
acc = grid.score(X_test, y_test)
#print("Accuracy: %f", acc)
print(f"Accuracy: {acc}")
print(f"\nBest params: {grid.best_params_}\nBest score: {grid.best_score_}")
