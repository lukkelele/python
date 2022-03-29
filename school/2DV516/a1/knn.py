import csv
import numpy as np
from matplotlib import pyplot as p


# Calculate distance for x
# Sort the distance starting with the lowest values
# Select k rows 
# Calculate the mean

chip1 = [-0.3, 1]
chip2 = [-0.5, -0.1]
chip3 = [0.6, 0]

# PLOT THE ORIGINAL DATA
x_values = []
x_negative_values = []

y_values = []
y_negative_values = []

z_values = []
z_negative_values = []


with open('./A1_datasets/microchips.csv') as csv_data:
    r = csv.reader(csv_data)
    for row in r:
        x_val = float(row[0])
        y_val = float(row[1])
        z_val = row[2]
        x_values.append(x_val) if x_val > 0 else x_negative_values.append(x_val)  # Fixed sorting
        y_values.append(y_val) if y_val > 0 else y_negative_values.append(y_val)
        


x_values.sort()
x_negative_values.sort(reverse=False)
y_values.sort()
y_negative_values.sort(reverse=False)

# Feature vectors sorted
X = x_negative_values + x_values
Y = y_negative_values + y_values
XY = []

for x in X:
    xy = {x, Y[X.index(x)]}
    XY.append(xy)

print(XY)
