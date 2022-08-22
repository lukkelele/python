from sklearn.model_selection import cross_val_score
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

data = ml.open_csv_file('./data/bm.csv', header=-1)
X, y = data[:, :2], data[:, 2]

xmax = np.max(X[:,0]) 
print(xmax)
xmax = np.max(X[:,1]) 
print(xmax)
xx, yy = ml.meshgrid(X[:,0], X[:,1], offset=1, step_size=0.1)

training_percentage = 0.50
tot_samples = len(y)
n_s = round(training_percentage * tot_samples)
np.random.seed(7)
r = np.random.permutation(tot_samples)
X, y = X[r, :], y[r]
X_train, y_train = X[:n_s, :], y[:n_s]
X_test, y_test = X[n_s:, :], y[n_s:]
print(len(X_train))
print(len(X))

C, gamma = 20, 'auto'
SVM = SVC(C=C, gamma=gamma)
rbf_clf = SVM.fit(X_train, y_train)
support_vecs_idxs = rbf_clf.support_
supportVectors = X_train[support_vecs_idxs]

y_pred_train = rbf_clf.predict(X_train)
errors = np.sum(y_pred_train != y_train)
print(errors)
print(f"training error: {errors/n_s}")

pred_grid = rbf_clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape) # remove
plt.subplot(121)
plt.title('Input data with decision boundary')
ml.plot_decision_boundary(rbf_clf, xx, yy)
ml.plot_twofeature(X[:,0], X[:,1], y, colors=['g', 'darkgray'])

plt.subplot(122)
plt.title('Support vectors with decision boundary')
supportVectorPlot = plt.scatter(supportVectors[:,0], supportVectors[:,1], c='k', s=8, label='supportVectors')
ml.plot_decision_boundary(rbf_clf, xx, yy, colors='y', alpha=0.67, linewidths=4)

plt.show()

























