from matplotlib import pyplot as p
import numpy as np
import csv
import math


csv_path = "./A1_datasets/polynomial200.csv"


# Open a csv file and read the data in to the list 'data'
def open_csv_file(path):
    try:
        with open(path) as csv_data:
            data = []
            r = csv.reader(csv_data)
            for row in r:
                data.append([row[0], row[1]])
            return np.array(data)                
    except: print("An error has occured!")


def calc_euclidean_distance(z):
    z0 = float(z[0])
    z1 = float(z[1])
    distances = []
    for row in data:        # row[0] and row[1] --> x0 , y
        x = float(row[0])
        y = float(row[1])
        d = math.pow((z0 - x, 2)) + math.pow((z1 - y, 2))
        distances.append([d, x, y])
    distances.sort()
    return distances

# Get average y val for a point z with k neighbors
def get_average(z, k):
    i = 0
    s = 0 # sum for likelyhood of OK or FAIL
    d = calc_euclidean_distance(z)
    while i < k:
        s += int(d[i][2])   # d[i][2] equals y value for each datapoint
        i += 1
    average = s/k   # divide the sum with the amount of neighbors
    return average

def plot_point(x, k):
    y = get_average(x, k)
    p.plot(x, y)

# Return an array with a amount of equidistant x points
def get_x_points(a):
    maximum = a


data = open_csv_file(csv_path)
