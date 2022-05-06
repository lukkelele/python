from matplotlib import pyplot as plt
import numpy as np


def prec_recall(x,y):
    return round((x/(x+y)), 3)

# pred is a predictability vector, y is 0/1 labels
def TP(pred, y):
    k = 0
    res = np.add(pred, y)
