from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import ml

path = "./data/microchips.csv"

chip_1 = [-0.3,    1]
chip_2 = [-0.5, -0.1]
chip_3 = [ 0.6,    0]
X_test = [chip_1, chip_2, chip_3]

class KNN:

    def __init__(self, path):
        data = ml.open_csv_file(path)
        self.X = data[:,[0,1,2]]
        self.y = data[:,2]

