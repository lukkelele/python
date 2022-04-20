from matplotlib import pyplot as plt
import mlrlib as func
import numpy as np
import csv_parser

# 1975 - 2017
# f(X) = B0 + B1*X + B2*X**2 + ... + B*X**d

csv_path = "./data/housing_price_index.csv"

class House:
    
    def __init__(self, path):
        self.fig = plt.figure(figsize=(12,9))
        self.path = path
        self.parse_csv_file()

    def parse_csv_file(self):
        dataset = csv_parser.open_house_file(self.path)
        self.X = dataset[:,0]
        self.y = dataset[:,1]
        self.n = len(self.X)

    def create_extended_matrixes(self):
        self.Xn = func.normalize_matrix(self.X, len(self.X), 1)
        self.Xe = func.extend_matrix(self.X, self.n)
        self.Xn_e = func.extend_matrix(self.Xn, self.n)

    def calc_cost(self, X, y, beta):
        j = np.dot(X, beta) - y
        J = (j.T.dot(j)) / self.n
        return J

    def gradient_descent(self, Xe, y, N, a):
        b = np.zeros((1,))
        for i in range(N):
            grad = -(Xe.T.dot(y - Xe.dot(b)) / self.n)
            b = b - a*grad
        return b

    def polynomial(self):
        point_size = 2
        for i in range(1,5):
            plt.subplot(2,2,i)
            plt.scatter(self.X, self.y, s=4, color="g", alpha=0.75)
            plt.xlim(0, 45)
            Xp = func.polynomial(self.X, i, self.n)
            print(Xp)
            beta = func.calc_beta(Xp, self.y)
            XB = np.dot(Xp, beta)
            if i == 1: plt.scatter(self.X, XB, s=point_size, color="m")
            elif i == 2:
                for k in range(2):
                    plt.scatter(self.X, XB, s=point_size, color="b")
            elif i == 3:
                for k in range(3):
                    plt.scatter(self.X, XB, s=point_size, color="r")
            elif i == 4:
                for k in range(4):
                    plt.scatter(self.X, XB, s=point_size, color="k")
            

h = House(csv_path)



h.polynomial()

plt.show()




