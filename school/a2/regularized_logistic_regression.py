from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import numpy as np
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)

data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,[0, 1]], data[:,2]
X1, X2 = X[:,0], X[:,1]
lim_step = 0.15
h = 0.004
iterations = 100
learning_rate = 0.25

x_min, x_max = X1.min() - lim_step, X1.max() + lim_step
y_min, y_max = X2.min() - lim_step, X2.max() + lim_step
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
x1, x2 = xx.ravel(), yy.ravel()
grid = np.c_[x1, x2]

C = 10000

for i in range(1, 10):
    plt.subplot(3,3,i)
    logReg = LogisticRegression(solver='lbfgs', C=C, tol=(1/np.e))
    # Create new X with the polynomial degree of i
    Xp = ml.polynomial(X1, X2, i, ones=False)
    # Train model classifier
    clf = logReg.fit(Xp, y)
    # Create mesh that has the same amount of features as Xp
    X_mesh = ml.polynomial(x1, x2, i, ones=False)
    # Predict and calculate training error
    y_pred = clf.predict(Xp)
    errors = np.sum(y!=y_pred)
    # Use the classifier on the mesh to get the decision boundary
    p = clf.predict(X_mesh)
    p_mesh = p.reshape(xx.shape)
    cmap_light = ListedColormap(['#d07e7e', '#c5c5c5', '#9aff97']) # mesh plot
    plt.pcolormesh(xx, yy, p_mesh, cmap=cmap_light)
    # Plot the initial scatter plot on top of the decision boundary
    ml.log_plot_twofeature(X1, X2, y, errors)


plt.show()
