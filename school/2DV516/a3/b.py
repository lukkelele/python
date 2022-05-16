from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

path = ""
XOR = np.array([ [0, 0],
                 [0, 1],
                 [1, 0],
                 [1, 1] ])
XOR_out = np.array([ [0], [1], [1], [0] ])

class B:

    def __init__(self):
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]]
        self.y = data[:,2]
