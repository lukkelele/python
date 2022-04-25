from matplotlib import pyplot as plt
from lib import csv_parser
import mlrlib as func
import numpy as np

csv_path = "./data/microchips.csv"

# Quadratic model XB = B0 + B1X1 + B2X2 + B3(X1)^2 + B4X1X2 + B5(X2)^2

class Microships:
    
    def __init__(self, path):
        self.parse_csv_file(path)
        self.fig = plt.figure(figsize=(12,10))
        self.b = func.calc_beta(self.Xe, self.y)

    def parse_csv_file(self, path):
        dataset = csv_parser.open_microships_file(path)
        self.n = len(dataset)
        self.X = dataset[:,[0,1]]
        self.y = dataset[:,2]
        self.create_extended_matrixes()
        self.XN = self.create_polynomial_X()

    def create_polynomial_X(self):
        Xn1 = self.Xn[:,0].reshape(self.n, 1)
        Xn2 = self.Xn[:,1].reshape(self.n, 1)
        Xn12 = np.concatenate((Xn1, Xn2), axis=1)
        Xn11 = np.square(Xn1)
        Xn22 = np.square(Xn2)
        Xn = np.concatenate((self.Xn_e, Xn11), axis=1)
        Xn = np.concatenate((Xn,Xn12), axis=1)
        Xn = np.concatenate((Xn,Xn22), axis=1)
        return Xn

    def create_extended_matrixes(self):
        matrixes = func.create_extended_matrixes(self.X)
        self.Xn, self.Xe, self.Xn_e = matrixes[0], matrixes[1], matrixes[2]
    
    # TODO: FIX THE DECISION BOUNDARY
    def model(self, X, y):
        x1, x2 = X[:,1], X[:,2]
        plt.subplot(1,2,1)
        b = func.log_gradient_descent(X, y, N=10, a=0.5, verbose=False, plot=True)
        c = b[0] + b[1]*x1 + b[2]*x2 + b[3]*x1**2 + b[4]*x1*x2 +b[5]*x2**2
        min_x1, max_x1 = np.min(x1), np.max(x1)
        XB = np.dot(X, b)
        xx = np.arange(min_x1, max_x1, 0.1)
        x = -(b[0] + b[1]*xx + b[2]*xx + b[3]*xx + b[4]*xx) / b[5]
        plt.subplot(1,2,2)
        plt.ylim(np.min(x1), np.max(x1))
        plt.plot(xx, x)
        self.plot_data()
        #print(f"Model: {c}")

    def map_features(self, Xe, d):
        X1, X2 = Xe[:,1], Xe[:,2]
        X = func.map_features(X1, X2, d)
        return X

    def plot_data(self):
        plt.xlabel('points')
        plt.ylabel('points')
        green_flag = False
        red_flag = False
        yy = self.y.reshape((len(self.y),1))
        X = np.concatenate((self.X, yy), axis=1)
        for a in X:
            x0 = a[0]
            x1 = a[1]
            y = a[2]
            if y == 1: # current legend implementation is not memory efficient
                plt.scatter(x0, x1, s=40, color='g', marker="v", label='1' if green_flag==False else "", edgecolors='k')
                green_flag = True
            else:
                plt.scatter(x0, x1, s=40, color='r', marker="x", label='0' if red_flag==False else "")
                red_flag = True
        plt.legend()



m = Microships(csv_path)
#f = plt.figure(figsize=(12,9))

X = func.map_features(m.Xe[:,1], m.Xe[:,2], 2)
beta = func.calc_beta(X, m.y)
#func.desicion_boundary(X[:,1], X[:,2], 2, beta)
m.model(m.XN, m.y)
#m.plot_data()
#m.plot_data()
plt.show()



