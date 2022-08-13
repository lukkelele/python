from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.model_selection import 
from sklearn.datasets import fetch_openml
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

print('Running...')
data = ml.open_csv_file('./data/mnistsub.csv', header=-1)
X, y = data[:,[0, 1]], data[:, 2]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80)
print('>> Data read')

#C_arr = np.arange(np.exp(-4), np.exp(5), np.exp(1))
C_arr = np.arange(0.1, 10, 0.1)
#gamma_arr = np.arange(1, (1/1000), 0.10)
gamma_arr = [1, 0.5, 0.1]
degree_arr = np.arange(1, 3, 1)
#degree_arr = [1, 2]
# preoptimized!
opt_C_lin = 0.40
opt_C_rbf = 0
opt_C_poly = 0

print('>> Creating grid parameters for the different kernels..')
param_grid_linear = {
         'C': C_arr,
         'kernel': ['linear']
         } 
param_grid_rbf = {
         'C': C_arr,
         'gamma': gamma_arr,
         'kernel': ['rbf']
         }
param_grid_poly = {
        'C': [0.1, 1, 10, 100],
        'gamma': gamma_arr,
        'degree': degree_arr,
        'kernel': ['poly']
        }
grid_params = [param_grid_linear, param_grid_rbf, param_grid_poly]
optimized_params_dict = [
        {'C': None, 'kernel': 'linear'},
        {'C': None, 'gamma': None, 'kernel': 'rbf'},
        {'C': None, 'gamma': None, 'degree': None, 'kernel': 'poly'},
        ]
optimized_params = []

print('>> Beginning grid search..')
tune = False
if tune == True:
    for k in range(0,3):
        start_time = ml.stopwatch()
        grid_param = grid_params[k]
        current_kernel = grid_param['kernel']
        print(f"\n   Current kernel: {current_kernel}")
        clf = SVC()
        grid_search = GridSearchCV(clf, grid_param)
        grid_search.fit(X_train, y_train)
        ml.stopwatch(start_time)
        #best_estimator = grid_search.best_estimator_  # TODO: To add instead of params(?)
        best_params = grid_search.best_params_
        optimized_params.append(best_params)
   
    C_linear, C_rbf, C_poly = optimized_params[0]['C'], optimized_params[1]['C'], optimized_params[2]['C']
    gamma_rbf, gamma_poly = optimized_params[1]['gamma'], optimized_params[2]['gamma']
    degree_poly = optimized_params[2]['degree']
else:
    C_linear, C_rbf, C_poly = 0.4, 0.7, 1
    gamma_rbf, gamma_poly = 0.10, 1
    degree_poly = 1


clf_lin = SVC(kernel='linear', C=C_linear).fit(X_train, y_train)
clf_rbf = SVC(kernel='rbf', C=C_rbf, gamma=gamma_rbf).fit(X_train, y_train) # pyright: ignore
clf_poly = SVC(kernel='poly', C=C_poly, gamma=gamma_poly, degree=degree_poly).fit(X_train, y_train) # pyright: ignore
clfs = [clf_lin, clf_rbf, clf_poly]
xx, yy = ml.meshgrid(X_train[:,0], X_train[:,1], offset=3)

clf_scores = []
# Produce plots
for i in range(3):
    plt.subplot(1,3,i+1)
    #plt.title(f"kernel: {optimized_params[i]['kernel']}")
    current_clf = clfs[i]
    y_mesh = current_clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plt.contourf(xx, yy, y_mesh, cmap='hot', alpha=0.35)
    #plt.scatter(X_train[:,0], X_train[:,1], s=12, c=y_train, edgecolors='k')   # training set
    plt.scatter(X_test[:,0], X_test[:,1], s=17, c=y_test, edgecolors='k')      # TEST DATA !!
    current_clf.sco 



print(f"""
--------------------------------
[RESULT] Optimized parameters  |
--------------------------------
    KERNELS
    -------
>>  Linear
          C: {C_linear}

>>  RBF
          C: {C_rbf}
      gamma: {gamma_rbf}

>>  Poly
          C: {C_poly}
      gamma: {gamma_poly}
     degree: {degree_poly}

------------------------------- 

""")



plt.show()
