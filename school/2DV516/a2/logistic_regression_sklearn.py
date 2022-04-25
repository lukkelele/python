from matplotlib import pyplot as plt
from lib import csv_parser
import sklearn
import mlrlib as func
import numpy as np


csv_path = "./data/microchips.csv"

class LR_sklearn:

    def __init__(self, path):
       self.parse_csv_file(path)

    def parse_csv_file(self, path):
        dataset = csv_parser.open_microships_file(path)
        self.n = len(dataset)

    def logistic_regression(self, X):
        Xe = func.map_features(X, 2, ones=False)
        #logreg = func.log_gradient_descent
