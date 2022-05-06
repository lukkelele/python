from matplotlib import pyplot as plt
import csv_parser as csv
import sklearn as sk
import pandas as pd
import numpy as np


path = './data/bm.csv'
SAMPLE_SIZE = 5000


class a:

    def __init__(self, path):
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]] 
        self.y = data[:,2]
        self.x0 = data[:,0]
        self.x1 = data[:,1]

    def generate_sample(self, datapoints):
        np.random.seed(7)   # 7 for comparison in the code
        r = np.random.permutation(datapoints)
        X, y = self.X[r, :], self.y[r]
        X_s, y_s = X[:5000:1], y[:5000:1]

    


a = a(path)
a.generate_sample(SAMPLE_SIZE)
