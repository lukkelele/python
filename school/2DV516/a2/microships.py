from matplotlib import pyplot as plt
from lib import csv_parser
import mlrlib as func
import numpy as np

csv_path = "./data/microchips.csv"

# Quadratic model XB = B0 + B1X1 + B2X2 + B3(X1)^2 + B4X1X2 + B5(X2)^2

class Microships:
    
    def __init__(self, path):
        self.parse_csv_file(path)
        self.b = func.calc_beta(self.Xe, self.y)

    def parse_csv_file(self, path):
        dataset = csv_parser.open_microships_file(path)
        self.n = len(dataset)
        self.X = dataset[:,[0,1]]
        self.y = dataset[:,2]
        self.create_extended_matrixes()
        Xn1 = self.Xn[:,0].reshape(self.n, 1)
        Xn2 = self.Xn[:,1].reshape(self.n, 1)
        Xn12 = np.concatenate((Xn1, Xn2), axis=1)
        Xn11 = np.square(Xn1)
        Xn22 = np.square(Xn2)
        Xn = np.concatenate((self.Xn_e, Xn11), axis=1)
        Xn = np.concatenate((Xn,Xn12), axis=1)
        Xn = np.concatenate((Xn,Xn22), axis=1)
        self.XN = Xn

    def create_extended_matrixes(self):
        matrixes = func.create_extended_matrixes(self.X)
        self.Xn, self.Xe, self.Xn_e = matrixes[0], matrixes[1], matrixes[2]

    def model2(self, X, y):
        x1, x2 = X[:,1], X[:,2]
        b = func.log_gradient_descent(X, y, N=10, a=0.5, verbose=True, plot=True)
        c = b[0] + b[1]*x1 + b[2]*x2 + b[3]*x1**2 + b[4]*x1*x2 +b[5]*x2**2
        idx = 0
        for i in range(len(x1)):
            x11, x22 = x1[idx], x2[idx]
            c = b[0] + b[1]*x11 + b[2]*x22 + b[3]*x11**2 + b[4]*x11*x22 +b[5]*x22**2
            idx += 1
            print(f"\nModel: {c}\n")
        #print(f"GRADIENT DESCENT BETA: {b}")

    def model(self, X, d):
        b = self.map_features(X, d)
        sum_b = np.sum(b)
        print(f"Model: {sum_b}\n")
        #print(f"GRADIENT DESCENT BETA: {b}\n")

    def model_iterate(self, X, y):
        idx = 0
        x1, x2 = X[:,1].ravel(), X[:,2].ravel()
        for x in x1:
            #print(x1[idx])
            self.model(X, y)
            idx += 1

    def map_features(self, Xe, d):
        X = func.map_features(Xe, d)
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
f = plt.figure(figsize=(12,9))

m.model(m.X, 5)
b = func.log_gradient_descent(m.XN, m.y)
m.model2(m.XN, m.y)

#m.plot_data()
#plt.show()



