from matplotlib import pyplot as plt
import numpy as np


def prec_recall(x,y):
    return round((x/(x+y)), 3)
