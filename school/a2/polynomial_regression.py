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
#plt.figure(figsize=(12,12))

def plot_original_data(X, y):
    plt.figure(figsize=(12,12))
    plt.title('Housing price index', fontsize=17)
    plt.scatter(X, y, edgecolors='k', c='g')
    plt.show()

def plot_poly_variants(X, y, d):
    dotcolor = ['b', 'g', 'm', 'darkblue']
    plt.figure(figsize=(12,12))
    plt.suptitle('Polynomial variants, X**i, i: 1 <-> 4', fontsize=16)
    for i in range(1, d+1):
        plt.subplot(2,2,i)
        plt.title(f"X**{i}", fontsize=16)
        X_p = ml.polynomial(X, i)
        gradients = ml.calc_beta(X_p, y)
        Y = X_p.dot(gradients)
        plt.plot(X, y, c='r')
        plt.scatter(X, Y, c=dotcolor[i-1], s=16 )
    plt.show()

def predict(X, y, year,  price, bought=1975, d=1):
    year = year - bought
    polynomial = ml.polynomial(X, d)
    gradients = ml.calc_beta(polynomial, y)
    p = ml.polynomial(np.array([year]), d)
    pred_y = p.dot(gradients)[0] / 100
    pred_price = pred_y * price / 10**6
    print(f"\n>> Predicted price: {round(pred_price, 4)} million kr\n   pred_y index = {round(pred_y, 2)}")
    print(f"   Price change = {round((pred_y-1), 2)}%\n")


house_price = 2.3 * 10**6

plot_original_data(X[:,0], y)
plot_poly_variants(X[:,0], y, 4)

predict(X[:,0], y, 2022, price=house_price, bought=2015, d=1)
predict(X[:,0], y, 2022, price=house_price, bought=2015, d=2)
predict(X[:,0], y, 2022, price=house_price, bought=2015, d=3)
predict(X[:,0], y, 2022, price=house_price, bought=2015, d=4)

