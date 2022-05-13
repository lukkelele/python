from matplotlib import pyplot as plt
from sklearn import tree
from time import time
import pandas as pd
import numpy as np

path = './data/bm.csv'

class Ensemble:

    def __init__(self, path, sample_size=0.5):
        self.start_time = time()
        print("==> Starting...")
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]]
        self.y = data[:,2]
        self.divide_data(self.X, self.y, train_size=sample_size, verbose=True)
        self.bootstrap_data(self.x_train, self.y_train, len(self.x_train))

    def divide_data(self, X, y, train_size=0.80, verbose=False):
        test = 1 - train_size
        rows = np.size(X,0)
        idx = round(test*rows) - 1
        self.x_test = X[:idx]
        self.y_test = y[:idx]
        self.x_train = X[idx:]
        self.y_train = y[idx:]
        if verbose: print(f"==> DATA SIZES (samples)\n    x_train == {len(self.x_train)}\n"+
                          f"    y_train == {len(self.y_train)}\n    x_test == {len(self.x_test)}\n"+
                          f"    y_test == {len(self.y_test)}\n==========================")

    def bootstrap_data(self, X, y, n):
        y = y.reshape(-1,1)
        rng = np.random.default_rng()
        r = np.zeros([n, 100], dtype=int)
        XX = np.zeros([n,2,100])
        Y = np.zeros([n,1,100])
        print(XX.shape)
        print(Y.shape)
        print(X.shape)
        print(y.shape)
        for i in range(100):
            r[:,i] = rng.choice(n, size=n, replace=True)
            XX[:,:,i] = X[r[:,i], :]
            Y[:,:,i] = y[r[:,i]]
        self.XX = XX
        self.Y = Y
        


en = Ensemble(path)

