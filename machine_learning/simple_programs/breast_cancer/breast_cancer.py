from matplotlib import pyplot as plt
from lib import mlrlib as func
from lib import csv_parser
import numpy as np

csv_path = "../data/breast_cancer.csv"

# How the data is divided does not really make a difference in the end results.
# The dataset is shuffled at the beginning which helps keep randomized datasets per simulation.

class Cancer:
    def __init__(self, path):
        #self.fig = plt.figure(figsize=(12,9))
        self.parse_csv_file(path)
        self.adjust_response()
        self.divide_data(self.Xn_e, 0.8)
        self.b_grad_test = self.train_model(self.test_set, self.y_test, 500, 0.5)
        self.b_grad_training = self.train_model(self.training_set, self.y_training, 500, 0.5)

    def parse_csv_file(self, path):
        dataset = csv_parser.open_cancer_file(path)
        np.random.shuffle(dataset)
        self.n = len(dataset)
        self.X = dataset[:,[0,1,2,3,4,5,6,7,8]]
        self.y = dataset[:, 9]
        self.create_extended_matrixes()
        self.b = func.calc_beta(self.Xe, self.y)

    def create_extended_matrixes(self):
        matrixes = func.create_extended_matrixes(self.X)
        self.Xn, self.Xe, self.Xn_e = matrixes[0], matrixes[1], matrixes[2]

    def adjust_response(self):
        idx = 0
        for response in self.y:
            if response == 2: self.y[idx] = 0
            else: self.y[idx] = 1
            idx += 1

    def plot_cost(self):
        self.train_model(self.training_set, self.y_training, 1000, 0.5, verbose=False, plot=True)
        plt.show()

    def divide_data(self, X, training):
        test = 1 - training
        rows = np.size(X,0)
        idx = round(test*rows) - 1
        self.test_set = X[:idx]
        self.y_test = self.y[:idx]
        self.training_set = X[idx:]
        self.y_training = self.y[idx:]

    def train_model(self, X, y, N, a, verbose=False, plot=False):
        return func.log_gradient_descent(X, y, N, a, verbose, plot)

    def compute_accuracy(self, verbose=False):
        training_errors = func.log_compute_errors(self.training_set, self.y_training, self.b_grad_training)
        test_errors = func.log_compute_errors(self.test_set, self.y_test, self.b_grad_test) 
        tot_training = len(self.training_set)
        tot_test = len(self.test_set)
        training_correct = tot_training - training_errors
        test_correct = tot_test - test_errors
        training_accuracy = round((training_correct / tot_training), 3)
        test_accuracy = round((test_correct / tot_test), 3)
        if verbose: print(f"Training errors: {training_errors}\nTest errors: {test_errors}\nTraining accuracy: {training_accuracy}\nTest accuracy: {test_accuracy}\n")
        return [training_accuracy, test_accuracy]


training = []
test = []
runs = 10
fig = plt.figure(figsize=(12,9))
print("===== RUNNING =====")
for i in range(runs):
    c = Cancer(csv_path)
    a = c.compute_accuracy(verbose=True)
    training.append(a[0])
    test.append(a[1])

training_mean = round(np.mean(training), 3)
test_mean = round(np.mean(test), 3)
p = round(((training_mean/test_mean) * 100), 2)
print(f"Average training accuracy: {training_mean}\nAverage test accuracy: {test_mean}\nTraining / Test: {p}%")
Cancer(csv_path).plot_cost()
