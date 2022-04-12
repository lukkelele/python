# EXERCISE A

from matplotlib import pyplot as plt
import csv_parser as csv
import numpy as np
import math

# Column 1: girl height
# Column 2: mom height
# Column 3: dad height
path = "./data/girls_height.csv"

class Exercise_A:

    def __init__(self, path):
        self.dataset = csv.open_csv_file(path)

    def plot_dataset(self):
        f = plt.figure(figsize=(12,9))
        plt.subplot(2,2,1)
        plt.title("Dataset")
        plt.xlabel('mom height')
        plt.ylabel('dad height')
        y = self.dataset[:, 0]
        x0 = self.dataset[:, 1]
        x1 = self.dataset[:, 2]
        X = self.dataset[:, [1,2]]
        #x0_min, x1_min = np.min(x0), np.min(x1)
        #x0_max, x1_max = np.max(x0), np.max(x1)
        plt.plot(X, y, c="b")
        plt.show()
        


a = Exercise_A(path=path)
a.plot_dataset()
