from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import ml

path = "./data/microchips.csv"

chip_1 = [-0.3, 1]
chip_2 = [-0.5, -0.1]
chip_3 = [0.6, 0]
X_test = [chip_1, chip_2, chip_3]

class KNN:

    def __init__(self, path):
        data = pd.read_csv(path).values  # pyright: ignore
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

    def get_neighbors(self, p, k):
        """
        Get k closest neighbors for a passed point.
        Uses other functions as 'euclidean_distance' to determine the distance
        between the passed vector and remaining points in dataset.
        """
        neighbors = []
        distances = []
        dist = np.zeros_like(self.X[:,[0,1]], dtype=object) # instantiate at init
        idx = 0
        for point in self.X:
            distance = self.euclidean_distance(p, point)
            dist[idx][0] = distance
            dist[idx][1] = point
            idx+=1
        dist = dist[dist[:,0].argsort()]
        #print(dist)
        for i in range(k):
            neighbors.append(dist[i][1])  # Get the k closest points
        return np.array(neighbors)

    def model(self, p, k):
        """
        Classification model determining 0 or 1 for a point 'p'.
        """
        n = self.get_neighbors(p, k)
        n_y = np.sum(n[:,2])
        half = floor(k/2)
        if n_y > half: 
            return 1
        else:
            return 0

    def model_clf(self, X, k):
        """
        Classify each vector provided in the passed parameter 'X'.
        Possible values are either 0 or 1. 
        The value of 'k' will determine the amount of neighbors per point.
        """
        predicted_y = []
        for vector in X:
            pred_y = self.model(vector, k)
            predicted_y.append(pred_y)
        return np.array(predicted_y)


    def simulate(self):
        """
        Calculate the closest neighbors in four cases whereas k is 1, 3, 5 and 7.
        The results will be plotted in four subplots with decision boundaries provided
        in each case.
        """
        fig = plt.figure(figsize=(16,12))
        plt.suptitle("Closest neighbors")
        #K = [1, 3, 5, 7]
        K = [1, 5]
        i = 1
        print(f"len self.X ==> {len(self.X[:,[0,1,2]])}")
        xx, yy = self.meshgrid(self.X, self.y, 1, 0.05)
        colormap = colors.ListedColormap(['red', 'green']) # colormap for values 0 and 1
        print("\nStarting simulation...\n")
        for k in K:
            training_errors = 0
            print(f"============\nCurrent K: {k}")
            # Setup proper subplot parameters
            plt.subplot(2,2,i), plt.xlabel('x0'), plt.ylabel('x1'), plt.title(f"k == {k}")
            # Predict y values for each point in meshgrid
            Y = self.model_clf(np.c_[xx.ravel(), yy.ravel()], k).reshape(xx.shape)
            # Plot the decision boundary
            plt.contourf(xx, yy, Y, cmap=colormap, alpha=0.35)
            for x in self.X:
                # Plot the original data
                y_predicted = self.model(x, k)
                plt.scatter(x[0], x[1], c='g' if x[2] == 1 else 'r', s=15, edgecolors='k')

            for X in X_test:
                # Plot the new data
                print(f"<< Chip: {X}", end=" ")
                y_pred = self.model(X, k)
                print("==> OK") if y_pred == 1 else print("==> FAIL")
                plt.scatter(X[0], X[1], s=85, edgecolors='k', c='g' if y_pred == 1 else 'r')
            i += 1 # Increasing index for new subplots
            print(f"-----------\n>> Training errors: {training_errors}\n")



k = KNN(path)
k.simulate()
#plt.show()


