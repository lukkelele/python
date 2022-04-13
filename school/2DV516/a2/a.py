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
# a = 22.779813084118473

class Exercise_A:

    def __init__(self, path):
        self.dataset = csv.open_csv_file(path)
        self.X = self.dataset[:, [1, 2]]
        self.y = self.dataset[:, 0]
        self.n = len(self.X)    # observations
        self.Xe = self.extend_x()
        self.a = 22.779813084118473

    def calc_height(self, mom, dad):
        B_mom = self.calc_beta(mom)
        B_dad = self.calc_beta(dad)
        sum_dad =(sum(sum(B_dad*dad))/self.n)
        sum_mom = (sum(sum(B_mom*mom))/self.n)
        print(f"sum_dad: {sum_dad}\nsum_mom: {sum_mom}\ngirl height: {self.a+sum_dad+sum_mom}")
        return self.a + sum_dad + sum_mom   # predicted height
        

    def plot_dataset(self):
        plt.figure(figsize=(12, 8))
        plt.subplot(121)
        plt.scatter(self.X[:, 0], self.y, color="r", s=30, label='mom')
        plt.scatter(65, self.calc_height(65,70), color="b", s=40, marker="v")
        plt.subplot(122)
        plt.scatter(self.X[:, 1], self.y, color="k", s=30, label='dad')
        plt.scatter(70, self.calc_height(65,70), color="b", s=40, marker="x")
        plt.show() 

    def extend_x(self):
        return np.c_[np.ones((self.n, 1)), self.X]

    # Normal equation
    def calc_beta(self, z):
        B = np.linalg.inv(self.Xe.T.dot(self.Xe)).dot(self.Xe.T).dot(z)
        return B

    # Cost function
    def calc_cost(self, y):
        B = self.calc_beta(y)
        j = np.dot(self.Xe, B) - y
        J = (j.T.dot(j)) / self.n
        print(f"Cost J: {J}\nlength_J: {len(J)}")
        return J


a = Exercise_A(path=path)
mom = 65
dad = 70
a.plot_dataset()


