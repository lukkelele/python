from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
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
print('\n>> Reading data...')
data = ml.open_csv_file('./data/bm.csv', header=-1)
X, y = data[:, :2], data[:, 2]
# Determine percentage of data to use for training
training_percentage = 0.50
tot_samples = len(y)
# Number of samples
n_s = round(training_percentage * tot_samples)
np.random.seed(7)
r = np.random.permutation(tot_samples)
# Shuffle data and split it in to training and test sets
print('>> Shuffling and splitting datasets accordingly')
X, y = X[r, :], y[r]
X_train, y_train, X_test, y_test = X[:n_s, :], y[:n_s], X[n_s:, :], y[n_s:]
n_trees = 100

# 100 bootstrapped training sets
print(f'>> Bootstrapping training data in to {n_trees} sets')
X_bootstrap_100 = ml.bootstrap_data(X_train, n_trees)

# Create and train the decision trees
print('>> Creating decision trees and training them on respective training set')
test_samples = len(X_test)
Y_pred = []
tree_scores = []
for i in range(n_trees):
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = clf.score(X_test, y_test)
    Y_pred.append(y_pred)
    errors = np.sum(y_pred != y_test)
    tree_scores.append([acc, errors])

Y_pred = np.array(Y_pred)
tree_scores = np.array(tree_scores)
avg_acc_tree = round(tree_scores[:,0].mean(), 10)
avg_error_tree = round(tree_scores[:,1].mean(), 6)
avg_error_rate_tree = round(1-avg_acc_tree, 6)
# Best scoring tree
best_tree_idx = np.where(tree_scores[:,0] == np.max(tree_scores[:,0]))[0][0]
best_tree_acc = tree_scores[:,0][best_tree_idx]
# Classification problem, sum columns for predicted y, if sum(y(col)) > (n_trees/2)
# Vote YES (1), else NO (0)
YY_pred = []
for i in range(test_samples):
    group_sum = np.sum(Y_pred[:, i]) / 2
    if group_sum >= 50:
        YY_pred.append(1)
    else:
        YY_pred.append(0)

YY_pred = np.array(YY_pred)
errors = np.sum(YY_pred != y_test)
error_rate = round(errors/test_samples, 6)
ensemble_acc = 1 - (errors/test_samples)

if ensemble_acc > avg_error_rate_tree:
    msg = f"Ensemble model performed best with an accuracy of {ensemble_acc}!\n\t{ensemble_acc} > {best_tree_acc}"
else:
    msg = f"Average individual accuracy performed better than the ensemble model!\n\t{ensemble_acc} < {avg_acc_tree}"

print(f"""
>> Results:

   [INDIVIDUAL TREES]

        Avg error: {avg_error_tree}
        Avg accuracy: {avg_acc_tree}
        Avg error rate: {avg_error_rate_tree}
        
        > BEST TREE:
        Number: {best_tree_idx + 1}     ( index {best_tree_idx} )
        Accuracy: {best_tree_acc}

   ------------------------------------------------------------------------------
   [ENSEMBLE]

        Error rate: {error_rate}  ( {errors} errors / {test_samples} samples )
        Accuracy: {ensemble_acc}
   ------------------------------------------------------------------------------
   [WINNER]

        {msg}
""")

# TODO: Plot data

