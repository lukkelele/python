from matplotlib import pyplot as plt
import mlrlib as func
import numpy as np
import csv_parser


# The 7th column is the response y
# Find f(X) = B0 + B1*X1 + ... + B6*X6

csv_path = "./data/GPUbenchmark.csv"

class GPU_benchmark:
    
    def __init__(self, path):
        self.path = path
        self.parse_csv_file()
        self.fig = plt.figure(figsize=(12,9))

    def parse_csv_file(self):
        dataset = csv_parser.open_gpu_file(self.path)
        self.X = dataset[:,[0,1,2,3,4,5]]
        self.y = dataset[:,6]
        self.x0 = dataset[:,0]
        self.x1 = dataset[:,1]
        self.x2 = dataset[:,2]
        self.x3 = dataset[:,3]
        self.x4 = dataset[:,4]
        self.x5 = dataset[:,5]

    def normalize_X(self, X):
        col_length = len(X[:,0])
        Xn = func.normalize_column(X, 0).reshape(col_length, 1)
        for i in range(1, 6):
            xn = func.normalize_column(X, i).reshape(col_length, 1)
            Xn = np.concatenate((Xn, (xn)), axis=1)
        return Xn

    def plot_features(self, X, y):
        for i in range(6):
            plt.subplot(2, 3, i+1)
            plt.scatter(X[:, i], y, s=10, color="b")


g = GPU_benchmark(csv_path)
print(g.normalize_X(g.X))
g.plot_features(g.X, g.y)
#plt.show()
