from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

# The 7th column is the response y
# Find f(X) = B0 + B1*X1 + ... + B6*X6

csv_path = "./data/GPUbenchmark.csv"

