from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.datasets import fetch_openml, load_digits
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import csv
import sys
import ml

#np.set_printoptions(threshold=sys.maxsize)

filename_training = './subset_training.csv'
filename_testing = './subset_testing.csv'

tp = 0.25   # % of train set size for test set
X, y = fetch_openml('mnist_784', version=1, data_home="~/Software/datasets/", return_X_y=True)
#y = y.reshape(-1, 1)
#X, y = mnist['data'], mnist['target']   # pyright: ignore
mnist = load_digits()
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.10)
train_size = len(X_train)
test_size = round(tp * train_size)
X_test, y_test = X_test[:test_size], y_test[:test_size]
print(y_test)

header = X.head()
#Xy = np.append(X, y, 1)
Xy = np.c_[X, y]
Xy_train = Xy[:train_size]
Xy_test = Xy[train_size:]

Xy_train = pd.DataFrame(Xy_train)
Xy_test = pd.DataFrame(Xy_test)

Xy_train_export = Xy_train.to_csv(filename_training, encoding='utf-8')
Xy_test_export = Xy_test.to_csv(filename_testing, encoding='utf-8')
#X_train_export = X_train.to_csv(filename_training, encoding='utf-8')
#X_test_export = X_test.to_csv(filename_testing, encoding='utf-8')
#X, y = [X_train, X_test], [y_train, y_test]



