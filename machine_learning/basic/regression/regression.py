from matplotlib import pyplot as p
import numpy as np
import csv
import math
import random

csv_path = "../datasets/polynomial200.csv"


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

# Finds closest x values in the data set for a provided x
def find_closest_x(x, data_set, k):
    x_values = np.copy(data_set[:, 0])
    close_x = []
    i = 0
    while i < k:
        absolute_val = np.abs(x_values - x)
        idx = absolute_val.argmin()
        x_values = np.delete(x_values, idx, axis=None)
        close_x.append(idx) # add the indexes for the closest x values
        i += 1
    return close_x

def calc_y_value(x, data_set, k):
    x_idx = find_closest_x(x, data_set, k)  # close x indexes
    y_values = np.take(data_set[:,1], x_idx) # get all y values with the indexes of the close x values
    average_y = float(sum(y_values)/k)  # average y value of neighbor points 
    return average_y

def plot_data(data_set, c):
    for point in data_set:
        x = float(point[0])
        y = float(point[1])
        p.scatter(x, y, color=c, s=3.5)

def plot_boundary(data_set, k):
    x_points = get_x_points()
    y_vals = []
    for x in x_points:
        y = calc_y_value(x, data_set, k)
        y_vals.append(y)    
    p.plot(x_points, y_vals, color="r")

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

def calc_mse(data_set):
    sum_diff = 0
    len_points = len(data_set)
    for z in data_set:
        diff = get_y_difference(z)
        sum_diff += diff
    sum_diff = float(sum_diff/len_points)
    print(f"Observations: {len_points}")
    return round(sum_diff, 3)

def calc_error_rate(data_set, k):
    mse = calc_mse(data_set)
    return mse 

def simulate_training(data_set):
    print("\nStarting test simulation...")
    iterations = [1, 3, 5, 7]
    i = 1
    for k in iterations:
        print(f"\n==== TRAINING SET\n-------------------\n| K == {k} |\n-------------------")
        mse = calc_error_rate(data_set, k)
        print(f"MSE = {mse}\n-------------------\n")
        i += 1
    print("===================================================\n") 

def simulate(data_set, training_set):
    print("\nStarting...")
    simulate_training(training_set)
    iterations = [1, 3, 5, 7]
    i = 1
    p.suptitle("knn regression")
    for k in iterations:
        print(f"-------------------\n| K == {k} |\n-------------------")
        ax = p.subplot(2,2,i)
        plot_boundary(data_set, k)
        mse = calc_error_rate(data_set, k)
        ax.set_title(f"k == {k}\nMSE = {mse}")
        plot_data(data_set, "b")
        i += 1
        print(f"MSE = {mse}\n-------------------\n")
    p.subplots_adjust(wspace=0.6, hspace=0.6)
    p.show()


all_data = open_csv_file(csv_path)
data = all_data[0]
training_set = all_data[1]

simulate(data, training_set)
#print(calc_y_value(1.3, data, 1))
#calc_y_value(3.6, data, 3)




