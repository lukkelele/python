from matplotlib import pyplot as plt
from lib import csv_parser
import mlrlib as func
import numpy as np

# Parametric classification method

csv_path = "./data/admission.csv"

class B:
    
    def __init__(self, path):
        self.fig = plt.figure(figsize=(12,9))
        self.parse_csv_file(path)

    def parse_csv_file(self, path):
        dataset = csv_parser.open_admission_file(path)
        self.n = len(dataset)
        self.X = dataset[:,[0,1]]
        self.y = dataset[:,2]
        self.create_extended_matrixes()
        self.x0_std = np.std(self.X[:,0])
        self.x1_std = np.std(self.X[:,1])
        self.x0_mean = np.mean(self.X[:,0])
        self.x1_mean = np.mean(self.X[:,1])

    def create_extended_matrixes(self):
        matrixes = func.create_extended_matrixes(self.X)
        self.Xn, self.Xe, self.Xn_e = matrixes[0], matrixes[1], matrixes[2]

    def plot_data(self):
        plt.xlabel('points')
        plt.ylabel('points')
        admitted_flag = False
        not_admitted_flag = False
        y = self.y.reshape((100,1))
        X = np.concatenate((self.Xn, y), axis=1)
        for a in X:
            x0 = a[0]
            x1 = a[1]
            y = a[2]
            if y == 1: # current legend implementation is not memory efficient
                plt.scatter(x0, x1, s=40, color='g', marker="v", label='Admitted' if admitted_flag==False else "", edgecolors='k')
                admitted_flag = True
            else:
                plt.scatter(x0, x1, s=40, color='r', marker="x", label='Not admitted' if not_admitted_flag==False else "")
                not_admitted_flag = True
        plt.legend()

    def predict_score(self, score, X, beta):
        X = np.array(score)
        x0 = (score[0] - self.x0_mean) / self.x0_std
        x1 = (score[1] - self.x1_mean) / self.x1_std
        Xn = np.array([x0, x1])
        Xn_e = np.c_[1, Xn[0], Xn[1]]
        prob = func.sigmoid(Xn_e.dot(beta))
        print(f"Adm. prob. for scores {X[0]}, {X[1]} is {round(prob[0], 2)}")


b = B(csv_path)
b.plot_data()
a = np.array([[0,1], [2,3]])
X = func.normalize_matrix(a, 2,2)
Xe = func.extend_matrix(X)
print(X)
print("\n")
print(Xe)
print("\n")
#print(func.log_calc_cost(Xe, a[:,1], [0,0,0]))
#beta = func.calc_beta(b.Xe, b.y)
grad_desc = func.log_gradient_descent(Xe, a[:,1], 1, 0.5)
#grad_desc = func.log_gradient_descent(b.Xn_e, b.y, 100, 0.5)
print(grad_desc)

#func.log_compute_errors(b.Xe, b.y, beta)
#b.predict_score([45,85], b.X, beta)


#plt.show()
