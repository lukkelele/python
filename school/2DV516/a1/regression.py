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
            np_data = np.array(data)                
            return np.sort(np_data, axis=0)
    except: print("An error has occured!")


def calc_euclidean_distance(z):
    z0 = float(z[0])
    z1 = float(z[1])
    distances = []
    for row in data:        # row[0] and row[1] --> x0 , y
        x = float(row[0])
        y = float(row[1])
        d = math.pow((z0 - x), 2) + math.pow((z1 - y), 2)
        distances.append([d, x, y])
    dist = np.array(distances)
    dist = np.sort(dist, axis=0)
    return dist

def plot_data(data_set):
    for point in data_set:
        x = float(point[0])
        y = float(point[1])
        p.scatter(x, y, color="b", s=6)
    p.show()

def find_near_value(x, data_set):
    index = np.searchsorted(data_set[:, 0], x, side="left")
    print(f"index: {index}\ndata[index]: {data_set[index]}")

def get_near_values(x, k, data_set):
    test_set = calc_euclidean_distance(x)
    counter = 0
    while counter < k:
        index = np.searchsorted(test_set[:, counter], x, side="left")
        print(f"data: {test_set[index]}")
        counter += 1

# z is a point without y value
def get_neighbors(x, k, data_set):
    distances = calc_euclidean_distance([x, 0])
    neighbors = []
    counter = 0
    while counter < k:
        neighbors.append(distances[counter])
        counter += 1
    return neighbors

def get_y_value(z, k, data_set):
    neighbors = get_neighbors(z, k, data_set)
    y_sum = 0
    for neighbor in neighbors:
        y_val = neighbor[2]
        y_sum += y_val
    y = float(y_sum/k)
    return y

def plot_boundary(k, data_set):
    x_points = get_x_points(1)
    for x in x_points:
        y = get_y_value(x, k, data_set) 
        p.scatter(x, y, color="k", s=2)
    #p.show()

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
#plot_data(data)
#get_neighbors(2, 5, data)
#get_y_value(2, 5, data)
#find_near_value(11.09, data)
get_near_values([5.2,0], 3, data)
#plot_boundary(5, data)


