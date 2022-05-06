from matplotlib import pyplot as plt
import csv_parser as csv
import sklearn as sk
import pandas as pd
import numpy as np

path = './data/bm.csv'

class a:

    def __init__(self, path):
        cols = ['x0', 'x1', 'y']
        data = pd.read_csv(path, names=cols) 
        print(data)

    def generate_sample(self, datapoints):
        np.random.seed(7)
        r = np.random.permutation(datapoints)
        




a = a(path)

a.generate_sample(5000)
