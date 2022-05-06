from matplotlib import pyplot as plt
import csv_parser as csv
import sklearn as sk
import pandas as pd
import numpy as np

path = './data/bm.csv'
SAMPLE_SIZE = 5000

class a:

    def __init__(self, path):
        cols = ['x0', 'x1', 'y']
        data = pd.read_csv(path).values
        print(type(data))
        self.X = data[:,[0,1]] 
        self.y = data[:,2]
        self.x0 = data[:,0]
        self.x1 = data[:,1]

    def generate_sample(self, datapoints):
        np.random.seed(7)
        r = np.random.permutation(datapoints)
        X_s, y_s = X[:datapoints, :], y[:datapoints]
        print(len(X_s))



a = a(path)
a.generate_sample(SAMPLE_SIZE)
