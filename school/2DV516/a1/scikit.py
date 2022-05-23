from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np




path = "./A1_datasets/microchips.csv"
simulation_k = [1, 3, 5, 7]  # k's to be used when simulating

chip_1 = [-0.3, 1]
chip_2 = [-0.5, -0.1]
chip_3 = [0.6, 0]
X_test = [chip_1, chip_2, chip_3]

class KNN_Scikit:

    def __init__(self, path):
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]]
        self.y = data[:,2]

    def meshgrid(self, X, y, h=1, z=0.1):
        """
        Create a meshgrid with a minimum of min(X, y)-h and
        a maximum of max(X, y)+h and a step size of z.
        """
        self.x_min, self.x_max, self.y_min, self.y_max = X.min()-(h/4), X.max()+(h/4), y.min()-h, y.max()+(h/4)
        xx, yy = np.meshgrid(np.arange(self.x_min, self.x_max, z),
                             np.arange(self.y_min, self.y_max, z))
        return xx, yy

    def model(self, v, X, k):
        """
        Classification model determining 0 or 1 for a vector 'v'.
        """
        n = get_neighbors(v, X, k)
        n_y = np.sum(n[:,])

    def get_neighbors(self, v, X, y, k):
        """
        Get neighbors closest 'k' neighbors to 'v' from 'X'. 
        """
        clf = KNeighborsClassifier(n_neighbors=k)
        clf = clf.fit(X, y)
        neighbors = clf.kneighbors(v)[1]  # [1] returns indexes
        n = []
        for idx in neighbors:
            point = X[idx]
            point = np.append(point, y[idx])
            n.append(point)
        return np.array(n)

    def model_clf(self, X, k):
        """
        Classify each vector provided in the passed parameter 'X'.
        Possible values are either 0 or 1. 
        The value of 'k' will determine the amount of neighbors per point.
        USED FOR THE DECISION BOUNDARY!
        """
        predicted_y = []
        for vector in X:
            pred_y = 0
            flag = self.model(vector, k)
            if flag == True:
                pred_y = 1
            predicted_y.append(pred_y)
        return np.array(predicted_y)

    def simulate(self, X, y, k):
        """
        Train a model with 'k' neighbors and classify the 
        test chips.  
        """



k = KNN_Scikit(path)
k.get_neighbors([[0, 1]], k.X, k.y, 3)
