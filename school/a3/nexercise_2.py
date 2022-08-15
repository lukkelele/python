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
# Create classifiers for each digit -> 9 classifers
# Compute score for each instance with all classifiers
# The classifier with the best score determines the class


print('>> Getting mnist_784 dataset...')
X, y = fetch_openml('mnist_784', version=1, data_home="~/Software/datasets/", return_X_y=True)
print('   Done!\n>> Splitting data...')
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.12, test_size=0.03)
X_train, X_test = X_train, X_test
train_size = len(X_train)
test_size = len(X_test)
#y_train, y_test = y_train.to_numpy(), y_test.to_numpy()
y_train, y_test = y_train.astype(np.int8), y_test.astype(np.int8)
#y_train, y_test = y_train[:, 1], y_test[:, 1] 

print('>> Data read\n   Size of training set: %s instances\n   Size of test set: %s instances' % (train_size, test_size))
# Train 9 binary classifiers
# Create target for each class
print('>> Creating target data for each class...')
Y_train = []
for i in range(0, 10):
    print('   Classifier: %d' % i)
    Y_train.append(y_train == i)
print('   Done creating target data!\n>> Creating the classifiers for each class...')
# Create the classifiers with corresponding target data
# No loops used because it does not work properly with sklearn
kernel = 'rbf'
C = 1
clf0 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[0])
clf1 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[1])
clf2 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[2])
clf3 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[3])
clf4 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[4])
clf5 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[5])
clf6 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[6])
clf7 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[7])
clf8 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[8])
clf9 = SVC(kernel=kernel, C=C).fit(X_train, Y_train[9])
clfs = [clf0, clf1, clf2, clf3, clf4, clf5, clf6, clf7, clf8, clf9]

#C_arr = np.array([0.1])
#g_arr = np.array([0.01])
C_arr = np.logspace(-3, 13, 4)
g_arr = np.logspace(-3, 6, 3)
params = { 'C': C_arr, 'gamma': g_arr, 'kernel': ['rbf']}
start = ml.stopwatch()
print('   Done!\n>> Creating SVC...')
clf = SVC()
print('   SVC created\n>> Starting grid search...')
grid = GridSearchCV(clf, params)
grid.fit(X_train, y_train)
clf_val_score_mean = cross_val_score(grid, X_test, y_test, scoring='accuracy', cv=2).mean()
print('>> Calculating score for classifier')
test_acc = grid.score(X_test, y_test)
print(f"""
   Test accuracy: {test_acc}
   Validation score: {clf_val_score_mean}
   Best estimator: {grid.best_estimator_}")
   Time spent: {ml.stopwatch(start)}
""")
# Compute the scores for the test set using the binary classifers
clfs_scores = []
# TODO: Iterate each sample and decide proper class, (nested loop)
for clf in clfs:
    idx = clfs.index(clf)
    y_pred = clf.predict(X_test)
    errors = np.sum(y_pred != y_test)
    acc = round(((test_size - errors) / test_size), 4)
    clfs_scores.append(acc)
    print(f"   {idx}: {acc}")
clfs_scores = np.array(clfs_scores)
best_idx = np.where(clfs_scores == np.max(clfs_scores))
best_score = clfs_scores[best_idx]
print(f">> Best score: {best_score}, classifier {best_idx[0]}")

