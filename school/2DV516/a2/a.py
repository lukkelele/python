# EXERCISE A

from matplotlib import pyplot as plt
import csv_parser as csv
import numpy as np
import math

# Column 1: girl height
# Column 2: mom height
# Column 3: dad height
path = "./data/girls_height.csv"


class Exercise_A:

    def __init__(self, path):
        self.dataset = csv.open_csv_file(path)
        self.X = self.dataset[:, [1, 2]]
        self.y = self.dataset[:, 0]
        self.n = len(self.X)    # observations
        self.Xe = self.extend_x()
        self.beta = self.calc_beta()
        self.j = self.calc_j()  # keep as variable instead of recalculating each call

    def plot_dataset(self):
        plt.figure(figsize=(12, 8))
        plt.subplot(121)
        plt.scatter(self.X[:, 0], self.y, color="r", s=30, label='mom')
        plt.subplot(122)
        plt.scatter(self.X[:, 1], self.y, color="k", s=30, label='dad')

    def extend_x(self):
        return np.c_[np.ones((self.n, 1)), self.X]

    # Standard deviation --> 
    def feature_norm(self):
        mom_height = self.X[:, 0]
        dad_height = self.X[:, 1]
        mom_mean, dad_mean = np.mean(mom_height), np.mean(dad_height)
         

    # Normal equation
    def calc_beta(self):
        B = np.linalg.inv(self.Xe.T.dot(self.Xe)).dot(self.Xe.T).dot(self.y)
        return B

    def calc_j(self):
        j = np.dot(self.Xe, self.beta) - self.y
        return j

    # Cost function
    def calc_cost(self):
        J = (self.j.T.dot(self.j)) / self.n
        print(f"Cost J: {J}\nlength_J: {len(J)}")
        return J

    def calc_height(self, mom, dad):
        height = self.beta[0] + self.beta[1]*mom + self.beta[2]*dad
        print(height)
        return height

a = Exercise_A(path=path)
a.calc_height(65, 70)
a.feature_norm()

