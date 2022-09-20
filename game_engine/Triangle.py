from pygame import draw as _draw
from Line import draw_edges
from Color import *
import numpy as np


def get_points(triangle):
    p1 = triangle[0]
    p2 = triangle[1]
    p3 = triangle[2]
    return p1, p2, p3

def draw(window, triangle, color=WHITE, with_edges=False):
    p1, p2, p3 = get_points(triangle)
    _draw.line(window, color, p1, p2)
    _draw.line(window, color, p1, p3)
    _draw.line(window, color, p2, p3)
    if with_edges:
        draw_edges(window, triangle, color)

