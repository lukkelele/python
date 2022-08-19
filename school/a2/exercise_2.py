from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

# header = -1 to set it to None in ml.py
data = ml.open_csv_file('./data/housing_price_index.csv', header=-1)
X, y = data[:,0], data[:,1]

def plot_original_data(X, y):
    plt.figure(figsize=(12,12))
    plt.title('Housing price index', fontsize=17)
    plt.scatter(X, y, edgecolors='k', c='g')

def plot_poly_variants(X, y, d):
    dotcolor = ['b', 'g', 'm', 'darkblue']
    plt.figure(figsize=(12,12))
    plt.suptitle('Polynomial variants, X**i, i: 1 <-> 4', fontsize=16)
    for i in range(1, d+1):
        plt.subplot(2,2,i)
        plt.title(f"X**{i}", fontsize=16)
        X_p = ml.polynomial_single(X, i)
        gradients = ml.calc_beta(X_p, y)
        Y = X_p.dot(gradients)
        plt.plot(X, y, c='r')
        plt.scatter(X, Y, c=dotcolor[i-1], s=16 )

def predict(X, y, year,  price, bought=1975, d=1):
    print(f">> TARGET YEAR (estimation): {year}\n   Initial price: {price/10**6} million kr  ({price})\n   Polynomial degree: {d}")
    year = np.array([year - bought])
    polynomial = ml.polynomial_single(X, d)
    gradients = ml.calc_beta(polynomial, y)
    p = ml.polynomial_single(year, d)
    pred_y = p.dot(gradients)[0] / 100
    pred_price = pred_y * price / 10**6
    print(f">> Predicted price: {round(pred_price, 4)} million kr\n   pred_y index = {round(pred_y, 2)}")
    print(f"   Price change = {round((pred_y-1), 2)}\n")


house_price = 2.3 * 10**6

#plot_original_data(X, y)
plot_poly_variants(X, y, 4)

flag = True
for k in range(1, 5):
    predict(X, y, 2022, price=house_price, bought=2015, d=k)

print('>> Is the answer realistic?\n   I\'d say it is realistic because the graph slope is increasing for each year and the two last',\
        'polynomial models estimated a price that was higher than the initial one')
plt.show()
