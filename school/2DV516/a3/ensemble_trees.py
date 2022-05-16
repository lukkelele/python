from sklearn.model_selection import cross_val_score
from matplotlib import pyplot as plt
from sklearn import tree
from time import time
import a3_lib as a3
import pandas as pd
import numpy as np

path = './data/bm.csv'

class Ensemble:

    def __init__(self, path, sample_size=0.5):
        self.start_time = time()
        print("==> Starting...")
        data = pd.read_csv(path).values
        self.X = data[:,[0,1]]
        self.y = data[:,2]
        self.divide_data(self.X, self.y, train_size=sample_size, verbose=True)
        self.bootstrap_data(self.x_train, self.y_train, len(self.x_train))
        #self.predict_data()
        self.calc_all_tree_errors(self.x_train, self.y_train)
        self.calc_ensemble_errors(self.x_test, self.y_test)
        clf = tree.DecisionTreeClassifier()
        scores = cross_val_score(clf, self.x_test, self.y_test, verbose=2)
        print(scores)

    def divide_data(self, X, y, train_size=0.80, verbose=False):
        test = 1 - train_size
        rows = np.size(X,0)
        idx = round(test*rows) - 1
        self.x_test = X[:idx]
        self.y_test = y[:idx]
        self.x_train = X[idx:]
        self.y_train = y[idx:]
        if verbose: print(f"==> DATA SIZES (samples)\n    x_train == {len(self.x_train)}\n"+
                          f"    y_train == {len(self.y_train)}\n    x_test == {len(self.x_test)}\n"+
                          f"    y_test == {len(self.y_test)}\n==========================")

    def bootstrap_data(self, X, y, n):
        y = y.reshape(-1,1)
        rng = np.random.default_rng()
        r = np.zeros([n, 100], dtype=int)
        XX = np.zeros([n,2,100])
        Y = np.zeros([n,1,100])
        self.clfs = []
        classifier = tree.DecisionTreeClassifier()
        for i in range(100):
            r[:,i] = rng.choice(n, size=n, replace=True)
            XX[:,:,i] = X[r[:,i], :]
            Y[:,:,i] = y[r[:,i]]
            self.clfs.append(classifier.fit(XX[:,:,i], Y[:,:,i]))
        self.XX = XX
        self.Y = Y

    def calc_errors(self, clf, X, y, verbose=False):
        acc = clf.score(X, y) 
        err = 1 - acc
        if verbose: print(f"==> Accurarcy: {round(acc*100, 5)}%\n    Error: {round(err*100, 5)}%")
        return acc

    def calc_ensemble_errors(self, X, y):
        res = 0
        for i in range(100):
            clf = self.clfs[i]
            pred_y = clf.predict(X)
            score = clf.score(X, y)
            if np.sum(pred_y) > 2500: res += 1
        print(res)

    def calc_all_tree_errors(self, X, y):
        res = 0
        for i in range(100):
            X = self.x_train
            y = self.y_train
            clf = self.clfs[i]
            acc = self.calc_errors(clf, X, y)
            res += acc
        res = round(res, 4)
        print(f"==> Mean accuracy for 100 trees: {res}%\n    Error rate: {round(100-res, 4)}%")

    def predict_data(self):
        plt.figure(figsize=(18,15))
        xx, yy = a3.make_meshgrid(self.x_train[:,0], self.x_train[:,1])
        point_size = 4
        print("==> Predicting data...")
        for i in range(100):
            plt.subplot(10,10,i+1)
            current_clf = self.clfs[i]
            pred_xy = current_clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
            plot = plt.contour(xx, yy, pred_xy, cmap='bwr')
        


en = Ensemble(path)
#plt.show()
