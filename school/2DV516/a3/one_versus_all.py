from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from keras.datasets import mnist
from sklearn import datasets
from sklearn import metrics
from sklearn import svm 
from time import time
from math import e
import pandas as pd
import a3_lib as a3
import numpy as np

path = './data/mnistsub.csv'

# Optimized parameters
# C = 837.67 
# Gamma = 3.16 * e^-6

# Linear: C | RBF: C, gamma | Poly: C, degree, gamma |
#   idx 0   |   idx 0, 1    |      idx 0, 1, 2       | 
C_range = np.logspace(-4, 11, 14)
gamma_range = np.logspace(-14, 3, 13)
param_grid = dict(gamma=gamma_range, C=C_range)

optimized_C = 800
optimized_gamma = 0.001 #3.16*e**-6

class OneVersusAll:

    def __init__(self, path, tune_params=False, test_size=0.10, train_size=0.30, verbose=True):
        print("\n==> Executing script...")
        self.start_time = time()
        if tune_params == False: print(f"==> Preconfigured parameters:\n"+
        f"    C={round(optimized_C, 3)}\n    gamma={round(optimized_gamma, 3)}")
        self.fig = plt.figure(figsize=(20,11))
        self.load_mnist_data(test=test_size, train=train_size, verbose=verbose)
        print("==> Creating classifier...")
        self.clf_rbf = svm.SVC(kernel='rbf', C=optimized_C, gamma=optimized_gamma)
        print("    Classifier CREATED!\n==> Training model...")
        self.clf_rbf.fit(self.x_train, self.y_train)
        print("    Model successfully trained!")
        self.evaluate_model()
        if time()-self.start_time< 60: 
            print("==================================\n"+
                 f" Total time: {round((time()-self.start_time),2)} seconds")
        else:
            print("==================================\n"+
                 f" Total time: {round((time()-self.start_time)/60,2)} minutes")
        print("==> Stopping script...\n")


    def load_mnist_data(self, test, train, verbose=True):
        if verbose: print(f"==> Loading MNIST...\n    TRAINING: {train*100}%\n    TESTING: {test*100}%")
        start = time()
        X, Y = datasets.fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)
        X = X.reshape((X.shape[0], -1))
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=test, train_size=train, shuffle=True)
        print(f"    Training samples: {train*len(self.y_train)}\n    Test samples: {(test)*len(self.y_test)}")
        scaler = StandardScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.fit_transform(self.x_test)
        if verbose: print("==> Data SPLIT!\n    Reshaping training and test data...")
        if verbose: print(f"    Time spent loading MNIST dataset: {round((time()-start), 2)} seconds")

    def evaluate_model(self, report=False):
        print("==> Evaluating model...")
        pred_y = self.clf_rbf.predict(self.x_test)
        if report: print(f"==> Confusion Matrix: \n{metrics.confusion_matrix(self.y_test, pred)}\n"+
                f"==> Classification report: \n{metrics.classification_report(self.y_test, pred_y)}\n")
        score = self.clf_rbf.score(self.x_test, self.y_test)
        error = 1-score
        print("    Model evaluated!")
        print(f"==> FINAL RESULTS\n    Accuracy: {round(score*100, 3)}%\n    Error: {round(error*100, 3)}%")

    def tune_hyperparams(self, X, Y):
        start = time()
        cv = StratifiedShuffleSplit(n_splits=5, train_size=0.2, test_size=0.1, random_state=42)
        grid_search = GridSearchCV(svm.SVC(), param_grid=param_grid, cv=cv)
        grid_search.fit(X, Y)
        time_spent = time() - start
        if time_spent > 60: print(f"Grid search for RBF completed in {round((time_spent/60), 2)} minutes")
        else: print(f"Grid search for RBF completed in {time_spent} seconds")
        print("BEST PARAMETERS ARE %s WITH A SCORE OF %0.2f" % (grid_search.best_params_, grid_search.best_score_))
        opt_C, opt_gamma = grid_search.best_params_['C'], grid_search.best_params_['gamma']

one = OneVersusAll(path, test_size=0.20, train_size=0.80)

