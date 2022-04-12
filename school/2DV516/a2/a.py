# EXERCISE A

from matplotlib import pyplot as plt
import csv_parser as csv
import numpy as np
import math

# Column 1: girl height
# Column 2: mom height
# Column 3: dad height
path = "./data/girls_height.csv"

# ==================================================================
# --- Linear Regression | y = a + bx 
# (y - yi)^2 = ((a + bx) - yi)^2  | the distance
# Cost function, J(a, b) | (1/n) * SUM((a+bx) - yi)^2  |  minimize the average distance 
# dy/dx = 0  ==> extreme values (max, min)
# Diffrentiate J(a, b) with a and b respectively and set to zero
# The normal equation is used to get the smallest distance (90 degrees from the plot)
# Vectorised version of linear regression (degree 1) | y = X_ext * B
# X_ext --> n x 2 matrix with an added column of 1's in row 0  
# y --> n x 1 vector 
# B --> 2 x 1 vector
# J(B) = (1\n)((X_ext*B - y)^T * (X_ext*B - y))
# Extending X: Xe = np.c_[np.ones((n,1)), X]
# Model: np.dot(Xe, B)
# Normal equation: B = np.linialg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(y)
# Cost function: J = (j.T.dot(j))/n  where j = np.dot(Xe, beta)-y
# ==================================================================
# --- Gradient Descent
# Select a point x0 | Move to x1 = x0 - lambda(df/dx)*x0 | lambda is called the learning rate
# Repeat the process until minimum point is reached or limit of iterations has been reached | df/dx > 0
# Will in general find a local minimum
# Very good for convex problems | Less effective for realistic cases with multiple local minimums
# Selecting learning rate is pretty much trial and error
# The cost function J(B1, B2) is an upward facing parabolic "bowl", i.e convex
# Therefore there will be a unique min(B1_min, B2_min) and it is possible to use any point as a starting point
# Initial steps: iterations N = 10, a = 0.00001, B0 = (0, 0)  | then plot the cost function
# a = 2*lambda / n  | Plot J(B) vs N is a good way to see if J(B) has stabilised

class Exercise_A:

    def __init__(self, path):
        self.dataset = csv.open_csv_file(path)

    def plot_dataset(self):
        #f = plt.figure(figsize=(12,9))
        ax = plt.subplot(2,2,1)
        ax.set_title("Dataset")
        ax.set_xlabel('mom height')
        ax.set_ylabel('dad height')
        y = self.dataset[:, 0]
        #x0 = self.dataset[:, 1]
        #x1 = self.dataset[:, 2]
        X = self.dataset[:, [1,2]]
        #x0_min, x1_min = np.min(x0), np.min(x1)
        #x0_max, x1_max = np.max(x0), np.max(x1)
        plt.plot(X, y, c="b")
        plt.show()
        


a = Exercise_A(path=path)
a.plot_dataset()
