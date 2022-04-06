from matplotlib import pyplot as p
import math
import csv
import numpy as np


csv_path = "./A1_datasets/microchips.csv"

values = []
simulation_k = [1, 3, 5, 7]  # k's to be used when simulating

chip1 = [-0.3, 1]
chip2 = [-0.5, -0.1]
chip3 = [0.6, 0]
chips = []
test_chips = [chip1, chip2, chip3]
chips_result = []

# Open a csv file and read the data in to the list 'values'
def open_csv_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            for row in r:
                # row[0] == x0_val  | row[1] == x1_val  | row[2] == y_val
            #    print(row)
                values.append([row[0], row[1], row[2]]) 
    except: print("An error has occured!")

# Calc distance between point z and ALL other points in the data set
# Returns a list with distance for each calculated point
def calc_euclidean_distance(z):
    z0 = float(z[0])
    z1 = float(z[1])
    distances = []
    for row in values:        # row[0] and row[1] --> x0 , x1
        d = math.pow((z0 - float(row[0])), 2) + math.pow((z1 - float(row[1])), 2)
        distances.append([d, row[0], row[1], row[2]])
    # All distances calculated
    distances.sort()
    return distances

# z is the point, k is the number of neighbors
# Returns 0 or 1 depending on the outcome of the known neighbors
def find_neighbors(z, k):
    i = 0
    s = 0 # sum for likelyhood of OK or FAIL
    d = calc_euclidean_distance(z)
    while i < k:
        s += int(d[i][3])
        i += 1
    if k == 1:
        if s == 1: return 1
        else: return 0
    elif k == 3:
        if s > 1: return 1
        else: return 0
    elif k == 5:
        if s > 2: return 1
        else: return 0
    elif k == 7:
        if s > 3: return 1
        else: return 0

# Print the result for point z with k neighbors and the sum s
def process_point(z, k, s):
    if s == 1:
        print(f"{z} ==> OK")
        chips_result.append([z, 1]) 
    else:
        print(f"{z} ==> Fail")
        chips_result.append([z, 0]) 

def training_errors(k):
    errors = 0
    for point in values:
        r = int(point[2])       # 0 or 1
        n = find_neighbors(point, k)
        if r != n: errors += 1
    print(f"Total number of training errors when k={k}: {errors}")


# TODO: get rid of counters and make use of numpy
def draw_grid(i):
    chips.clear()
    xx, yy = np.meshgrid(np.arange(-2, 2, 0.1),
                         np.arange(-2, 2, 0.1)) 
    x_counter = 0
    counter = 0
    x_index = 0
    y_index = 0
    while x_counter < 40:
        counter = 0
        while counter < 40:
            chips.append([xx[0, x_index], yy[y_index, 0]])
            counter += 1
            y_index += 1
        y_index = 0
        x_index += 1
        x_counter += 1
    for chip in chips:
        result = find_neighbors(chip, i)
        if result == 0: p.scatter(float(chip[0]), float(chip[1]), color="r", alpha=0.15)
        elif result == 1: p.scatter(float(chip[0]), float(chip[1]), color="g", alpha=0.15)


def base_plot():
    for vals in values:
        point_color = ""
        if int(vals[2]) == 0:
            point_color = "r"
        elif int(vals[2]) == 1:
            point_color = "g"
        p.scatter(float(vals[0]), float(vals[1]), color=point_color)


# Run simulation with the list k that hold amount of neighbors per test
def simulate(k):
    index_count = 1
    flag = True
    p.subplots(2,2)
    p.suptitle("knn testing")
    try:
        open_csv_file(csv_path)
    except: flag = False  # if any error has occured with opening the file, dont start testing
    for n in k: # Iterate the list k to make sure no even numbers are chosen as neighbor values
        if n % 2 == 0:  # if even number
            print("Even numbers are not allowed to use as k!")
            flag = False
    if flag == True:
        for i in k: # iterate list k
            print(f"\n-----------------\n| RUNNING k = {i} |\n-----------------")
            training_errors(i)
            draw_grid(i)
            base_plot()
            p.title(f"k == {i}")
            for chip in test_chips:
                s = find_neighbors(chip, i)
                process_point(chip, i, s)
            for chip in chips_result:
                if int(chip[1]) == 0:   # chip[0][0] == x0 , chip[0][1] == x1
                    p.scatter(float(chip[0][0]), float(chip[0][1]), color="r", marker='X')
                elif int(chip[1]) == 1:
                    p.scatter(float(chip[0][0]), float(chip[0][1]), color="g", marker='X')
            p.subplot(2, 2, index_count)
            index_count += 1


simulate(simulation_k)
p.subplots_adjust(wspace=0.4, hspace=0.4)
p.show()
