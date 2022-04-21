from matplotlib import pyplot as plt
import mlrlib as func
import numpy as np
import csv_parser

# 1975 - 2017
# f(X) = B0 + B1*X + B2*X**2 + ... + B*X**d

# The fourth degree is what gives the best fit in my opinion. MOTIVATE!
# Answer is NOT realistic.

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

    def calc_index(self, d, c):
        Xp = func.polynomial(self.X, d, self.n)
        b = func.calc_beta(Xp, self.y)
        if d == 1: index = b[0] + b[1]*c
        if d == 2: index = b[0] + b[1]*c + b[2]*c**2
        if d == 3: index = b[0] + b[1]*c + b[2]*c**2 + b[3]*c**3
        if d == 4: index = b[0] + b[1]*c + b[2]*c**2 + b[3]*c**3 + b[4]*c**4
        return index

    def polynomial(self):
        point_size = 2
        for i in range(1,5):
            plt.subplot(2,2,i)
            plt.xlabel('year')
            plt.ylabel('index')
            plt.scatter(np.add(self.X, 1975), self.y, s=4, color="g", alpha=0.75)
            Xp = func.polynomial(self.X, i, self.n)
            beta = func.calc_beta(Xp, self.y)
            XB = np.dot(Xp, beta)
            if i == 1: plt.scatter(np.add(self.X, 1975), XB, s=point_size, color="m")
            elif i == 2:
                for k in range(2):
                    plt.scatter(np.add(self.X, 1975), XB, s=point_size, color="b")
            elif i == 3:
                for k in range(3):
                    plt.scatter(np.add(self.X, 1975), XB, s=point_size, color="r")
            elif i == 4:
                for k in range(4):
                    plt.scatter(np.add(self.X, 1975), XB, s=point_size, color="k")
        plt.show()            

h = House(csv_path)
print(h.calc_index(4, 2.3))
print(h.calc_index(3, 2.3))
print(h.calc_index(2, 2.3))
print(h.calc_index(1, 2.3))

print(h.calc_index(4, 2.3))

h.polynomial()



