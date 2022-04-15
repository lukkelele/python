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
        self.beta = self.calc_beta(self.Xe, self.y)
        self.fig = plt.figure(figsize=(12,9))

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
    def feature_norm(self, X):
        mom_height, dad_height = X[:, 0], X[:, 1]
        mom_mean, dad_mean = np.mean(mom_height), np.mean(dad_height)
        mom_subt, dad_subt = np.subtract(mom_height, mom_mean), np.subtract(dad_height, dad_mean)
        mom_std, dad_std = np.std(mom_height), np.std(dad_height)     
        mom_norm, dad_norm = np.divide(mom_subt, mom_std), np.divide(dad_subt, dad_std)
        Xn = np.concatenate((mom_norm.reshape(len(dad_height), 1), dad_norm.reshape(len(dad_height), 1)), axis=1)
        Xn_e = self.extend_x(Xn, len(dad_height))   # len(dad_height) == len(mom_height) == 214
        print(f"\n|== Mean ================|\nMom: {mom_mean}\nDad: {dad_mean}\n"
             +f"\n|== Standard deviation ==|\nMom: {mom_std}\nDad: {dad_std}\n"
             +f"\n|== Normalized Mean =====|\nMom: {np.mean(Xn_e[:,1])}\nDad: {np.mean(Xn_e[:,2])}\n" 
             +f"\n|== Norm standard dev ===|\nMom: {np.std(Xn_e[:,1])}\nDad: {np.std(Xn_e[:,2])}\n")
        self.plot_subplot(Xn_e[:,1], Xn_e[:,2], 3, ['r', 'g']) # x0, x1, subplot index, colors for x0 and x1
        return Xn_e

    def feature_norm_y(self, z, y):
        y_mean = np.mean(y)
        y_subt = np.subtract(y, y_mean)
        y_std = np.std(y)
        y_norm = np.divide(y_subt, y_std)
        n = (z-y_mean)/y_std
        return n

    def normalize_x(self, x, X):
        x_mean = np.mean(X)
        x_std = np.std(X)
        x_norm = (x - x_mean) / x_std
        return x_norm

    # Normal equation
    def calc_beta(self, Xe, y):
        B = np.linalg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(y)
        print(f"BETA: {B}\n")
        return B

    def calc_j(self, X, beta):
        j = np.dot(X, beta) - self.y
        return j

    # Cost function
    def calc_cost(self, X, beta):
        j = self.calc_j(X, beta)
        J = (j.T.dot(j)) / self.n
        return J

    def calc_height(self, beta, mom, dad):
        height = beta[0] + beta[1]*mom + beta[2]*dad
        return height


a = Exercise_A(path=path)
a.plot_subplot(a.X[:,0], a.X[:,1], 1)
Xn_e = a.feature_norm(a.X)
B = a.calc_beta(Xn_e, a.y)
mom = a.normalize_x(65, a.X[:,0])
dad = a.normalize_x(70, a.X[:,1])
print(a.calc_height(B, mom, dad))

#plt.show()

