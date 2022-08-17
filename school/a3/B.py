from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.datasets import fetch_openml, load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import numpy as np
import sys
import ml

# Perceptron XOR gate

# Input data 
X = np.array([[0,0], [0,1], [1,0], [1,1]])
# Target output to mimic a XOR gate
y = np.array([0, 1, 1, 0])

clf = MLPClassifier()
clf.fit(X, y)

print(clf.predict([ [0, 0] ] ))
print(clf.predict([ [0, 1] ] ))
print(clf.predict([ [1, 0] ] ))
print(clf.predict([ [1, 1] ] ))
print(clf.get_params())
