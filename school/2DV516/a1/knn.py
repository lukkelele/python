from matplotlib import pyplot as p
import math
import csv
import numpy as np

# Calculate distance for x
# Sort the distance starting with the lowest values
# Select k rows 
# Calculate the mean

# PLOT THE ORIGINAL DATA
values = []
y_values = []

chip1 = [-0.3, 1]
chip2 = [-0.5, -0.1]
chip3 = [0.6, 0]


# Calc distance between point z and ALL other points in the data set
def calc_euclidean_distance(z):
    z0 = z[0]
    z1 = z[1]
    distances = []
    for row in values:        # row[0] and row[1] --> x0 , x1
        d = math.pow((z0 - float(row[1])), 2) + math.pow((z1 - float(row[1])), 2)
        distances.append([d, row[0], row[1], row[2]])
    # All distances calculated
    distances.sort()
    return distances


# z is the point, k is the number of neighbors
def find_neighbors(z, k):
    i = 0
    neighbors = []
    d = calc_euclidean_distance(z)
    while i < k:
        neighbors.append(d[i])
        i += 1
    print("\nNeighbors found!\n")
    for n in neighbors:
        print(n)
    print()
    return neighbors



def get_point_y(z, k):
    # Get neighbors
    n = find_neighbors(z, k)



with open('./A1_datasets/microchips.csv') as csv_data:
    r = csv.reader(csv_data)
    for row in r:
        # row[0] == x0_val  | row[1] == x1_val  | row[2] == y_val
        values.append([row[0], row[1], row[2]]) 


find_neighbors(chip1, 3)
