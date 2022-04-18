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
        self.Xe = self.extend_matrix(self.X, self.n)
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

    def extend_matrix(self, X, n):
        return np.c_[np.ones((n, 1)), X]

    def normalize_matrix(self, X):
        mom_height, dad_height = X[:, 0], X[:, 1]
        mom_mean, dad_mean = np.mean(mom_height), np.mean(dad_height)
        mom_subt, dad_subt = np.subtract(mom_height, mom_mean), np.subtract(dad_height, dad_mean)
        mom_std, dad_std = np.std(mom_height), np.std(dad_height)     
        mom_norm, dad_norm = np.divide(mom_subt, mom_std), np.divide(dad_subt, dad_std)
        Xn = np.concatenate((mom_norm.reshape(len(dad_height), 1), dad_norm.reshape(len(dad_height), 1)), axis=1)
        return Xn

    def normalize_extend(self, X):
        Xn = a.normalize_matrix(X)
        Xn_e = a.extend_matrix(Xn, len(Xn))
        return Xn_e

    def normalize_y(self, z, y):
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
        return B

    # Cost function
    def calc_cost(self, X, beta, y, n):
        j = np.dot(X, beta) - y
        J = (j.T.dot(j)) / n
        return J

        # X has to be extended
    def gradient_descent(self, Xe, y, N=10, a=0.0001, b=np.array([[0],[0],[0]])):
        b = [0,0,0]
        beta = self.calc_beta(self.Xe, self.y)
        for i in range(N):
            grad_vec = -(Xe.T.dot(y - Xe.dot(b)) / self.n)
            b = b - a*grad_vec
            cost = self.calc_cost(self.Xe, b, self.y, self.n)
            #print(cost)
            plt.scatter(cost, i, s=5)
            #print(b)
        return b

    def calc_height(self, beta, mom, dad):
        height = beta[0] + beta[1]*mom + beta[2]*dad
        return height


a = Exercise_A(path=path)
#a.plot_subplot(a.X[:,0], a.X[:,1], 1)
b = a.calc_beta(a.Xe, a.y)
#print(a.calc_cost(a.Xe, b, a.y, a.n))
grad = a.gradient_descent(a.Xe, a.y, 1000, 0.00023)
cost_grad = a.calc_cost(grad, b, a.y, a.n)
#a.plot_subplot(a.Xe[:,1], a.Xe[:,2], 1)
plt.ylim([1, 1100])
plt.show()

