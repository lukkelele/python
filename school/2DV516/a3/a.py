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
        self.fig = plt.figure(figsize=(12,10))
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]] 
        self.y = data[:,2]
        self.x0 = data[:,0]
        self.x1 = data[:,1]

    def generate_training_sample(self, datapoints):
        np.random.seed(7)   # 7 for comparison in the code
        r = np.random.permutation(datapoints)
        X, y = self.X[r, :], self.y[r]
        sample_end = int(datapoints/2)
        X_s, y_s = X[0:sample_end:1], y[0:sample_end:1]
        X_test, Y_test = X[sample_end:datapoints:1], y[sample_end:datapoints:1]
        return [X_s, y_s, X_test, Y_test]

    def make_meshgrid(self, x, y, step=0.05):
        x_min, x_max = x.min() - 3, x.max() + 3
        y_min, y_max = y.min() - 3, y.max() + 3
        plt.xlim(x_min, x_max), plt.ylim(y_min, y_max)
        xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
        return xx, yy

    def plot_contour(self, clf, xx, yy):
        p = plt.subplot(211)
        pred = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        plot = p.contourf(xx, yy, pred) 
        return plot

    # C trades off misclassification of training examples 
    # gamma defines how much influence a single training example has
    def get_classifier(self, kernel, gamma, C, verbose=False):
        classifier = svm.SVC(kernel=kernel, gamma=gamma, C=C, verbose=verbose)
        return classifier
    
    def evaluate(self, test, pred):
        conf_matrix = metrics.confusion_matrix(test, pred)
        classification_report = metrics.classification_report(test, pred)
        print(f"Confusion matrix:\n{conf_matrix}\n---------\nClassification report:\n{classification_report}\n=====================")

a = a(path)
sample = a.generate_training_sample(SAMPLE_SIZE)
X, Y, X_test, Y_test = sample[0], sample[1], sample[2], sample[3]
clf = a.get_classifier('rbf', 0.5, 20)
score = clf.fit(X, Y).score(X, Y)
xx, yy = a.make_meshgrid(X_test, Y_test)
plot = a.plot_contour(clf, xx, yy)

predicted_Y = clf.predict(X_test)
#plt.scatter(X_test[:,0], predicted_Y) 
#plt.scatter(X_test[:,1], Y_test)

plt.show()
