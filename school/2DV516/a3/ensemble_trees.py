from matplotlib import pyplot as plt
from sklearn import svm 
from time import time
import pandas as pd
import numpy as np

path = './data/bm.csv'

class Ensemble:

    def __init__(self, path):
        self.start_time = time()
        print("==> Starting...")
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]]
        self.y = data[:,2]
        self.divide_data(self.X, self.y, verbose=True)

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




en = Ensemble(path)
