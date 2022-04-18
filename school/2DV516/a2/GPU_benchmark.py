from matplotlib import pyplot as plt
import mlrlib as func
import numpy as np
import csv_parser


# The 7th column is the response y
# Find f(X) = B0 + B1*X1 + ... + B6*X6

csv_path = "./data/GPUbenchmark.csv"
task_3_values = [2432, 1607, 1683, 8, 8, 256]


class GPU_benchmark:
    
    def __init__(self, path):
        self.path = path
        self.parse_csv_file()
        self.fig = plt.figure(figsize=(12,9))

    def parse_csv_file(self):
        dataset = csv_parser.open_gpu_file(self.path)
        self.X = dataset[:,[0,1,2,3,4,5]]
        self.y = dataset[:,6]
        self.Xe = func.extend_matrix(self.X, len(self.X))
        self.x0 = dataset[:,0]
        self.x1 = dataset[:,1]
        self.x2 = dataset[:,2]
        self.x3 = dataset[:,3]
        self.x4 = dataset[:,4]
        self.x5 = dataset[:,5]

    def normalize_X(self, X):
        col_length = len(X[:,0])
        Xn = func.normalize_column(X, 0).reshape(col_length, 1)
        for i in range(1,6):
            print(i)
            xn = func.normalize_column(X, i).reshape(col_length, 1)
            Xn = np.concatenate((Xn, (xn)), axis=1)
        return Xn

    def plot_features(self, X, y):
        for i in range(6):
            current_column = X[:,i]
            x_min, x_max = np.min(current_column) - 1, np.max(current_column) + 1
            plt.subplot(2, 3, i+1)
            plt.xlim(x_min, x_max)
            plt.xlabel(f"x_{i}")
            plt.ylabel("y")
            plt.scatter(current_column, y, s=10, color="b")

    def calc_beta(self, Xe, y):
        beta = func.calc_beta(Xe, y)
        #print(beta)
        return beta

    def calc_benchmark(self, X, beta):
        benchmark_result = (beta[0] + beta[1]*X[0] + beta[2]*X[1] + beta[3]*X[2] +
                            beta[4]*X[3] + beta[5]*X[4] + beta[6]*X[5])
        return benchmark_result

    def calc_cost(self, X, beta, y, n):
        cost = func.calc_cost(X, beta, y, n)
        return cost



g = GPU_benchmark(csv_path)
#print(g.normalize_X(g.X))
#g.plot_features(g.normalize_X(g.X), g.y)

b = g.calc_beta(g.Xe, g.y)
g.normalize_X(g.X)
g.calc_benchmark(task_3_values, b)
print(g.calc_cost(g.X, b, g.y, len(g.X[:,0])))

plt.subplots_adjust(wspace=0.28)
#plt.show()
