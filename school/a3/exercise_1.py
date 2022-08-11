from sklearn.model_selection import cross_val_score, GridSearchCV
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

data = ml.open_csv_file('./data/mnistsub.csv', header=-1)
X, y = data[:,[0, 1]], data[:, 2]


