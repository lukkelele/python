from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import gaussian_process
from sklearn import svm 
from sklearn import metrics
import csv_parser as csv
import pandas as pd
import numpy as np


path = './data/bm.csv'
SAMPLE_SIZE = 5000


class a:

    def __init__(self, path):
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]] 
        self.y = data[:,2]
        self.x0 = data[:,0]
        self.x1 = data[:,1]

    def generate_training_sample(self, datapoints):
        np.random.seed(7)   # 7 for comparison in the code
        r = np.random.permutation(2*datapoints)
        X, y = self.X[r-1, :], self.y[r-1]
        X_s, y_s = X[:5000:1], y[:5000:1]
        X_test, Y_test = X[5000:10000:1], y[5000:10000:1]
        return [X_s, y_s, X_test, Y_test]

    # C trades off misclassification of training examples 
    # gamma defines how much influence a single training example has
    def get_classifier(self, kernel, gamma, C, verbose=False):
        classifier = svm.SVC(kernel=kernel, gamma=gamma, C=C, verbose=verbose)
        return classifier
    
    def make_prediction(self, clf, prediction):
        pred = clf.predict(prediction)
        return pred

    def evaluate(self, test, pred):
        conf_matrix = metrics.confusion_matrix(test, pred)
        classification_report = metrics.classification_report(test, pred)
        print(f"Confusion matrix:\n{conf_matrix}\n---------\nClassification report:\n{classification_report}\n=====================")

a = a(path)
sample = a.generate_training_sample(SAMPLE_SIZE)
X, Y, X_test, Y_test = sample[0], sample[1], sample[2], sample[3]
clf = a.get_classifier('rbf', 0.5, 20)
clf.fit(X, Y)
pred = a.make_prediction(clf, X_test)
print(f"Prediction: {pred}")
a.evaluate(Y_test, pred)
