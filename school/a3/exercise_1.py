from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
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
C_arr = np.arange(0, 10, 0.9)
#gamma_arr = np.arange(1, (1/1000), 0.10)
gamma_arr = [1, 0.10]
#degree_arr = np.arange(1, 4, 1)
degree_arr = [1, 2]

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
for k in range(0,3):
    grid_param = grid_params[k]
    current_kernel = grid_param['kernel']
    print(f"   Current kernel: {current_kernel}")
    clf = SVC()
    grid_search = GridSearchCV(clf, grid_param)
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    print(f"   Best params: {best_params}")
    optimized_params.append(best_params)
   
C_linear, C_rbf, C_poly = optimized_params[0]['C'], optimized_params[1]['C'], optimized_params[2]['C']
gamma_rbf, gamma_poly = optimized_params[1]['gamma'], optimized_params[2]['gamma']
degree_poly = optimized_params[2]['degree']
print(f""">> C_linear, C_rbf and C_poly ==> {C_linear} , {C_rbf}, {C_poly}
   gamma_rbf and gamma_poly ==> {gamma_rbf}, {gamma_poly}
   degree_poly ==> {degree_poly}
""")

print(optimized_params)

