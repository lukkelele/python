from matplotlib import pyplot as p
import math
import csv
import numpy as np


# Calculate distance for x
# Sort the distance starting with the lowest values
# Select k rows 
# Calculate the mean

# PLOT THE ORIGINAL DATA
csv_path = "./A1_datasets/microchips.csv"

values = []
x_axis = []
y_axis = []
simulation_k = [1, 3, 5, 7]  # k's to be used when simulating

chip1 = [-0.3, 1]
chip2 = [-0.5, -0.1]
chip3 = [0.6, 0]
chips = [chip1, chip2, chip3]
chips_result = []


# Open a csv file and read the data in to the list 'values'
def open_csv_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            for row in r:
                # row[0] == x0_val  | row[1] == x1_val  | row[2] == y_val
                print(row)
                values.append([row[0], row[1], row[2]]) 
    except: print("An error has occured!")

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
    print_result(z, k, s)
    return neighbors



# Print the result for point z with k neighbors and the sum s
def print_result(z, k, s):
    if k == 1:
        if s == 1:
            print(f"{z} ==> OK")
            chips_result.append([z, 1]) 
        else:
            print(f"{z} ==> Fail")
            chips_result.append([z, 0]) 
    elif k == 3:
        if s > 1:
            print(f"{z} ==> OK")
            chips_result.append([z, 1]) 
        else:
            print(f"{z} ==> Fail")
            chips_result.append([z, 0]) 
    elif k == 5:
        if s > 2:
            print(f"{z} ==> OK")
            chips_result.append([z, 1]) 
        else:
            print(f"{z} ==> Fail")
            chips_result.append([z, 0]) 
    elif k == 7:
        if s > 3:
            print(f"{z} ==> OK")
            chips_result.append([z, 1]) 
        else:
            print(f"{z} ==> Fail")
            chips_result.append([z, 0]) 
    else:
        print("The number could not be run as a value of neighbors.\n"+
              "Make sure the numbers are odd.")

def base_plot():
    x_vals = []
    y_vals = []
    for vals in values:
        point_color = ""
        if int(vals[2]) == 0: point_color = "r"
        elif int(vals[2]) == 1: point_color = "g"
        x_vals.append(float(vals[0]))
        y_vals.append(float(vals[1]))
        p.scatter(float(vals[0]), float(vals[1]), color=point_color)



# Run simulation with the list k that hold amount of neighbors per test
def simulate(k):
    flag = True
    p.suptitle("knn testing")
    try:
        open_csv_file(csv_path)
    except: flag = False  # if any error has occured with opening the file, dont start testing
    for n in k: # Iterate the list k to make sure no even numbers are chosen as neighbor values
        if n % 2 == 0:  # if even number
            print("Even numbers are not allowed to use as k!")
            flag = False
    if flag == True:
        index_count = 0
        for i in k: # iterate list k
            print(k)
            index_count += 1
            print(f"\n-----------------\n| RUNNING k = {i} |\n-----------------")
            base_plot()
            for chip in chips:
                find_neighbors(chip, i)
            for chip in chips_result:
                print(f"chip_result -> {chip}  |  s == {chip[1]}")
                if int(chip[1]) == 0: p.scatter(float(chip[0][0]), float(chip[0][1]), color="b")
                elif int(chip[1]) == 1: p.scatter(float(chip[0][0]), float(chip[0][1]), color="c")
            p.subplot(2, 2, index_count)
            p.title(f"k == {i}")
            
# chips_result holds a list of three items per k.
# index 0 holds k = 1, index 1 holds k = 3 etc.
# index 3 --> k = 7


simulate(simulation_k)
p.subplots_adjust(wspace=0.4, hspace=0.4)
p.show()



