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

poly = ml.polynomial(X[:,1], 3)

print(poly)

