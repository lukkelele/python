from pygame.locals import *
from pygame.key import *
import pygame, sys, os
import pywavefront
import numpy as np
import Transform
import window
import time
import math


class Engine:

    def __init__(self, width=500, height=500, title="Lukkelele Game Engine"):
        self.pg = pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.window = window.Window(width, height, title)
        self.WIDTH  = width
        self.HEIGHT = height

    def clearScreen(self):
        self.window.clear()
        self.window.update()

    def quit(self):
        pygame.quit()
        exit()

    def drawEdges(self, vertices, color=(255,255,255), rad=4):
        # FIXME
        vec1, vec2, vec3 = vertices[0], vertices[1], vertices[2]
        pygame.draw.circle(self.window.screen, color, vec1, radius=rad)
        pygame.draw.circle(self.window.screen, color, vec2, radius=rad)
        pygame.draw.circle(self.window.screen, color, vec3, radius=rad)


e = Engine(width=1000, height=1000)
e.window.screen.fill((0,0,0)) # blackscreen
background = pygame.Surface((e.WIDTH, e.HEIGHT))
cube = Transform.createCube()
ship = Transform.obj_to_mesh('./obj/ship.obj')
axis = Transform.obj_to_mesh('./obj/axis.obj')
#axis = e.importObject('./axis.obj')
e.clearScreen()
objmodel = ship

OFFSET_x, OFFSET_y = e.WIDTH / 2, e.HEIGHT / 2
vCamera = Transform.Float3(0,0,0)
vLookDir = Transform.Float3(0,0,1)
vUp = Transform.Float3(0,1,0)
vForward = Transform.Float3(0,0,1)
theta, fYaw = 0.0, 0.0
matCam, matView = Transform.Matrix4(), Transform.Matrix4()
vOffsetView = Transform.Float3(0,0,1)
matProj = Transform.perspective(90.0, e.HEIGHT/e.WIDTH, 0.10, 1000.0)
color = (255,255,255) # REMOVE

edges = True
scale = 100
camScale = 0.10
zRot = Transform.get_rotation_matrix_z(theta * 0.50)
xRot = Transform.get_rotation_matrix_x(theta)


while True:
    e.window.screen.blit(background, (0,0)) # TODO: fix refresh for screen

    for event in pygame.event.get():
        if event.type == QUIT:
            e.quit()
    
    # Basic input controls for camera
    if pygame.key.get_pressed()[K_RIGHT]:
        vCamera[0] += camScale
    elif pygame.key.get_pressed()[K_LEFT]:
        vCamera[0] -= camScale
    elif pygame.key.get_pressed()[K_UP]:
        vCamera[1] += camScale
    elif pygame.key.get_pressed()[K_DOWN]:
        vCamera[1] -= camScale

    # First Person Shooter controls
    if pygame.key.get_pressed()[K_w]:
        vCamera = Transform.vector_add(vCamera, vForward)
    elif pygame.key.get_pressed()[K_s]:
        vCamera = Transform.vector_sub(vCamera, vForward)
    if pygame.key.get_pressed()[K_d]:
        vCamera[0] -= camScale
    elif pygame.key.get_pressed()[K_a]:
        vCamera[0] += camScale
    elif pygame.key.get_pressed()[K_q]:
        fYaw += 0.10
    elif pygame.key.get_pressed()[K_e]:
        fYaw -= 0.10

    # Rotate y axis by yaw value
    yRot = Transform.get_rotation_matrix_y(fYaw)
    
    # World matrix 
    matWorld = Transform.Matrix4()
    matTrans = Transform.get_translate_matrix(0.0, 0.0, 4.0)
    matWorldRot = np.dot(zRot, xRot)
    matWorld = np.dot(matWorld, matWorldRot)
    matWorld = np.dot(matWorld, matTrans)
    
    # Look, target and forward vectors
    vTarget = Transform.Float4(0,0,1)
    vLookDir = Transform.matrix_multiply_vector(yRot, vTarget)
    vTarget = Transform.vector_add(vCamera, vLookDir)
    vForward = Transform.vector_mul(vLookDir, 1)

    # Look-at matrix
    Transform.lookat(matView, vCamera, vTarget, vUp)

    for triangle in objmodel:
        triProj = []; triOffset = []; triProj_norm = []
        p1, p2, p3 = triangle[0], triangle[1], triangle[2]

        p1 = np.append(p1, np.array([1]))  # TODO: add extend method
        p2 = np.append(p2, np.array([1]))
        p3 = np.append(p3, np.array([1]))
        # World Transformation
        p1t, p2t, p3t =  Transform.matrix_multiply_vector(matWorld, p1), \
                         Transform.matrix_multiply_vector(matWorld, p2), \
                         Transform.matrix_multiply_vector(matWorld, p3)
        # Camera Transformation
        p1v, p2v, p3v =  Transform.matrix_multiply_vector(matView, p1t), \
                         Transform.matrix_multiply_vector(matView, p2t), \
                         Transform.matrix_multiply_vector(matView, p3t)
        
        # Clip world space
        viewPlane = Transform.Float4(0,0,10,0)
        normalPlane = Transform.Float4(0,0,-5,0)
        clipped_triangles = [] 
        tri1, tri2 = Transform.triangle_clip(viewPlane, normalPlane, [p1v, p2v, p3v])
        
        if tri1 is not None:
            clipped_triangles.append(tri1)
            if tri2 is not None: clipped_triangles.append(tri2)
        triQueue = []
        c = len(clipped_triangles)
        for n in range(c):
            tri = clipped_triangles[n]
            # Project the clipped triangle
            p1p, p2p, p3p = np.dot(matProj, tri[0]), np.dot(matProj, tri[1]), np.dot(matProj, tri[2])
            triProj = [p1p, p2p, p3p]
            for vert in triProj:
                v = Transform.vector_div(vert, vert[3])  # vector / w
                v = Transform.vector_add(v, vOffsetView) # offset view
                v[0] *= -1.0 # redo inversion -> for XY plane
                v[1] *= -1.0 # redo inversion
                x = v[0]*scale + OFFSET_x
                y = v[1]*scale + OFFSET_y 
                v = (x, y)
                triOffset.append(v)

        # TODO: ADD METHOD
            P1 = triOffset[0]
            P2 = triOffset[1]
            P3 = triOffset[2]
            line1 = np.array([P2[0] - P1[0], P2[1] - P1[1]], dtype=np.float32)
            line2 = np.array([P3[0] - P1[0], P3[1] - P1[1]], dtype=np.float32)
            line_norm = np.cross(line1, line2)
            # if face is visible
            if line_norm > 0:
                triQueue.append(triOffset)

        for triangle in triQueue:
            P1, P2, P3 = triangle[0], triangle[1], triangle[2]
            pygame.draw.line(e.window.screen, color, P1, P2)
            pygame.draw.line(e.window.screen, color, P1, P3)
            pygame.draw.line(e.window.screen, color, P2, P3)
            if edges == True:
                e.drawEdges(triOffset, rad=2)

    
    e.fpsClock.tick(30)
    e.window.update()

