from sklearn.model_selection import train_test_split, GridSearchCV
from matplotlib import pyplot as plt
from keras.datasets import mnist
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
param_rbf  = {'C': [0.1, 1, 10, 100, 1000, 10000],
             'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
             'kernel': ['rbf']      }
optimized_C = 0.1
optimized_gamma = 1

class OneVersusAll:

    def __init__(self, path, tune_params=False):
        self.fig = plt.figure(figsize=(20,11))
        self.load_mnist_data(train=0.40, test=0.20, verbose=True)
        if tune_params == False: self.tune_hyperparams(self.x_train, self.y_train) # only prints best, does not set them
        print("==> Creating classifier...")
        self.clf_rbf = svm.SVC(kernel='rbf', C=optimized_C, gamma=optimized_gamma)
        print("==> Classifier CREATED!\n==> Training model...")
        self.clf_rbf.fit(self.x_train, self.y_train)
        print("==> Model successfully trained!")

    def load_mnist_data(self, train=0.10, test=0.05, verbose=False):
        if verbose: print(f"==> Loading MNIST...\n  TRAINING: {train*100}%\n  TESTING: {test*100}%")
        start = time()
        (X, y), (xx_test, yy_test) = mnist.load_data()
        x_train, x_test, self.y_train, self.y_test = train_test_split(X, y, train_size=train, test_size=test)
        if verbose: print("==> Data SPLIT!\n   Beginning to reshape training and test data...")
        n, nx, ny = x_train.shape
        self.x_train = x_train.reshape((n,nx*ny))
        n, nx, ny = x_test.shape
        self.x_test = x_test.reshape((n, nx*ny))
        if verbose: print(f"Time spent loading MNIST dataset ==> {round((time()-start), 2)} seconds")

    def evaluate_model(self):
        print("==> Beginning to evaluate model...")
        pred_y = self.clf_rbf.predict(self.x_test)
        #actual = self.y_test
        #conf_matrix = metrics.confusion_matrix(actual, pred)
        #clf_report = metrics.classification_report(actual, pred)
        score = round((self.clf_rbf.score(self.y_test, pred_y)), 3)
        error = round((1-score), 3)
        print(f"Accuracy: {score*100}%\nError: {error*100}%")

    def tune_hyperparams(self, X, Y):
        start = time()
        grid_search = GridSearchCV(svm.SVC(), param_rbf, refit=True)
        grid_search.fit(X, Y)
        time_spent = time() - start
        if time_spent > 60: print(f"Grid search for RBF completed in {round((time_spent/60), 2)} minutes")
        else: print(f"Grid search for RBF completed in {time_spent} seconds")
        print(grid_search.best_params_)

print("\n==> Starting...")
one = OneVersusAll(path)
one.evaluate_model()


