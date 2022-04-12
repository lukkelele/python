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
# --- Linear Regression | y = B1 + B2x 
# (y - yi)^2 = ((B1 + B2*x) - yi)^2  | the distance
# Cost function, J(B1, B2) | (1/n) * SUM((B1 + B2*x) - yi)^2  |  minimize the average distance 
# dy/dx = 0  ==> extreme values (max, min)
# Diffrentiate J(B1, B2) with B1 and B2 respectively and set to zero
# The normal equation is used to get the smallest distance (90 degrees from the plot)
# Vectorised version of linear regression (degree 1) | y = X_ext * B
# X_ext --> n x 2 matrix with an added column of 1's in row 0  
# y --> n x 1 vector 
# B --> 2 x 1 vector
# J(B) = (1\n)((X_ext*B - y)^T * (X_ext*B - y))
# Extending X: Xe = np.c_[np.ones((n,1)), X]
# Model: np.dot(Xe, B)
# Normal equation: B = np.linalg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(y)
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
# B^(j+1) = B^j - (2*lambda/n)*X^T * (X*B^j - y)

# Assumption: height = a + b*mom_height + c*dad_height
# Model: y = B1 + B2*x1 + B3*x2
# Vectorized: y = XB
# J(B) = (1/n)*(XB-y)^T * (XB-y)
# Exact solution: B = (X^T*X)^(-1) * (X^T*y)
# B^(j+1) = B^j - (2*lambda/n)*X^T * (XB^j - y)

class Exercise_A:

    def __init__(self, path):
        self.dataset = csv.open_csv_file(path)
        self.X = self.dataset[:, [1, 2]]
        self.y = self.dataset[:, 0]
        self.n = len(self.X)    # observations

    def plot_dataset(self):
        plt.figure(figsize=(12, 8))
        plt.subplot(121)
        plt.scatter(self.X[:, 0], self.y, color="r", s=30, label='mom')
        plt.subplot(122)
        plt.scatter(self.X[:, 1], self.y, color="k", s=30, label='dad')
        plt.show() 

    def extend_x(self):
        n = len(self.X)
        self.Xe = np.c_[np.ones((n, 1)), self.X]

    def calc_normal(self, y):
        B = np.linalg.inv(self.Xe.T.dot(self.Xe)).dot(self.Xe.T).dot(y)
        return B

    def calc_cost(self, y):
        B = self.calc_normal(y)
        j = np.dot(self.Xe, B) - y
        J = (j.T.dot(j)) / self.n
        print(f"Cost J: {J}\nlength_J: {len(J)}")
        return J

a = Exercise_A(path=path)
a.extend_x()
a.calc_cost(65)
a.plot_dataset()
