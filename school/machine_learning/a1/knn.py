from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
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

    def scatter_point(self, p, y_pred, k, alpha=1.0, scale=12):
        color = 'g' if y_pred == 1 else 'r'
        plt.scatter(p[0], p[1], c=color, s=scale, edgecolors='k', alpha=alpha)

    def classify_grid(self, k, step_size, colormap):
        xx, yy = ml.meshgrid(self.X, self.y, offset=1, step_size=step_size) # offset and step size
        grid = np.c_[xx.ravel(), yy.ravel()] 
        Y, X = [], []
        for point in grid:
            y_pred = ml.knn_clf(point, k, self.X)  # classify each point in grid
            X.append(point)
            Y.append(y_pred)
        X, Y = np.array(X), np.array([Y]).reshape(len(Y), 1)
        mesh = np.append(X, Y, axis=1)  # Combine arrays 
        # Plot the decision boundary
        plt.contourf(xx, yy, Y.reshape(xx.shape), cmap=colormap, alpha=0.35) 
        return mesh

    def simulate(self, k, grid):
        training_errors = 0
        for x in self.X:
            y_pred = ml.knn_clf(x, k, self.X)
            y_pred_grid = ml.knn_clf(x, k, grid)
            if y_pred != y_pred_grid: # if 
                training_errors += 1
            self.scatter_point(x, y_pred, k, scale=15, alpha=0.75)
        for chip in X_test:
            y_pred = ml.knn_clf(chip, k, self.X)
            color = 'g' if y_pred == 1 else 'r'
            plt.scatter(chip[0], chip[1], c=color, s=30, edgecolors='k')
            # Alignment for terminal output
            output = f"[ {chip[0]} ,  {chip[1]} , {y_pred} ]"
            len_output = len(output)
            space_diff = 25 - len_output
            result_msg = "OK" if y_pred == 1 else "Fail"
            output = output + space_diff*" " + "==> " + result_msg
            print(output)
        return training_errors


    def main(self, argv):
        np.set_printoptions(threshold=sys.maxsize)
        try:
            if len(argv) == 1:
                step_size = 0.045
            else:
                step_size = float(argv[1])
            print(f"\nStarting...\nSTEP_SIZE: {step_size}\n")
            colormap = colors.ListedColormap(['red', 'green']) # colormap for values 0 and 1
            K = [1, 3, 5, 7]
            i = 1
            for k in K:
                print(f"\n===> CURRENT K: {k} <===")
                plt.subplot(2,2,i), plt.xlabel('x0'), plt.ylabel('x1')
                mesh = self.classify_grid(k, step_size, colormap)
                training_errors = self.simulate(k, mesh)
                print(f">> Training errors: {training_errors}\n")
                plt.title(f"k={k}, training errors = {training_errors}")
                i+=1
            plt.show()
        except:
            print()
    

knn = KNN(path)
knn.main(sys.argv)

