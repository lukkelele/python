# EXERCISE A

from matplotlib import pyplot as plt
import csv_parser as csv
import numpy as np
import math

# Column 1: girl height
# Column 2: mom height
# Column 3: dad height
path = "./data/girls_height.csv"

# Linear Regression | y = a + bx 
# (y - yi)^2 = ((a + bx) - yi)^2  | the distance
# Cost function, J(a, b) | (1/n) * SUM((a+bx) - yi)^2  |  minimize the average distance 
# dy/dx = 0  ==> extreme values (max, min)
# Diffrentiate J(a, b) with a and b respectively and set to zero
# The normal equation is used to get the smallest distance (90 degrees from the plot)
# Vectorised version of linear regression (degree 1) | y = X_ext * B
# X_ext --> n x 2 matrix with an added column of 1's in row 0  
# y --> n x 1 vector 
# B --> 2 x 1 vector

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
