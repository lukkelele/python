# EXERCISE A

from matplotlib import pyplot as plt
import csv_parser as csv
import numpy as np
import math

path = "./data/girls_height.csv"

class Exercise_A:

    def __init__(self, path):
        self.dataset = csv.open_csv_file(path)

    def plot_dataset(self):
        plt.subplot(2,2,1)
        plt.title("Dataset")
        plt.xlabel('')
