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


    def render_timeSymbol(self):
        self.window.clear()
        scale = 3
        p1, p2, p3, p4 = (50*scale,50*scale), (100*scale,50*scale), (50*scale,100*scale), (100*scale,100*scale)
        pygame.draw.line(self.window.screen, (255,255,0), p1, p2, 3)
        pygame.draw.line(self.window.screen, (0,255,0), p2, p3, 3)
        pygame.draw.line(self.window.screen, (255,0,0), p3, p4, 3)
        pygame.draw.line(self.window.screen, (255,0,255), p4, p1, 3)
        self.window.update()

    def render_triangle(self):
        self.window.clear()
        s = 50  # scaler
        d = 100
        p1, p2, p3 = (0+d,0+d), (0+d, 1*s + d), (1*s + d,1*s + d)
        pygame.draw.line(self.window.screen, (255,255,0), p1, p2, 3)
        pygame.draw.line(self.window.screen, (0,255,0), p2, p3, 3)
        pygame.draw.line(self.window.screen, (255,0,0), p3, p1, 3)
        self.window.update()



e = Engine()
rect = pygame.Rect(50, 100, 100, 50)
while True:

    pygame.draw.rect(e.window.screen, (255,255,0), rect)
    e.window.update()
    #e.render_triangle()
    e.fpsClock.tick(30)






