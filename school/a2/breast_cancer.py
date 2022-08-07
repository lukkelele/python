from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import mllib
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)
print(">> Running...\n")
"""
Total of 9 features and the 10th column contains binary labels of either 2 (0) or 4 (1)
"""

# Open and shuffle data
data = ml.open_csv_file('./data/breast_cancer.csv')
np.random.shuffle(data)
X, y = data[:,[0,1,2,3,4,5,6,7,8]], data[:,9]#.reshape(-1,1)
# Replace y values of 2 and 4 to 0 and 1 respectively
y = np.where(y == 2, 0, 1) 

# Divide data to training and testing sets
train_size = 0.80
train_idx = round(train_size * len(X))
X_train, X_test = X[:train_idx], X[train_idx:]
y_train, y_test = y[:train_idx], y[train_idx:]

# Normalize training data and train a linear logistic regression model
X_train = ml.normalize_matrix(X_train)
N, a = 1000, 0.01
beta = ml.log_gradient_descent(X_train, y_train, N=N, a=a, plotCost=True)

# Training errors and accuracy in training data
training_errors = ml.logreg_training_errors(X_train, y_train, beta)
correct = train_idx - training_errors
training_accuracy = round(correct / len(X), 4) * 100
print(f""">> TRAINING STATISTICS
   Errors: {training_errors}
   Accuracy: {training_accuracy}%
-------------------------------""")

#plt.show()
