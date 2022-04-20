from matplotlib import pyplot as plt
import mlrlib as func
import numpy as np
import csv_parser

# 1975 - 2017
# f(X) = B0 + B1*X + B2*X**2 + ... + B*X**d

csv_path = "./data/housing_price_index.csv"

class House:
    
    def __init__(self, path):
        self.path = path
        self.parse_csv_file()

    def parse_csv_file(self):
        dataset = csv_parser.open_house_file(self.path)
        self.X = dataset[:,0]
        self.y = dataset[:,1]
        self.n = len(self.X)

    def create_extended_matrixes(self):
        self.Xn = self.normalize_X(self.X, 6)
        self.Xe = self.extend_matrix(self.X, self.n)
        self.Xn_e = self.extend_matrix(self.Xn, self.n)

    def normalize_X(self, X, r):
        Xn = np.zeros((18, 6))
        for i in range(r):
            Xn[:,i] = func.normalize_column(X, i)
        return Xn

    def normalize_column(self, X, col):
        norm_col = func.normalize_column(X, col)
        return norm_col

    def extend_matrix(self, X, n):
        return np.c_[np.ones((n, 1)), X]

    def normalize_val(self, X, col, val):
        column = X[:,col]
        mean = np.mean(column) 
        std = np.std(column) 
        norm_val = (val-mean)/std
        return norm_val

    def normalize_features(self, features):
        norm_vals = []
        for i in range(6):
            norm_vals.append(self.normalize_val(self.X, i, features[i]))
        return norm_vals

    def calc_cost(self, Xe, y, beta):
        j = np.dot(Xe, beta) - y
        J = (j.T.dot(j)) / self.n
        return J

    def gradient_descent(self, Xe, y, N, a):
        b = np.zeros((7,))
        for i in range(N):
            grad = -(Xe.T.dot(y - Xe.dot(b)) / self.n)
            b = b - a*grad
            cost = self.calc_cost(Xe, y, b)
            if i < 5: pass
           # plt.scatter(i, cost, s=3, color="k")
        return b


h = House(csv_path)

func.plot_features(h.X, h.y, 1)
plt.show()




