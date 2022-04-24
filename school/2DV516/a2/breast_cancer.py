from matplotlib import pyplot as plt
from lib import csv_parser
import mlrlib as func
import numpy as np

csv_path = "./data/breast_cancer.csv"

# Divide 80/20

class Cancer:
    
    def __init__(self, path):
        self.fig = plt.figure(figsize=(12,9))
        self.parse_csv_file(path)
        self.adjust_response()
        self.divide_data(self.Xn_e, 0.8)

    def parse_csv_file(self, path):
        dataset = csv_parser.open_cancer_file(path)
        np.random.shuffle(dataset)
        self.n = len(dataset)
        self.X = dataset[:,[0,1,2,3,4,5,6,7,8]]
        self.y = dataset[:, 9]
        self.create_extended_matrixes()

    def create_extended_matrixes(self):
        matrixes = func.create_extended_matrixes(self.X)
        self.Xn, self.Xe, self.Xn_e = matrixes[0], matrixes[1], matrixes[2]

    def adjust_response(self):
        idx = 0
        for response in self.y:
            if response == 2: self.y[idx] = 0
            else: self.y[idx] = 1
            idx += 1

    def divide_data(self, X, training):
        test = 1 - training
        rows = np.size(X,0)
        idx = round(test*rows) - 1
        sets = np.split(X, [idx])
        self.training_set = sets[0]
        self.test_set = sets[1]



c = Cancer(csv_path)



