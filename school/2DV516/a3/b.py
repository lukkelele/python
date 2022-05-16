from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# NOT DONE

path = ""
XOR_in = np.array([ [0, 0],
                 [0, 1],
                 [1, 0],
                 [1, 1] ])
XOR_out = np.array([ 0, 1, 1, 0 ])
# x0 x1
# ============
# | 0  0 | 0 |
# | 0  1 | 1 |
# | 1  0 | 1 |
# | 1  1 | 0 |
# ============

class B:

    def __init__(self, path=""):
        if path != "":
            data = pd.read_csv(path).values
            self.X = data[:,[0,1]]
            self.y = data[:,2]
        self.mlp = MLPClassifier(solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 2))
        self.train_classifier()
   
    def train_classifier(self):
        self.mlp.fit(XOR_in, XOR_out)


b = B()
ara = np.arange(-10, 10, 1)
ara2 = np.arange(-20, 20, 2)
A = np.array([ara, ara2]).T
prediction = b.mlp.predict(XOR_in)
#score = b.mlp.score(A, XOR_out)
print(prediction)

