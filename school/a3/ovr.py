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

np.set_printoptions(threshold=sys.maxsize)

# Load digits 8x8 pixels
# Features 0-16, 8 x 8 pixel combinations results in dimension 64

#X, y = fetch_openml('mnist_784', version=1, data_home="~/Software/datasets/", return_X_y=True)
mnist = load_digits()
X, y = mnist['data'], mnist['target']   # pyright: ignore
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.40)
train_size = len(X_train)
X_test, y_test = X_test[:train_size], y_test[:train_size]
print(">> Features: %d" % (len(X[0])/4))
print('>> Data read\n   Size of training set: %s' % train_size)
# One versus all classifier, train classifer for each class, 1-10
y_train_1 = y_train == 1
y_train_2 = y_train == 2
y_train_3 = y_train == 3
y_train_4 = y_train == 4
y_train_5 = y_train == 5
y_train_6 = y_train == 6
y_train_7 = y_train == 7
y_train_8 = y_train == 8
y_train_9 = y_train == 9
y_train_ = [y_train_1, y_train_2, y_train_3, y_train_4,
            y_train_5, y_train_6, y_train_7, y_train_8,
            y_train_9]

# Train classifiers
kernel = 'rbf'
gamma = 1
C = 1
clf1 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_1)
clf2 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_2)
clf3 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_3)
clf4 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_4)
clf5 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_5)
clf6 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_6)
clf7 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_7)
clf8 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_8)
clf9 = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train_9)
clfs = [clf1, clf2, clf3, clf4, clf5, clf6, clf7, clf8, clf9]

# Measure performance for clf1
clf1_cross_results = []

# How good each classifier is at classifying its own class
for clf in clfs:
    i = clfs.index(clf)
    y_ = y_train_[i]
    #clf_ = clf.fit(X_train, y_)
    cross_validation_score = cross_val_score(clf, X_train, y_, cv=3, scoring='accuracy').mean()
    clf1_cross_results.append(cross_validation_score)
    print(f"{i}  :  {cross_validation_score}")

m = len(X_train)
for clf in clfs:
    i = clfs.index(clf)
    print(f">> Classifier {i+1} \n")    
    for y_train in y_train_:
        y_pred = clf.predict(X_train)
        acc = sum(y_train == y_pred) / m
        print(f"  {acc}")
    print('\n\n')

