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
import csv
import sys
import ml

#np.set_printoptions(threshold=sys.maxsize)

# ONE VERSUS ALL MNIST
# RBF kernel, 95% test accuracy
# 784 features
print('>> Getting mnist_784 dataset...')
X, y = fetch_openml('mnist_784', version=1, data_home="~/Software/datasets/", return_X_y=True)
print('   Done!\n>> Splitting data...')
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.25, test_size=0.10)
train_size = len(X_train)
test_size = len(X_test)
print('>> Data read\n   Size of training set: %s\n   Size of test set: %s' % (train_size, test_size))

C_arr = np.logspace(-3, 13, 11)
g_arr = np.logspace(-3, 8, 11)
params = { 'C': C_arr, 'gamma': g_arr, 'kernel': ['rbf']}

print('   Done!\n>> Creating SVC...')
start = ml.stopwatch()
#clf = SVC(kernel='rbf', C=0.35)
clf = SVC()
print('   SVC created\n>> Starting grid search...')
grid = GridSearchCV(clf, params)
grid.fit(X_train, y_train)
clf_val_score_mean = cross_val_score(grid, X_test, y_test, scoring='accuracy', cv=2).mean()
print('>> Calculating score for classifier')
test_acc = grid.score(X_test, y_test)
print(f"\nTest accuracy: {test_acc}\nValidation score: {clf_val_score_mean}")

print(f">> Best estimator:\n   {grid.best_estimator_}")

print(f"Time spent: {ml.stopwatch(start)}")



