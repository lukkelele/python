from math import sqrt
import pandas as pd
import numpy as np



class KNN:

    def __init__(self, path):
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]]
        self.y = data[:,2]

    def euclidean_distance(self, v1, v2):
        """
        Calculate the euclidean distance between two vectors v1 and v2.
        Returns the squared distance.
        """
        d = 0
        for i in range(len(v1)-1):
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
        dist = np.zeros_like(self.X, dtype=object)
        idx = 0
        for vector in self.X:
            distance = self.euclidean_distance(v, vector)
            print(distance)
            dist[idx][0] = distance
            dist[idx][1] = vector
            idx+=1
        dist = dist[dist[:,0].argsort()]
        for i in range(k):
            neighbors.append(dist[i][1])  # Get the k closest distances
        return neighbors

    def simulate(self, s=4):
        """
        Calculate the closest neighbors in four cases whereas k is 1, 3, 5 and 7.
        """




path = "./A1_datasets/microchips.csv"

k = KNN(path)
n = k.get_neighbors([0,1], 3)
print(n)
