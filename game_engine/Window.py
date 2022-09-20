from pygame import display, Surface
from Color import *

# STANDARD VALUES
WIDTH = 1200
HEIGHT = 1024
FOV = 90.0
SCALE = 100
ZNEAR = 0.10
ZFAR = 1000.0
STEP = 0.10
TITLE = "lukkelele"

# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)

class Window:

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = display.set_mode((self.width, self.height))
        self.background = Surface((width, height))
        display.set_caption(self.title)

    def update(self):
        display.update()

    def clear(self):
        self.screen.fill((0,0,0))
        self.update()
