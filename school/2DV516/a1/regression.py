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
    for x in x_points:
        y = math_function(x)
        y_vals.append(y)    
        points.append([x, y])
    for point in points:
        y_sum = 0
        neighbors = get_neighbors(point, k, data_set)
        for neighbor in neighbors:
            y_sum += neighbor[2]   # y value 
        average_y = float(y_sum/k) # new y value
        average_y_vals.append(average_y)
    return [x_points, average_y_vals]

# Return an array with a amount of equidistant x points
def get_x_points():
    x_points = np.arange(1, 25, 0.2)
    return x_points

def calc_mse(k, data_set):
    sum_diff = 0
    for z in data_set:
        x = float(z[0])
        y = float(z[1])
        predicted_y = math_function(x)
        print(f"x: {x}\ny: {y}\npredicted_y: {predicted_y}\n")
        diff = float(y - predicted_y)
        diff = math.pow(diff, 2)
        sum_diff += diff
    print(f"sum_diff: {sum_diff}")

def get_neighbors(z, k, data_set):
    distances = calc_euclidean_distance(z)
    neighbors = []
    counter = 0
    while counter < k:
        neighbors.append(distances[counter])
        counter += 1
    return neighbors

def simulate(data_set):
    print("\nStarting...")
    iterations = [1, 3, 5, 7]
    i = 1
    p.suptitle("knn regression")
    for k in iterations:
        print(f"-------------------\n| K == {k} |\n-------------------\n")
        p.subplot(2,2,i)
        subplot = plot_boundary(k, data_set)
        plot_data(data_set, "b")
        p.title = f"k == {k}"
        p.plot(subplot[0], subplot[1], color="r")
        i += 1
        print("\n-------------------\n")
    p.show()
    print(f"\nSimulation done!\n")

all_data = open_csv_file(csv_path)
data = all_data[0]
training_set = all_data[1]

simulate(data)
