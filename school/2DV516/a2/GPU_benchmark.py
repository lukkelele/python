from matplotlib import pyplot as plt
from lib import mlrlib as func
from lib import csv_parser
import numpy as np

# The 7th column is the response y
# Find f(X) = B0 + B1*X1 + ... + B6*X6

csv_path = "./data/GPUbenchmark.csv"

class GPU_benchmark:
    
    def __init__(self, path):
        self.path = path
        self.parse_csv_file()
        self.fig = plt.figure(figsize=(12,9))
        self.create_extended_matrixes()
        self.beta = func.calc_beta(self.Xe, self.y)
        self.beta_n = func.calc_beta(self.Xn_e, self.y)

    def parse_csv_file(self):
        dataset = csv_parser.open_gpu_file(self.path)
        self.X = dataset[:,[0,1,2,3,4,5]]
        self.y = dataset[:,6]
        self.n = len(self.X)
        self.x0 = dataset[:,0]
        self.x1 = dataset[:,1]
        self.x2 = dataset[:,2]
        self.x3 = dataset[:,3]
        self.x4 = dataset[:,4]
        self.x5 = dataset[:,5]

    def create_extended_matrixes(self):
        matrixes = func.create_extended_matrixes(self.X)
        self.Xn, self.Xe, self.Xn_e = matrixes[0], matrixes[1], matrixes[2]

    def calc_benchmark(self, X, beta):
        benchmark_result = (beta[0] + beta[1]*X[0] + beta[2]*X[1] + beta[3]*X[2] +
                            beta[4]*X[3] + beta[5]*X[4] + beta[6]*X[5])
        return benchmark_result

    def normalize_features(self, features):
        norm_vals = []
        for i in range(6):
            norm_vals.append(func.normalize_val(self.X, i, features[i]))
        return norm_vals

    def calc_cost(self, Xe, y, beta):
        j = np.dot(Xe, beta) - y
        J = (j.T.dot(j)) / self.n
        return J

    def gradient_descent(self, Xe, y, N, a):
        b = np.zeros((7,))
        for i in range(N):
            grad = -(Xe.T.dot(y - Xe.dot(b)) / self.n)
            b = b - a*grad
            cost = self.calc_cost(Xe, y, b)
            if i < 5: pass
            plt.scatter(i, cost, s=3, color="k")
        return b

    def cost_diff(self, norm, grad, margin):
        cost_error = margin * norm
        lower_boundary = norm - cost_error
        upper_boundary = norm + cost_error
        print(f"""Cost norm equ: {norm}\nCost grad desc: {grad}
Allowed difference between norm and grad:\n{round(lower_boundary, 3)} < {round(norm, 3)} < {round(upper_boundary, 3)}\n""")
        if norm - grad > lower_boundary and norm - grad < upper_boundary:
            print("The cost difference is within 1% --> SUCCESS!\n")
        else: print("The cost difference is within 1% --> SUCCESS!\n")


values = [2432, 1607, 1683, 8, 8, 256]
g = GPU_benchmark(csv_path)
print()
norm_vals = g.normalize_features(values)
norm_benchmark = g.calc_benchmark(norm_vals, g.beta_n)
gradient_descent = g.gradient_descent(g.Xn_e, g.y, 1000, 0.12)
grad_benchmark = g.calc_benchmark(norm_vals, gradient_descent)
cost_norm = g.calc_cost(g.Xn_e, g.y, g.beta_n)
cost_grad = g.calc_cost(g.Xn_e, g.y, gradient_descent)

print(f"""Benchmark normal equ: {norm_benchmark}
Benchmark grad desc: {g.calc_benchmark(norm_vals, gradient_descent)}\n""")
g.cost_diff(cost_norm, cost_grad, 0.01)
plt.show()
