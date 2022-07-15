from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np

path = "../datasets/microchips.csv"

chip_1 = [-0.3, 1]
chip_2 = [-0.5, -0.1]
chip_3 = [0.6, 0]
X_test = [chip_1, chip_2, chip_3]

class KNN:

    def __init__(self, path):
        data = pd.read_csv(path).values
        self.X = data[:,[0,1,2]]
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

    def euclidean_distance(self, v1, v2):
        """
        Calculate the euclidean distance between two vectors v1 and v2.
        Returns the squared distance.
        """
        d = 0
        for i in range(len(v1)):
            d += (v1[i] - v2[i])**2
        return sqrt(d)

    def get_neighbors(self, v, k):
        """
        Get k closest neighbors for a passed vector.
        Uses other functions as 'euclidean_distance' to determine the distance
        between the passed vector and remaining points in dataset.
        """
        neighbors = []
        distances = []
        dist = np.zeros_like(self.X[:,[0,1]], dtype=object)
        idx = 0
        for vector in self.X:
            distance = self.euclidean_distance(v, vector)
            dist[idx][0] = distance
            dist[idx][1] = vector
            idx+=1
        dist = dist[dist[:,0].argsort()]
        #print(dist)
        for i in range(k):
            neighbors.append(dist[i][1])  # Get the k closest points
        return np.array(neighbors)

    def determine_point(self, vector, neighbors):
        """
        Check whether the passed vector should result in a green or red dot.
        """
        half = round(len(neighbors)/2)
        y = np.sum(neighbors[:,2])
        return y >= half

    def model(self, v, k):
        """
        Classification model determining 0 or 1 for a vector 'v'.
        """
        n = self.get_neighbors(v, k)
        n_y = np.sum(n[:,2])
        half = floor(k/2)
        return n_y > half

    def model_clf(self, X, k):
        """
        Classify each vector provided in the passed parameter 'X'.
        Possible values are either 0 or 1. 
        The value of 'k' will determine the amount of neighbors per point.
        """
        predicted_y = []
        for vector in X:
            pred_y = 0
            flag = self.model(vector, k)
            if flag == True:
                pred_y = 1
            predicted_y.append(pred_y)
        return np.array(predicted_y)

    def decision_boundary(self, xx, yy, k):
        """
        OUTDATED VERSION! ==> model_clf is used instead.
        -----------------------------------------------
        Plot the decision boundary on passed meshgrid.
        """
        x_idx = 0
        for x_val in xx:
            x = x_val[x_idx]
            y_idx = 0
            for y_val in yy:
                y = y_val[y_idx]
                point = [x, y]
                flag = self.model(point, k)
                plt.scatter(x, y, c='g' if flag==True else 'r', alpha=0.2)
                y_idx += 1
            x_idx += 1

    def simulate(self):
        """
        Calculate the closest neighbors in four cases whereas k is 1, 3, 5 and 7.
        The results will be plotted in four subplots with decision boundaries provided
        in each case.
        """
        fig = plt.figure(figsize=(16,12))
        plt.suptitle("Closest neighbors")
        K = [1, 3, 5, 7]
        i = 1
        xx, yy = self.meshgrid(self.X, self.y, 1, 0.05)
        colormap = colors.ListedColormap(['red', 'green']) # colormap for values 0 and 1
        for k in K:
            # Setup proper subplot parameters
            plt.subplot(2,2,i), plt.xlabel('x0'), plt.ylabel('x1'), plt.title(f"k == {k}")
            # Predict y values for each point in meshgrid
            Y = self.model_clf(np.c_[xx.ravel(), yy.ravel()], k).reshape(xx.shape)
            # Plot the decision boundary
            plt.contourf(xx, yy, Y, cmap=colormap, alpha=0.35)
            for x in self.X:
                # Plot the original data
                plt.scatter(x[0], x[1], c='g' if x[2] == 1 else 'r', s=15, edgecolors='k')
            for X in X_test:
                # Plot the new data
                flag = self.model(X, k)
                plt.scatter(X[0], X[1], s=85, edgecolors='k', c='g' if flag==True else 'r')
            i += 1 # Increasing index for new subplots



k = KNN(path)
k.simulate()
plt.show()
