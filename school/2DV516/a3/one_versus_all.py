from sklearn.model_selection import train_test_split, GridSearchCV
from matplotlib import pyplot as plt
from keras.datasets import mnist
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn import metrics
from sklearn import svm 
from time import time
import pandas as pd
import a3_lib as a3
import numpy as np

path = './data/mnistsub.csv'

# Optimized parameters
# RBF ==> C=0.1, gamma=1

# Linear: C | RBF: C, gamma | Poly: C, degree, gamma |
#   idx 0   |   idx 0, 1    |      idx 0, 1, 2       | 
C_range = np.logspace(-1, 10, 8)
gamma_range = np.logspace(-6, 3, 8)
param_grid = dict(gamma=gamma_range, C=C_range)

optimized_C = 0.01
optimized_gamma = 10

class OneVersusAll:

    def __init__(self, path, tune_params=False, test_size=0.15, train_size=0.20, verbose=True):
        print("\n||  STARTING SCRIPT...\n=====================\n")
        self.fig = plt.figure(figsize=(20,11))
        self.load_mnist_data(test=test_size, train=train_size, verbose=verbose)
        print("==> Creating classifier...")
        self.clf_rbf = svm.SVC(kernel='rbf', C=optimized_C, gamma=optimized_gamma)
        print("    Classifier CREATED!\n==> Training model...")
        self.clf_rbf.fit(self.x_train, self.y_train)
        print("    Model successfully trained!")

    def load_mnist_data(self, test, train, verbose=True):
        if verbose: print(f"==> Loading MNIST...\n    TRAINING: {train*100}%\n    TESTING: {test*100}%")
        start = time()
        X, Y = datasets.fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)
        X = X.reshape((X.shape[0], -1))

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=test, train_size=train, shuffle=False)
        print(f"    Training samples: {train*len(self.y_train)}\n    Test samples: {(test)*len(self.y_test)}")
        #scaler = StandardScaler()
        #self.x_train = scaler.fit_transform(self.x_train)
        #self.x_test = scaler.fit_transform(self.x_test)
        #numbers = datasets.load_digits()
        #n_samples = len(numbers.images)
        #data = numbers.images.reshape((n_samples, -1))
        #self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(data, numbers.target, test_size=test, shuffle=False)
        if verbose: print("==> Data SPLIT!\n    Beginning to reshape training and test data...")
        if verbose: print(f"    Time spent loading MNIST dataset: {round((time()-start), 2)} seconds")

    def evaluate_model(self, conf_matrix=False):
        print("==> Beginning to evaluate model...")
        pred_y = self.clf_rbf.predict(self.x_test)
        if conf_matrix: print(f"==> Confusion Matrix: \n{metrics.confusion_matrix(self.y_test, pred)}\n"+
                f"==> Classification report: \n{metrics.classification_report(self.y_test, pred_y)}\n")
        score = round((self.clf_rbf.score(self.x_test, self.y_test)), 6)
        error = round((1-score), 6)
        print(f"    FINAL RESULTS\n    Accuracy: {score*100}%\n    Error: {error*100}%\n\n----------------------------\n\n")

    def tune_hyperparams(self, X, Y):
        start = time()
        grid_search = GridSearchCV(svm.SVC(), param_grid=param_grid)
        grid_search.fit(X, Y)
        time_spent = time() - start
        if time_spent > 60: print(f"Grid search for RBF completed in {round((time_spent/60), 2)} minutes")
        else: print(f"Grid search for RBF completed in {time_spent} seconds")
        print(grid_search.best_params_)

one = OneVersusAll(path, test_size=0.02, train_size=0.04, tune_params=False)
#one.tune_hyperparams(one.x_train, one.y_train)
one.evaluate_model()

