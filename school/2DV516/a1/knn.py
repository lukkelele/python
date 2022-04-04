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
simulation_k = [1, 3, 5, 7]  # k's to be used when simulating

chip1 = [-0.3, 1]
chip2 = [-0.5, -0.1]
chip3 = [0.6, 0]
chips = [chip1, chip2, chip3]


# Calc distance between point z and ALL other points in the data set
# Returns a list with distance for each calculated point
def calc_euclidean_distance(z):
    z0 = z[0]
    z1 = z[1]
    distances = []
    for row in values:        # row[0] and row[1] --> x0 , x1
        d = math.pow((z0 - float(row[1])), 2) + math.pow((z1 - float(row[1])), 2)
        #print(f"d = {d}")
        distances.append([d, row[0], row[1], row[2]])
    # All distances calculated
    distances.sort()
    return distances


# z is the point, k is the number of neighbors
# Returns a list of k number of neighbors of point z
def find_neighbors(z, k):
    i = 0
    s = 0 # sum for likelyhood of OK or FAIL
    neighbors = []
    d = calc_euclidean_distance(z)
    while i < k:
        neighbors.append(d[i])
        i += 1
    for n in neighbors:
        s += int(n[3])
    if s > 1: print(f"{z} ==> OK")
    else: print(f"{z} ==> Fail")
    return neighbors


def simulate(k):
    flag = True
    for n in k:
        # Check the provided list of k's
        if n % 2 == 0:
            print("Even numbers are not allowed to use as k!")
            flag = False
    if flag == True:
        for i in k: # iterate list k
            print(f"\n--------------\n| RUNNING k = {i} |")
            for chip in chips:
                find_neighbors(chip, i)
            print(f"--------------")


with open('./A1_datasets/microchips.csv') as csv_data:
    r = csv.reader(csv_data)
    for row in r:
        # row[0] == x0_val  | row[1] == x1_val  | row[2] == y_val
        values.append([row[0], row[1], row[2]]) 


#find_neighbors(chip1, 3)


simulate(simulation_k)



