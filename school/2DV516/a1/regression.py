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
    #print(f"y1 = {y}\ny2 = {calculated_y}\n")
    return y == calculated_y 

def calc_error_rate(data_set):
    errors = 0
    for point in data_set:
        if validate_point(point) == False:
            errors += 1
    return errors 

def plot_data(data_set, c):
    for point in data_set:
        x = float(point[0])
        y = float(point[1])
        p.scatter(x, y, color=c, s=6)

def plot_boundary(k, data_set):
    x_points = get_x_points()
    y_vals = []
    for x in x_points:
        y = math_function(x)
        y_vals.append(y)    
    p.plot(x_points, y_vals, color="r")

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

def get_neighbors(z, k, data_set):
    distances = calc_euclidean_distance(z)
    neighbors = []
    counter = 0
    while counter < k:
        neighbors.append(distances[counter])
        counter += 1
    return neighbors


# Return an array with a amount of equidistant x points
def get_x_points():
    x_points = np.arange(1, 25, 0.2)
    return x_points


all_data = open_csv_file(csv_path)
data = all_data[0]
training_set = all_data[1]


plot_data(data, "b")
#plot_data(training_set, "k")
plot_boundary(3, data)
p.show()
