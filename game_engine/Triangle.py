from pygame import draw as _draw
from Line import draw_edges
from Color import *
import numpy as np
import Transform


def get_points(triangle):
    p1 = triangle[0]
    p2 = triangle[1]
    p3 = triangle[2]
    return p1, p2, p3

def draw(window, triangle, linecolor=WHITE, edgecolor=GREEN, with_edges=False):
    p1, p2, p3 = get_points(triangle)
    _draw.line(window, linecolor, p1, p2)
    _draw.line(window, linecolor, p1, p3)
    _draw.line(window, linecolor, p2, p3)
    if with_edges:
        draw_edges(window, triangle, edgecolor)

def transform(triangle, matWorld, matCam):
    p1, p2, p3 = triangle[0], triangle[1], triangle[2]

    p1 = Transform.extend_vector_ones(p1)
    p2 = Transform.extend_vector_ones(p2)
    p3 = Transform.extend_vector_ones(p3)
    # World Transformation
    p1t, p2t, p3t = Transform.matrix_multiply_vector(matWorld, p1), \
                    Transform.matrix_multiply_vector(matWorld, p2), \
                    Transform.matrix_multiply_vector(matWorld, p3)
    # Camera Transformation
    p1v, p2v, p3v = Transform.matrix_multiply_vector(matCam, p1t), \
                    Transform.matrix_multiply_vector(matCam, p2t), \
                    Transform.matrix_multiply_vector(matCam, p3t)

    return [p1v, p2v, p3v]