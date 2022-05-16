from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm 
from sklearn import metrics
import pandas as pd
import numpy as np

# NOT USED THAT MUCH...

def prec_recall(x,y):
    return round((x/(x+y)), 3)

# pred is a predictability vector, y is 0/1 labels
def TP(pred, y):
    k = 0
    res = np.add(pred, y)

def make_meshgrid(x, y, step=0.1, h=3):
    x_min, x_max = x.min() - h, x.max() + h
    y_min, y_max = y.min() - h, y.max() + h
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
    return xx, yy

def get_xylims(X, h=1):
    x_min, x_max, y_min, y_max = np.min(X[:,0])-h, np.max(X[:,0])+h, np.min(X[:,1])-h, np.max(X[:,1])+h
    return x_min, x_max, y_min, y_max

def set_lims(X, h=1):
    x_min, x_max, y_min, y_max = get_xylims(X)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

def plot_contour(clf, xx, yy, cmap="gray"):
    pred = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plot = plt.contourf(xx, yy, pred, cmap=cmap, alpha=0.4, levels=[0.1,2]) 

def get_support_vectors(clf, X):
    support_vector_indices = clf.support_
    support_vectors = X[support_vector_indices]
    return support_vectors

# C trades off misclassification of training examples 
# gamma defines how much influence a single training example has
def get_classifier(kernel, gamma="", C="", d="", verbose=False):
    if gamma == "" and d == "": clf = svm.SVC(kernel='linear', C=C)
    elif d != "": clf = svm.SVC(kernel='poly', gamma=gamma, degree=d, C=C) 
    else: clf = svm.SVC(kernel=kernel, gamma=gamma, C=C)
    return clf


def evaluate(test, pred):
    conf_matrix = metrics.confusion_matrix(test, pred)
    classification_report = metrics.classification_report(test, pred)
    print(f"Confusion matrix:\n{conf_matrix}\n---------\nClassification report:\n{classification_report}\n=====================")


def plot_support_vectors(clf, X):
    support_vectors = self.get_support_vectors(clf, X)
    plt.scatter(
            support_vectors[:,0],
            support_vectors[:,1],
            s=22,
            edgecolors='k',
            c='g'        )


