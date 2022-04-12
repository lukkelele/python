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
        print(self.dataset)

    def plot_dataset(self):
        plt.subplot(2,2,1)
        plt.title("Dataset")
        plt.xlabel('mom height')
        plt.ylabel('dad height')
        mom = self.dataset[:, 1]
        dad = self.dataset[:, 2]
        print(f"Mom: {mom}\n\n\n\nDad: {dad}")



a = Exercise_A(path=path)
a.plot_dataset()
