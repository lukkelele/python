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

    def plot_subplot(self, x1, x2, i, c=['m', 'b']):
        j = 2
        I = int(f"{j}2{i}")
        plt.subplot(I)
        plt.scatter(x1, self.y, color=c[0], s=30, edgecolors='k', label='mom')
        I = int(f"{j}2{i+1}")
        plt.subplot(I)
        plt.scatter(x2, self.y, color=c[1], s=30, edgecolors='k', label='dad')

    def extend_x(self, X, n):
        return np.c_[np.ones((n, 1)), X]

    # Standard deviation --> compute each value - mean
    def feature_norm(self):
        mom_height, dad_height = self.X[:, 0], self.X[:, 1]
        mom_mean, dad_mean = np.mean(mom_height), np.mean(dad_height)
        mom_std, dad_std = np.std(mom_height), np.std(dad_height)     
        mom_subt, dad_subt = np.subtract(mom_height, mom_mean), np.subtract(dad_height, dad_mean)
        mom_norm, dad_norm = np.divide(mom_subt, mom_std), np.divide(dad_subt, dad_std)
        print(mom_norm/mom_std)
        Xn = np.array([mom_norm, dad_norm]).reshape((214,2))
        Xn_e = self.extend_x(Xn, len(dad_height))
        print(f"\n|== Mean ================|\nMom: {mom_mean}\nDad: {dad_mean}\n"
             +f"\n|== Height - mean =======|\nMom: {mom_subt}\nDad: {dad_subt}\n"
             +f"\n|== Standard deviation ==|\nMom: {mom_std}\nDad: {dad_std}\n"
             +f"\n|== Normalized Mean =====|\nMom: {np.mean(Xn_e[1])}\nDad: {np.mean(Xn_e[2])}\n") 
        self.plot_subplot(Xn_e[:,1], Xn_e[:,2], 3, ['r', 'g'])

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

    def calc_height(self, beta, mom, dad):
        height = beta[0] + beta[1]*mom + beta[2]*dad
        print(f"Calculated height: {height}")
        return height

a = Exercise_A(path=path)
plt.figure(figsize=(12,9))
a.plot_subplot(a.X[:,0], a.X[:,1], 1)
a.feature_norm()
plt.show()
