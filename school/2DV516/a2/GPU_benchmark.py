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
        self.n = len(self.X)
        self.Xe = func.extend_matrix(self.X, len(self.X))
        self.x0 = dataset[:,0]
        self.x1 = dataset[:,1]
        self.x2 = dataset[:,2]
        self.x3 = dataset[:,3]
        self.x4 = dataset[:,4]
        self.x5 = dataset[:,5]
        self.beta = self.calc_beta(self.Xe, self.y) 

    def normalize_X(self, X):
        col_length = len(X[:,0])
        Xn = func.normalize_column(X, 0).reshape(col_length, 1)
        for i in range(1,6):
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
        return beta

    def calc_benchmark(self, X, beta):
        benchmark_result = (beta[0] + beta[1]*X[0] + beta[2]*X[1] + beta[3]*X[2] +
                            beta[4]*X[3] + beta[5]*X[4] + beta[6]*X[5])
        return benchmark_result

    def normalize_column(self, X, col):
        norm_col = func.normalize_column(X, col)
        return norm_col

    def normalize_val(self, X, col, val):
        column = X[:,col]
        mean = np.mean(column) 
        std = np.std(column) 
        norm_val = (val-mean)/std
        return norm_val

    def normalize_features(self, features):
        norm_vals = []
        for i in range(6):
            norm_vals.append(self.normalize_val(self.X, i, features[i]))
        return norm_vals

    def calc_cost(self, Xe, beta, y, n):
        j = np.dot(Xe, beta) - y
        J = (j.T.dot(j)) / n
        return J

    def gradient_descent(self, Xe, y, b, N, a):
        #b = func.gradient_descent(Xe, y, b, N, a)
        n = len(Xe)
        #print(Xe)
        for i in range(N):
            grad = -(Xe.T.dot(y - Xe.dot(b)) / n)
            b = b - a*grad
            cost = self.calc_cost(Xe, b, y, self.n)
            if i < 5: pass
            plt.scatter(i, cost, s=3, color="k")
        #plt.show()
        return b

    def task_3(self):
        values = [2432, 1607, 1683, 8, 8, 256]
        print(f"| Predicted benchmark: {self.calc_benchmark(values, self.beta)}")
        
    def task_4(self):
        print(f"| Cost J(B): {self.calc_cost(self.Xe, self.beta, self.y, len(self.x0))}")

    def run_tests(self):
        print("\n------------------------------------------------\n| Running tests...\n"+
              "------------------------------------------------")
        self.task_3()
        self.task_4()
        print("------------------------------------------------\n")



values = [2432, 1607, 1683, 8, 8, 256]

g = GPU_benchmark(csv_path)
g.run_tests()
grad_b = g.gradient_descent(g.Xe, g.y, [0,0,0,0,0,0,0], 100, 0.00000001)

#g.normalize_column(g.X, 0)
#print(g.normalize_val(g.X, 0, 3584))
norm_values = g.normalize_features(values)
print(g.calc_benchmark(norm_values, grad_b))


#print(g.calc_benchmark(norm_values, grad_b))

plt.subplots_adjust(wspace=0.28)
plt.show()











