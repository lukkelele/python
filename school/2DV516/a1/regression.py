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

def calc_euclidean_distance(z):
    z0 = float(z[0])
    z1 = float(z[1])
    distances = []
    for row in data:        # row[0] and row[1] --> x0 , y
        x = float(row[0])
        y = float(row[1])
        d = math.pow((z0 - x), 2) + math.pow((z1 - y), 2)
        distances.append([d, x, y])
    distances.sort()
    dist = np.array(distances)
    return dist

def plot_data(data_set, c):
    for point in data_set:
        x = float(point[0])
        y = float(point[1])
        p.scatter(x, y, color=c, s=3.5)

def plot_boundary(k, data_set):
    x_points = get_x_points()
    y_vals = []
    average_y_vals = []
    points = []
    knn_points = []
    for x in x_points:
        y = math_function(x)
        y_vals.append(y)    
        points.append([x, y])
    for point in points:
        y_sum = 0
        x = float(point[0])
        neighbors = get_neighbors(point, k, data_set)
        for neighbor in neighbors:
            y_sum += neighbor[2]   # y value 
        average_y = float(y_sum/k) # new y value
        knn_points.append([x, average_y])
        average_y_vals.append(average_y)
    p.plot(x_points, average_y_vals, color="r")
    return knn_points

# Return an array with a amount of equidistant x points
def get_x_points():
    x_points = np.arange(1, 25, 0.2)
    return x_points

def get_y_difference(z):
    x = float(z[0])
    y = float(z[1])
    predicted_y = math_function(x)
    diff = float(y - predicted_y)
    diff = math.pow(diff, 2)
    return diff

def get_neighbors(z, k, data_set):
    distances = calc_euclidean_distance(z)
    neighbors = []
    counter = 0
    while counter < k:
        neighbors.append(distances[counter])
        counter += 1
    return neighbors

def calc_mse(data_set, points):
    sum_diff = 0
    idx = 0
    len_points = len(data_set) + len(points) # all observations
    for z in data_set:
        diff = get_y_difference(z)
        sum_diff += diff
    for point in points: # the decision boundary plot with equidistant x's
        diff = get_y_difference(point)
        idx += 1
        sum_diff += diff
    sum_diff = float(sum_diff/len_points)
    return round(sum_diff, 3)

def simulate(data_set):
    print("\nStarting...")
    iterations = [1, 3, 5, 7]
    i = 1
    p.suptitle("knn regression")
    for k in iterations:
        print(f"-------------------\n| K == {k} |\n-------------------\n")
        ax = p.subplot(2,2,i)
        subplot = plot_boundary(k, data_set)
        mse = calc_mse(data_set, subplot)  # use in the plotting stage
        print(f"MSE: {mse}")
        ax.set_title(f"k == {k}\nMSE = {mse}")
        plot_data(data_set, "b")
        i += 1
        print("\n-------------------\n")
    p.subplots_adjust(wspace=0.6, hspace=0.6)
    p.show()

all_data = open_csv_file(csv_path)
data = all_data[0]
training_set = all_data[1]

simulate(data)
