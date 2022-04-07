from matplotlib import pyplot as p
import numpy as np
import csv
import math

csv_path = "./A1_datasets/polynomial200.csv"

global data

# Open a csv file and read the data in to the list 'data'
def open_csv_file(path):
    try:
        with open(path) as csv_data:
            data = []
            r = csv.reader(csv_data)
            for row in r:
                data.append([float(row[0]), float(row[1])])
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

def plot_data(data_set):
    for point in data_set:
        x = float(point[0])
        y = float(point[1])
        p.scatter(x, y, color="b", s=6)
    p.show()


# Get average y val for a point z with k neighbors
def get_average(z, k):
    i = 0
    s = 0 
    d = calc_euclidean_distance(z)
    while i < k:
        s += int(d[i][2])   # d[i][2] equals y value for each datapoint
        i += 1
    average = s/k   # divide the sum with the amount of neighbors
    return average

def plot_point(x, k):
    y = get_average(x, k)
    p.plot(x, y, color="r")

# Return an array with a amount of equidistant x points
def get_x_points(a):
    np_maximum = np.max(data, axis=0) 
    np_minimum = np.min(data, axis=0)
    maximum = 0
    minimum = 100
    for val in np_maximum:
        if val > maximum:
            maximum = val
    for val in np_minimum:
        if val < minimum:
            minimum = val
    x_points = np.arange(minimum, maximum, 0.5)
    return x_points



data = open_csv_file(csv_path)
plot_data(data)




