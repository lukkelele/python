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

    def scatter_point(self, p, y_pred, k):
        color = 'g' if y_pred == 1 else 'r'
        plt.scatter(p[0], p[1], c=color, s=12, edgecolors='k', alpha=0.92)

    def simulate(self, k):
        print(f">>> K: {k}")
        training_errors = 0
        for x in self.X:
            y_pred = ml.knn_clf(x, k, self.X)
            #print(f"[ {x[0]}   {x[1]}  ==>  {y_pred} ]")
            self.scatter_point(x, y_pred, k)
            y = int(x[2])
            if y_pred != y:
                training_errors += 1
        print(f">> Training errors: {training_errors}")
        for chip in X_test:
            y_pred = ml.knn_clf(chip, k, self.X)
            print(f"[ {chip[0]}   {chip[1]}  ==>  {y_pred} ]")
            color = 'g' if y_pred == 1 else 'r'
            plt.scatter(chip[0], chip[1], c=color, s=40, edgecolors='k')

    def main(self):
        print("\n>> Starting...\n")
        K = [1, 3, 5, 7]
        i = 1
        for k in K:
            plt.subplot(2,2,i)
            self.simulate(k)
            i+=1

        #plt.show()
    

knn = KNN(path)
knn.main()
