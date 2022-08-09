from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)

"""
Quadratic model, polynomial degree 2
"""

# Read the already normalized data
data = ml.open_csv_file('./data/microchips.csv')
X, y = data[:,[0, 1]], data[:,2]
X1, X2 = X[:, 0], X[:, 1]

iterations = 100000
learning_rate = 0.135

# Polynomial of degree 2
ml.log_plot_cost_db(X1, X2, y, 2, iterations=iterations, learning_rate=learning_rate)
# Polynomial of degree 5
ml.log_plot_cost_db(X1, X2, y, 5, iterations=iterations, learning_rate=learning_rate)


plt.show()
