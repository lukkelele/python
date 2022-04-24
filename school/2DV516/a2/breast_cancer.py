from matplotlib import pyplot as plt
from lib import csv_parser
import mlrlib as func
import numpy as np

csv_path = "./data/breast_cancer.csv"

class Cancer:
    
    def __init__(self, path):
        self.fig = plt.figure(figsize=(12,9))
        self.parse_csv_file(path)
        self.adjust_response()
        self.divide_data(self.Xn_e, 0.8)
        self.b_grad_test = self.train_model(self.test_set, self.y_test, 200, 0.5)
        self.b_grad_training = self.train_model(self.training_set, self.y_training, 200, 0.5)

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

    def get_errors(self):
        training_errors = func.log_compute_errors(self.training_set, self.y_training, self.b_grad_training)
        test_errors = func.log_compute_errors(self.test_set, self.y_test, self.b_grad_test) 
        tot_training = len(self.training_set)
        tot_test = len(self.test_set)
        training_correct = tot_training - training_errors
        test_correct = tot_test - test_errors
        training_accuracy = training_correct / tot_training
        test_accuracy = test_correct / tot_test
        print(f"Training accuracy: {round(training_accuracy, 3)}\nTest accuracy: {round(test_accuracy, 3)}")


c = Cancer(csv_path)

c.train_model(c.training_set, c.y_training, 100, 0.5, verbose=False, plot=True)

c.get_errors()

#plt.show()


