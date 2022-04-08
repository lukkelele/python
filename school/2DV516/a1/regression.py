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
        y = calculate_y(x, data_set, k)
        print(f"x: {x}\ny: {y}")
        p.scatter(x, y, color="k", s=2)


def calculate_y(x, data_set, k):
    x_vals = find_close_x_values(x, data_set, k)
    y_sum = 0
    len_x_vals = len(x_vals)
    for x_val in x_vals:
        if x_val[0] != x:
            y_sum += x_val[1]
            #print(f"y_sum: {y_sum}\nx_vals = {x_vals[1]}")
    if len_x_vals == 0: len_x_vals = 1 
    average_y = float(y_sum / len_x_vals)
    #print(f"average_y: {average_y}")
    return average_y

def find_close_x_values(x, data_set, k):
    data_set = np.sort(data_set, axis=0)
    index_reduction = math.floor(k/2)
    x_index = 0
    x_vals = []
    for val in data_set:
        x_vals.append(val)
    #X = np.abs(data_set - x)
    idx = (np.abs(data_set-x)).argmin()
    #idx = np.where(X == X.min())
    x_index = idx
    print(x_index)
    start = x_index - index_reduction
    stop = x_index + index_reduction + 1
    while stop > len(data_set):
        stop -= 1
    x_vals = x_vals[start:stop]
    return x_vals

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
    x_points = np.arange(minimum, maximum, 2)
    return x_points

def simulate(data_set, k):
    print(f"Starting simulation!")
    plot_data(data_set)
    plot_boundary(k, data_set)    

    p.show()

all_data = open_csv_file(csv_path)
data = all_data[0]
training_set = all_data[1]

simulate(data, 3)

#print(calculate_y(12.6806, data, 5))



