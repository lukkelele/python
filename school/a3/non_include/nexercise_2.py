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

np.set_printoptions(threshold=sys.maxsize)

# ONE VERSUS ALL MNIST
# RBF kernel, 95% test accuracy
# Create classifiers for each digit -> 9 classifers
# Compute score for each instance with all classifiers
# The classifier with the best score determines the class

# Tuned parameters ==> C: 71.96, gamma = 6.57*10^-7
grid_search = False
opt_C = 71.96
opt_gamma = 6.57*(10**-7)

print('>> Getting mnist_784 dataset...')
X, y = fetch_openml('mnist_784', version=1, data_home="~/Software/datasets/", return_X_y=True)
print('   Done!\n>> Splitting data...')
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.03, test_size=0.005)
X_train, X_test = X_train.to_numpy(), X_test.to_numpy()
train_size = len(X_train)
test_size = len(X_test)
#y_train, y_test = y_train.to_numpy(), y_test.to_numpy()
y_train, y_test = y_train.astype(np.int8), y_test.astype(np.int8)

print('>> Data read\n   Size of training set: %s instances\n   Size of test set: %s instances' % (train_size, test_size))
# Train 9 binary classifiers
# Create target for each class
print('>> Creating target data for each class...')
Y_train = []
for i in range(0, 10):
    print('   Classifier: %d' % i)
    Y_train.append(y_train == i)
print('   Done creating target data!\n>> Creating the classifiers for each class...')

#C_arr = np.logspace(-8, 15, 6)
#g_arr = np.logspace(-3, 6, 3)
params = { 'C': np.logspace(-5, 9, 17), 'gamma': np.logspace(-13, 3, 16), 'kernel': ['rbf']}

start = ml.stopwatch()
print('   Done!\n>> Creating SVC...')
#clf = SVC(kernel='rbf', C=100)
print('   SVC created!')
if grid_search == False:
    clf = SVC(kernel='rbf', C=71.69, gamma=opt_gamma) # pyright: ignore
else:
    svc = SVC()
    grid = GridSearchCV(svc, params)
    grid.fit(X_train, y_train)
    print(grid.best_params_)
    clf = SVC(C=grid.best_params_['C'], gamma=grid.best_params_['gamma'], kernel='rbf')
    print(f"""
   Best parameters: {grid.best_params_}
   Best estimator: {grid.best_estimator_}
""")
clf.fit(X_train, y_train)
clf_val_score_mean = cross_val_score(clf, X_test, y_test, scoring='accuracy', cv=2).mean()
test_acc = clf.score(X_test, y_test)
print(f"""
>> Performance: One-Versus-One
   Test accuracy: {test_acc}
   Validation score: {clf_val_score_mean}
   """)
# Create the classifiers with corresponding target data
# No loops used because it does not work properly with sklearn
kernel = 'rbf'
C = grid.best_params_['C']
gamma = grid.best_params_['gamma']
prob = True
clf0 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[0])
clf1 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[1])
clf2 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[2])
clf3 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[3])
clf4 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[4])
clf5 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[5])
clf6 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[6])
clf7 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[7])
clf8 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[8])
clf9 = SVC(kernel=kernel, C=C, gamma=gamma, probability=prob).fit(X_train, Y_train[9])
clfs = [clf0, clf1, clf2, clf3, clf4, clf5, clf6, clf7, clf8, clf9]

# Compute the scores for the test set using the binary classifers
Y_pred = np.zeros((len(X_test), 1))
for clf in clfs:
    # Predict_proba : [0] NO  | [1]  YES
    y_pred = clf.predict_proba(X_test)[:,1].reshape(-1,1) # choose positive prediction column
    Y_pred = np.append(Y_pred, y_pred, 1)
# delete first 0 column
Y_pred = np.delete(Y_pred, 0, 1)

YY_pred = []
for pred in Y_pred:
    pred_class = np.where(pred == np.max(pred))[0]
    YY_pred.append(pred_class)

YY_pred = np.array(YY_pred).ravel()
errors =  np.sum(YY_pred != y_test)
tot_acc = round(((test_size - errors) / test_size), 4)
print(f""">> Final results
        Accuracy: 
                  One-Versus-One  classifier: {test_acc}
                  One-Versus-All  classifier: {tot_acc}     (10 classifiers)
   Time spent: {ml.stopwatch(start)}
""")




