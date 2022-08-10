from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MultipleLocator
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

def plot3x3_clfs(C, plot=True):
    plt.figure()
    cross_vals_scores = []
    errors = []
    for i in range(1, 10):
        if plot: plt.subplot(3,3,i)
        logReg = LogisticRegression(solver='lbfgs', C=C, tol=(1/np.e))
        # Create new X with the polynomial degree of i
        Xp = ml.polynomial(X1, X2, i, ones=False)
        # Train model classifier
        clf = logReg.fit(Xp, y)
        # Create mesh that has the same amount of features as Xp
        X_mesh = ml.polynomial(x1, x2, i, ones=False)
        # Predict and calculate training error
        y_pred = clf.predict(Xp)
        training_errors = np.sum(y!=y_pred)
        # Use the classifier on the mesh to get the decision boundary
        if plot:
            p = clf.predict(X_mesh)
            p_mesh = p.reshape(xx.shape)
            cmap_light = ListedColormap(['#d07e7e', '#c5c5c5', '#54d650']) # mesh plot
            plt.pcolormesh(xx, yy, p_mesh, cmap=cmap_light)
            # Plot the initial scatter plot on top of the decision boundary
            ml.log_plot_twofeature(X1, X2, y, training_errors)
        score = cross_val_score(clf, Xp, y, cv=5).mean()
        cross_vals_scores.append(score)
        errors.append(clf.score(Xp, y))
    plt.suptitle(f"C == {C}")
    return cross_vals_scores, errors

#plt.legend()

C_1, errors_C1 = plot3x3_clfs(1)
C_10K, errors_C10K= plot3x3_clfs(C)
avg_errors_C1, avg_errors_C10K = 0, 0
set_size = len(X)
bar_width = 0.25
degrees = np.arange(1, 10, 1)
plt.figure()
for d in degrees:
    error_C1 = (1-errors_C1[d-1]) * set_size
    error_C10K = (1-errors_C10K[d-1]) * set_size
    avg_errors_C1 += error_C1
    avg_errors_C10K += error_C10K
    plt.bar(d-(bar_width/2), error_C1, color='g', width=bar_width, edgecolor='k')
    plt.bar(d+(bar_width/2), error_C10K, width=bar_width, color='r', edgecolor='k')

plt.xlabel('Polynomial degree')
plt.legend(['Regularized', 'Unregularized'])
plt.xticks(np.arange(0,10,1)), plt.yticks(np.arange(0,75,5))

mean = len(degrees)
print(f""">>  Results:

  < Unregularized
    C = 1
    Score: {sum(errors_C1)/mean}
    Errors (avg): {avg_errors_C1/mean}
    ===========================================
  < Regularized
    C = 10K
    Score: {sum(errors_C10K)/mean}
    Errors (avg): {avg_errors_C10K/mean}
    
    Mean (len(degrees)) ==> {mean}

""")
plt.show()



