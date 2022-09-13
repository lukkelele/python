from mesh import Mesh, Triangle
from pygame.locals import *
import pygame, sys, os
import window
import time


class Engine:

    def __init__(self, width=500, height=500, title=""):
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.window = window.Window(width, height, title)

    def render(self):
        self.window.clear()

        self.window.update()

    def meshCube(self):
        vertices = [ 
                # South
                [(0,0,0), (0,1,0), (1,1,0)],
                [(0,0,0), (1,1,0), (1,0,0)],
                # East
                [(1,0,0), (1,1,0), (1,1,1)],
                [(1,0,0), (1,1,1), (1,0,1)],
                # North
                [(1,0,1), (1,1,1), (0,1,1)],
                [(1,0,1), (0,1,1), (0,0,1)],
                # West
                [(0,0,1), (0,1,1), (0,1,0)],
                [(0,0,1), (0,1,0), (0,0,0)],
                # Top
                [(0,1,0), (0,1,1), (1,1,1)],
                [(0,1,0), (1,1,1), (1,1,0)],
                # Bottom
                [(1,0,1), (0,0,1), (0,0,0)],
                [(1,0,1), (0,0,0), (1,0,0)],
            ]
        return vertices



e = Engine()
while True:

    e.fpsClock.tick(30)






