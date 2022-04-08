from matplotlib import pyplot as p
import numpy as np
import csv
import math
import random

csv_path = "./A1_datasets/polynomial200.csv"

global training_set
global data
global distances


# Open a csv file and read the data in to the list 'data'
def open_csv_file(path):
    try:
        with open(path) as csv_data:
            data = []
            training = []
            r = csv.reader(csv_data)
            count = 0
            for row in r:
                x = float(row[0])
                y = float(row[1])
                if count < 100: data.append([x, y])
                else: training.append([x, y])
                count += 1
            np_data = np.array(data)                
            training_set = np.array(training)
            return [np_data, training_set]
    except: print("An error has occured!")


def math_function(x):
    # f(x) = 5 + 12x - x^2 + 0,025x^3 + normrnd(0,5)
    y = 5 + 12*x - math.pow(x, 2) + 0.025*math.pow(x, 3) + np.random.normal(0.5)
    return y

# Point z --> (x, y)
# Used for error checking
def validate_point(z):
    x = round(float(z[0]), 2)
    y = round(float(z[1]), 2)
    calculated_y = round(math_function(x), 2)
    print(f"y1 = {y}\ny2 = {calculated_y}\n")
    return y == calculated_y 

def calc_error_rate(data_set):
    errors = 0
    for point in data_set:
        if validate_point(point) == False:
            errors += 1
    return errors 

def plot_data(data_set):
    for point in data_set:
        x = float(point[0])
        y = float(point[1])
        p.scatter(x, y, color="b", s=6)
    p.show()

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


def get_near_values(x, k, data_set):
    y_sum = 0
    counter = 0
    index = 0
    index = np.searchsorted(data_set[:, 0], x, side="left")
    while counter < k:
        y_sum += data_set[index][1]
        counter += 1
        index += 1
    average = y_sum/k
    print(f"average ==> {average}")
    return average
    

def get_neighbors(z, k, data_set):
    distances = calc_euclidean_distance(z)
    neighbors = []
    counter = 0
    while counter < k:
        neighbors.append(distances[counter])
        counter += 1
    return neighbors

def plot_boundary(k, data_set):
    x_points = get_x_points(1)
    for x in x_points:
        y = math_function(x)
        p.scatter(x, y, color="k", s=2)
    p.show()


def find_close_x_values(x, data_set, k):
    data_set = np.sort(data_set, axis=0)
    index_reduction = math.floor(k/2)
    x_vals = []
    for val in data_set:
        x_vals.append(val[0]) # val[0] == x
        print(val[0])
    x_index = x_vals.index(x)
    print(x_index-index_reduction)
    start = x_index - index_reduction
    stop = x_index + index_reduction + 1
    while stop > len(data_set):
        stop -= 1
    x_vals = x_vals[start:stop]
    print(x_vals)

# Return an array with a amount of equidistant x points
def get_x_points(a):
    np_maximum = np.max(data, axis=0) 
    np_minimum = np.min(data, axis=0)
    print(f"maximum val ==> {np_maximum}")
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



all_data = open_csv_file(csv_path)
data = all_data[0]
training_set = all_data[1]


find_close_x_values(24.51496, data, 5)




