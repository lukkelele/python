from pygame.locals import *
from pygame.key import *
from math import sin, cos, sqrt
import pygame, sys, os
import numpy as np
import window
import time
import mesh as _mesh

WIDTH, HEIGHT = 500, 500


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

    def clearScreen(self):
        self.window.clear()
        self.window.update()

    def quit(self):
        pygame.quit()
        exit()


e = Engine()
e.window.screen.fill((0,0,0)) # blackscreen
background = pygame.Surface((WIDTH, HEIGHT))
cube = e.mesh.createCube()
e.clearScreen()
projected_points = [
        [n,n] for n in range(len(cube))
    ]

#for tri in cube: for vertex in tri: pygame.draw.line()
angle=0
x_angle, y_angle, z_angle = 0, 0, 0
scale = 100
circle_pos = [WIDTH/2, HEIGHT/2]
keys = [K_RIGHT, K_LEFT]
while True:
    e.window.screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            e.quit()
    
    if pygame.key.get_pressed()[K_RIGHT]:
        #angle += 0.1
        z_angle += 0.1
    elif pygame.key.get_pressed()[K_LEFT]:
        #angle -= 0.1
        z_angle -= 0.1

    projected_points = []
    for tri in cube:
        proj_points = [] 
        line1 = np.subtract(tri[1], tri[0])
        line2 = np.subtract(tri[2], tri[0])
        norm_x = np.subtract(line1[1] * line2[2], line1[2] * line2[1])
        norm_y = np.subtract(line1[2] * line2[0], line1[0] * line2[2])
        norm_z = np.subtract(line1[0] * line2[1], line1[1] * line2[0])
        rotation2d_x, rotation2d_y, rotation2d_z = 0, 0, 0

        #print(f"Norm vals:\n{norm_x}\n{norm_y}\n{norm_z}\n")
        for vert in tri:
            vert = np.array(vert)   # FIXME
            rotation2d_z = np.dot(e.mesh.rotation_z(angle), vert.reshape(3,1))
            rotation2d_y  = np.dot(e.mesh.rotation_y(z_angle), rotation2d_z)
            rotation2d_x = np.dot(e.mesh.rotation_x(angle), rotation2d_y)
            projection2d = np.dot(e.proj_mat, rotation2d_x)
            x = int(projection2d[0][0] * scale + circle_pos[0]) # circle_pos -> OFFSET
            y = int(projection2d[1][0] * scale + circle_pos[1]) #               offset
            #print(rotation2d_x);print()
            if norm_x * rotation2d_x[0] + norm_y * rotation2d_x[1] + norm_z * rotation2d_x[2] > 0:
                pygame.draw.circle(e.window.screen, (255,0,100), (x,y), 3)
            proj_points.append([x,y])
        #print(proj_points)
        l1 = np.array(proj_points[2]) - np.array(proj_points[0])
        l2 = np.array(proj_points[1]) - np.array(proj_points[0])
        norm_d = np.cross(l1, l2)
        if norm_d > 0:
            pygame.draw.line(e.window.screen, (255,255,255), proj_points[0], proj_points[1])
            pygame.draw.line(e.window.screen, (255,255,255), proj_points[0], proj_points[2])
            pygame.draw.line(e.window.screen, (255,255,255), proj_points[2], proj_points[1])
            #pygame.draw.line(e.window.screen, (255,255,255), l2[0], l2[1])

        projected_points.append(proj_points)
    
    for projected_point in projected_points:
        # DRAW LINES
        p1 = np.array(projected_point[0][:2])
        p2 = np.array(projected_point[1][:2])
        p3 = np.array(projected_point[2][:2])
        l1 = p2 - p1
        l2 = p3 - p1
        angle+=0.001
        #pygame.draw.line(e.window.screen, (255,255,255), p1, p2)
        #pygame.draw.line(e.window.screen, (255,255,255), p2, p3)
        #pygame.draw.line(e.window.screen, (255,255,255), p1, p3)


    # Update screen
    e.fpsClock.tick(30)
    e.window.update()






