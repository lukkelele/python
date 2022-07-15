import numpy as np
import csv


def open_csv_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: 
                row = row[0].split('\t')
                X.append([row[0], row[1], row[2]])
            return np.array(X, dtype=float)
    except: print("An error has occured!")

# For opening and reading GPUbenchmark.csv
def open_gpu_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: 
                X.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
            return np.array(X, dtype=float)
    except: print("An error has occured!")

def open_house_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: 
                X.append([row[0], row[1]])
            return np.array(X, dtype=float)
    except: print("An error has occured!")

def open_admission_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: 
                X.append([row[0], row[1], row[2]])
            return np.array(X, dtype=float)
    except: print("An error has occured!")

def open_cancer_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: 
                X.append([row[0],row[1],row[2],row[3],
                          row[4],row[5],row[6],row[7],
                          row[8],row[9]])
            return np.array(X, dtype=float) # dtype=int ?
    except: print("An error has occured!")

def open_microships_file(path):
    try:
        with open(path) as csv_data:
            r = csv.reader(csv_data)
            X = []
            for row in r: 
                X.append([row[0], row[1], row[2]])
            return np.array(X, dtype=float)
    except: print("An error has occured!")

