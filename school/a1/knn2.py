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

    """
    Plot the decision boundary and compare the original datapoints to the
    closest neighbors on the meshgrid 
    """

    def __init__(self, path):
        data = ml.open_csv_file(path)
        self.X = data[:,[0,1,2]]
        self.y = data[:,2]
        self.xx, self.yy = ml.meshgrid(self.X, self.y, 1, 0.008)

    def scatter_point(self, p, y_pred, k, a=1.0):
        color = 'g' if y_pred == 1 else 'r'
        plt.scatter(p[0], p[1], c=color, s=12, edgecolors='k', alpha=a)

    def simulate(self, k):
        print(f">>> K: {k}")
        training_errors = 0
        for x in self.X:
            y_pred = ml.knn_clf(x, k, self.X)
            y_pred_mesh = ml.knn_clf(x, k, self.mesh)
            #print(f"[ {x[0]}   {x[1]}  ==>  {y_pred} ]")
            self.scatter_point(x, y_pred, k)
            if y_pred != y_pred_mesh:
                training_errors += 1
        for chip in X_test:
            y_pred = ml.knn_clf(chip, k, self.X)
            print(f"[ {chip[0]}   {chip[1]}  ==>  {y_pred} ]")
            color = 'g' if y_pred == 1 else 'r'
            plt.scatter(chip[0], chip[1], c=color, s=40, edgecolors='k')
        print(f">> Training errors: {training_errors}")

    def main(self):
        print("\n>> Starting...\n")
        colormap = colors.ListedColormap(['red', 'green']) # colormap for values 0 and 1
        #K = [1, 3, 5, 7]
        K = [5]
        i = 1
        meshgrid = np.c_[self.xx.ravel(), self.yy.ravel()] #.reshape(self.xx.shape)
        #print(meshgrid)
        for k in K:
            training_errors = 0
            plt.subplot(2,1,i), plt.xlabel('x0'), plt.ylabel('x1'), plt.title(f"k == {k}")
            Y_meshgrid = []
            X_meshgrid = []
            for point in meshgrid:
                y_mesh = ml.knn_clf(point, k, self.X)
                self.scatter_point(point, y_mesh, k, a=0.85)
                X_meshgrid.append(point)
                Y_meshgrid.append(y_mesh)
            Y_meshgrid = np.array([Y_meshgrid]).reshape(len(Y_meshgrid), 1)
            X_meshgrid = np.array(X_meshgrid)#.reshape(-1,2)
            self.mesh = np.append(X_meshgrid, Y_meshgrid, axis=1)
            #print(mesh)
            for x in self.X:
                "Compare y_val to meshgrid y_val"
                y_pred = ml.knn_clf(x, k, self.mesh)
                #print(f"> Predicted y : {y_pred}\n> Actual y : {x[2]}\n")
                if y_pred != int(x[2]):
                    training_errors += 1

            plt.contourf(self.xx, self.yy, Y_meshgrid.reshape(self.xx.shape), cmap=colormap, alpha=0.35)
            #print(f">>> Training errors: {training_errors}")
            self.simulate(k)
            i+=1

        plt.show()
    

knn = KNN(path)
knn.main()
