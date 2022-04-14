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
        self.Xe = self.extend_x(self.X, self.n)
        self.beta = self.calc_beta(self.Xe)
        self.j = self.calc_j()  # keep as variable instead of recalculating each call

    def plot_dataset(self):
        plt.figure(figsize=(12, 8))
        plt.subplot(121)
        plt.scatter(self.X[:, 0], self.y, color="r", s=30, label='mom')
        plt.subplot(122)
        plt.scatter(self.X[:, 1], self.y, color="k", s=30, label='dad')

    def extend_x(self, X, n):
        return np.c_[np.ones((n, 1)), X]

    # Standard deviation --> compute each value - mean
    def feature_norm(self):
        mom_height = self.X[:, 0]
        dad_height = self.X[:, 1]
        mom_mean, dad_mean = np.mean(mom_height), np.mean(dad_height)
        mom_std, dad_std = np.std(mom_height), np.std(dad_height)     
        mom_subt, dad_subt = np.subtract(mom_height, mom_mean), np.subtract(dad_height, dad_mean)
        mom_norm, dad_norm = np.divide(mom_subt, mom_std), np.divide(dad_subt, dad_std)
        Xn = np.array([mom_norm, dad_norm]).reshape((214,2))
        Xn_e = self.extend_x(Xn, len(dad_height))
        print(f"\n|== Standard deviation ==|\nMom: {np.std(Xn_e[1])}\nDad: {np.std(Xn_e[2])}\n"
             +f"\n|== Mean ================|\nMom: {np.mean(Xn_e[1])}\nDad: {np.mean(Xn_e[2])}\n") 
        plt.scatter(Xn_e[:, 1], self.y, color="r", s=30, label='mom')
        plt.scatter(Xn_e[:, 2], self.y, color="b", s=30, label='dad')
        print(self.calc_beta(Xn_e))
        print(self.calc_height(Xn_e[:,1], dad)(Xn_e))


    # Normal equation
    def calc_beta(self, Xe):
        B = np.linalg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(self.y)
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
        print(f"Calculated height: {height}")
        return height

a = Exercise_A(path=path)
a.feature_norm()

plt.show()
