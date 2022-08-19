from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.neural_network import MLPClassifier
from matplotlib.ticker import MultipleLocator
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
from sklearn.svm import SVC
import numpy as np
import warnings
import time
import sys
import ml
import os

#np.set_printoptions(threshold=sys.maxsize)
if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore" # Also affect subprocesses


# Fashion MNIST
# Image classification

train_data, test_data = ml.open_csv_file('./data/fashion-mnist_train.csv'), \
                        ml.open_csv_file('./data/fashion-mnist_test.csv')
# Number of features used to slice data
f_idx = train_data.shape[1]
train_size = 0.80
test_size = 1.00
train_samples, test_samples = len(train_data), len(test_data)
new_train_size, new_test_size = round(train_size * train_samples), \
                                round(test_size * test_samples)
# Split the data, label on column 0
train_data, test_data = train_data[:new_train_size], test_data[:new_test_size]
X_train, X_test, y_train, y_test = train_data[:, 1:f_idx], test_data[:, 1:f_idx],\
                                   train_data[:,0],  test_data[:,0]
print(">> Dataset sizes\n   Training set: %d samples, %d%% of entire training set" \
                                              % (new_train_size, 100*train_size))
print("   Test set: %d samples, %d%% of entire test set" \
                        % (new_test_size, 100*test_size))
start_time = time.time()
# Train classifier
mlp_clf = MLPClassifier(max_iter=210)
print('>> Setting up gridsearch parameters')
params = {
    'hidden_layer_sizes': [(50,50,50,50,50), (100,100,100), (100,100), (100,50,100), (50,100), (100,)],
    'activation': ['relu'],
    'solver': ['adam'],
    'alpha': np.logspace(-5, -20, 16),
    'learning_rate': ['constant', 'adaptive'],
}
# n_jobs=-1 --> utilize CPU max, cv=2 --> 2 folds
print('>> Beginning grid search...')
clf = GridSearchCV(mlp_clf, params, n_jobs=4, cv=2) 
print('>> Training model...')
clf.fit(X_train, y_train)

mean_test_score = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
print('>> Calculating results')
for mean, std, params in zip(mean_test_score, stds, clf.cv_results_['params']):
    # std * 2 -> standard deviation that include 95% of the data under normal distribution
    print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))

print(f"\n>> Best parameters: {clf.best_params_}\n   Best estimator: {clf.best_estimator_}")
print(f"  Best test score: {np.max(mean_test_score)}")
end_time = time.time()
print(f">> Time spent testing hyperparameters: {end_time - start_time}")



