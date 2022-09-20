from pygame import draw as _draw
from Color import *
import numpy as np

EDGE_SIZE = 4

def draw_line(window, p1, p2, color=WHITE, draw_edge=False):
        _draw.line(window, color, p1, p2)
        if draw_edge: draw_edges([p1,p2], window, color, rad=EDGE_SIZE)

def draw_edge(window, v, color=WHITE, rad=4):
    _draw.circle(window, color, v, radius=rad)

def draw_edges(window, vertices, color=WHITE, rad=4):
    for vert in vertices:
        draw_edge(window, vert, color, rad)
        #draw.circle(window.screen, color, vert, radius=rad)

def line(p1, p2):
    """
    Calculate the line between p1 and p2
    Return the line with type float32
    """
    return np.array([p2[0]-p1[0], p2[1]-p1[1]], dtype=np.float32)

def normal(L1, L2):
    """
    Calculate the normal for the two lines L1 and L2
    """
    return np.cross(L1, L2)
