from pygame.locals import *
from pygame.key import *
from math import sin, cos, sqrt
import pygame, sys, os
import numpy as np
import pywavefront
import window
import time
import mesh as _mesh

WIDTH, HEIGHT = 500, 500
BLACK, WHITE = (0,0,0), (255,255,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
RED = (255,0,0)



class Engine:


    def __init__(self, width=500, height=500, title=""):
        self.pg = pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.window = window.Window(width, height, title)
        self.angle = 0
        self.proj_mat = np.matrix([
            [1,0,0],
            [0,1,0]
        ])
        self.mesh = _mesh.Mesh()
        self.WHITE = (255,255,255) # TODO: Add color class / enums
        self.BLACK = (0,0,0)

    def clearScreen(self):
        self.window.clear()
        self.window.update()

    def quit(self):
        pygame.quit()
        exit()

    def drawTriangle(self, vertices, color=WHITE, edges=False):
        "Three vertices"
        vec1, vec2, vec3 = vertices[0], vertices[1], vertices[2]
        pygame.draw.line(self.window.screen, self.WHITE, vec1, vec2)
        pygame.draw.line(self.window.screen, self.WHITE, vec1, vec3)
        pygame.draw.line(self.window.screen, self.WHITE, vec2, vec3)
        if edges: self.drawEdges(vertices)

    def drawEdges(self, vertices, color=WHITE, rad=4):
        vec1, vec2, vec3 = vertices[0], vertices[1], vertices[2]
        pygame.draw.circle(self.window.screen, color, vec1, radius=rad)
        pygame.draw.circle(self.window.screen, color, vec2, radius=rad)
        pygame.draw.circle(self.window.screen, color, vec3, radius=rad)

    def importObject(self, path_to_object):
        scene = pywavefront.Wavefront(path_to_object, collect_faces=True)
        return scene.vertices

e = Engine()
e.window.screen.fill((0,0,0)) # blackscreen
background = pygame.Surface((WIDTH, HEIGHT))
cube = e.mesh.createCube()
ship = [e.importObject('./ship.obj')]
e.clearScreen()
print(ship)
print('\n')
print(cube)
objmodel = cube
projected_points = [
        [n,n] for n in range(len(objmodel))
    ]

#for tri in cube: for vertex in tri: pygame.draw.line()
angle=0
x_angle, y_angle, z_angle = 0, 0, 0
scale = 80
circle_pos = [WIDTH/2, HEIGHT/2]
while True:
    e.window.screen.blit(background, (0,0)) # TODO: fix refresh for screen
    for event in pygame.event.get():
        if event.type == QUIT:
            e.quit()

    if pygame.key.get_pressed()[K_RIGHT]:
        y_angle += 0.1
    elif pygame.key.get_pressed()[K_LEFT]:
        y_angle -= 0.1
    elif pygame.key.get_pressed()[K_UP]:
        z_angle -= 0.1
    elif pygame.key.get_pressed()[K_DOWN]:
        z_angle += 0.1

    projected_points = []
    for tri in objmodel:
        proj_points = [] 
        line1 = np.subtract(tri[1], tri[0])
        line2 = np.subtract(tri[2], tri[0])

        for vert in tri:
            vert = np.array(vert)   # FIXME
            rotation2d_z = np.dot(e.mesh.rotation_z(z_angle), vert.reshape(3,1))
            rotation2d_y  = np.dot(e.mesh.rotation_y(y_angle), rotation2d_z)
            rotation2d_x = np.dot(e.mesh.rotation_x(x_angle), rotation2d_y)
            projection2d = np.dot(e.proj_mat, rotation2d_x)
            x = int(projection2d[0][0] * scale + circle_pos[0]) # circle_pos -> OFFSET
            y = int(projection2d[1][0] * scale + circle_pos[1]) #               offset
            #if norm_x * rotation2d_x[0] + norm_y * rotation2d_x[1] + norm_z * rotation2d_x[2] > 0:
            #pygame.draw.circle(e.window.screen, (255,0,100), (x,y), 3)
            proj_points.append([x,y])
        l1 = np.array(proj_points[2]) - np.array(proj_points[0])
        l2 = np.array(proj_points[1]) - np.array(proj_points[0])
        norm_d = np.cross(l1, l2)
        if norm_d > 0:
            e.drawTriangle(proj_points, e.window.screen, edges=True)

    
    angle+=0.02

    # Update screen
    e.fpsClock.tick(30)
    e.window.update()




