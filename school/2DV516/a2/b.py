from matplotlib import pyplot as plt
from lib import mlrlib as func
from lib import csv_parser
import numpy as np

# Parametric classification method

csv_path = "./data/admission.csv"

class B:
    
    def __init__(self, path):
        self.fig = plt.figure(figsize=(12,9))
        self.path = path
        self.parse_csv_file()

    def parse_csv_file(self):
        self.dataset = csv_parser.open_admission_file(self.path)
        self.n = len(self.dataset)
        self.X = self.dataset[:,[0,1]]
        self.y = self.dataset[:,2]
        self.x0, self.x1 = self.dataset[:,0], self.dataset[:,1]
        self.create_extended_matrixes()

    def create_extended_matrixes(self):
        self.Xn = func.normalize_matrix(self.X, len(self.X), 2)
        print(self.Xn)
        self.Xe = func.extend_matrix(self.X, self.n)
        self.Xn_e = func.extend_matrix(self.Xn, self.n)

    def gradient_descent(self, Xe, y, N, a):
        f = func.gradient_descent(Xe, y, N, a)
        return f

    def plot_data(self):
        plt.xlabel('points')
        plt.ylabel('points')
        admitted_flag = False
        not_admitted_flag = False
        y = self.y.reshape((100,1))
        X = np.concatenate((self.Xn, y), axis=1)
        print(X)
        for a in X:
            x0 = a[0]
            x1 = a[1]
            y = a[2]
            if y == 1: # current legend implementation is not memory efficient
                plt.scatter(x0, x1, s=40, color='g', marker="v", label='Admitted' if admitted_flag==False else "", edgecolors='k')
                admitted_flag = True
            else:
                plt.scatter(x0, x1, s=40, color='r', marker="x", label='not Admitted' if not_admitted_flag==False else "")
                not_admitted_flag = True
        plt.legend()



b = B(csv_path)
b.plot_data()

plt.show()
