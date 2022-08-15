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
#X, y = fetch_openml('mnist_784', version=1, data_home="~/Software/datasets/", return_X_y=True)
#X.to_csv('X_mnist.csv', encoding='utf-8')
#y.to_csv('y_mnist.csv', encoding='utf-8')

tp = 0.25   # % of train set size for test set
train_size = 600
test_size = round(tp * train_size)
test_slice = train_size + test_size
print('>> Opening MNIST csv files...')
X, y = ml.open_csv_file('data/X_mnist.csv'), ml.open_csv_file('data/y_mnist.csv')
X_train, X_test = X[:train_size], X[train_size:test_slice]
# Filter out rows from y as well
y_train, y_test = y[:train_size][:,1], y[train_size:test_slice][:,1]
print('>> Data read\n   Size of training set: %s\n   Size of test set: %s' % (train_size, test_size))

#C_arr = np.arange(0.1, 1, 0.01)
#gamma_arr = np.logspace(-10, 3, 12)
print('>> Creating C and gamma arrays')
step_C = 0.05
step_gamma = 0.2
C_arr = np.arange(0.10, 1, step_C)
gamma_arr = np.arange(0.10, 1, step_gamma)
max_C, min_C = round(max(C_arr), 4), round(min(C_arr), 4)
max_gamma, min_gamma = round(max(gamma_arr), 4), round(min(gamma_arr), 4)

param_grid_rbf = {
         'C': C_arr,
         'gamma': gamma_arr,
         'kernel': ['rbf']
         }

print('   Done!\n>> Creating SVC...')
clf = SVC(kernel='rbf')
print(f""">> Starting grid search
   Tuning parameters:
                      C:  {min_C} <-> {max_C}, step: {step_C}
                  gamma:  {min_gamma} <-> {max_gamma}, step: {step_gamma}
                  """)
start = ml.stopwatch()
grid = GridSearchCV(clf, param_grid_rbf)
print('>> Refitting training set...')
grid.fit(X_train, y_train)
clf_score = cross_val_score(grid, X_test, y_test, scoring='accuracy', cv=3)
print('>> Calculating score for classifier')
train_acc = grid.score(X_train, y_train)
test_acc = grid.score(X_test, y_test)
#print("Accuracy: %f", acc)
print(f"Training accuracy: {train_acc}\nTest accuracy: {test_acc}\nValidation score: {clf_score}")
print(f"Best params: {grid.best_params_}\nBest score: {grid.best_score_}\n   Time spent: {ml.stopwatch(start)}")


