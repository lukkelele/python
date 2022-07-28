from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

# header = -1 to set it to None in ml.py
data = ml.open_csv_file('./data/housing_price_index.csv', header=-1)
X, y = data[:,[0,1]], data[:,1]

def plot_original_data(X, y):
    plt.title('Housing price index', fontsize=17)
    plt.scatter(X, y, edgecolors='k', c='g')
    plt.show()

def plot_poly_variants(X, y, d):
    for i in range(1, d+1):
        plt.subplot(2,2,i)
        plt.title(f"X**{i}")
        X_p = ml.polynomial(X, i)
        #print(f"X_p == {X_p}")
        gradients = ml.calc_beta(X_p, y)
        print(f"GRADIENTS ==> {gradients}")
        Y = X_p.dot(gradients)
        print(f"\n -- Y \n {Y}")
        plt.plot(X, y, c='r')
        plt.scatter(X, Y, c='g', s=12)
    plt.show()


plt.figure(figsize=(12,12))

#poly = ml.polynomial(X[:,1], 3)
#plot_original_data(X[:,0], y)
plot_poly_variants(X[:,0], y, 4)

