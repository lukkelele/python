from ssl import PROTOCOL_TLSv1_2
from pygame.locals import *
from pygame.key import *
from Window import *
import pygame, sys, os
#import pywavefront
import numpy as np
import Transform
import Triangle
import Line


class Engine:

    def __init__(self, width=1600, height=1024, title="Lukkelele Game Engine", tickrate=60,
                 linecolor=WHITE, edgecolor=GREEN, camstep=0.10, yawstep=0.10):
        self.pg = pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.tickrate = tickrate
        self.theta = 0.0
        self.yaw = 0.0
        self.vCam, self.vLook = Transform.Float3(0,0,0), Transform.Float3(0,0,1)
        self.vUp, self.vForward = Transform.Float3(0,1,0), Transform.Float3(0,0,1)
        self.vTarget = Transform.Float4(0,0,1)
        self.window = Window(width, height, title)
        self.width, self.height = width, height
        self.aspect_ratio = self.width / self.height
        self.linecolor, self.edgecolor = linecolor, edgecolor
        self.camstep, self.yawstep = camstep, yawstep
        self.matCam, self.matView = Transform.Matrix4(), Transform.Matrix4()
        self.matWorld = Transform.Matrix4()
        self.matTrans = Transform.get_translate_matrix(0.0, 0.0, 4.0)

    def clear_screen(self):
        self.window.clear()
        self.window.update()

    def tick(self):
        e.window.update()
        e.fpsClock.tick(self.tickrate)

    def quit(self):
        pygame.quit()
        exit()


e = Engine(width=1400, height=1000)
e.window.screen.fill((0,0,0)) # blackscreen
background = pygame.Surface((e.width, e.height))
cube = Transform.createCube()
ship = Transform.obj_to_mesh('./obj/ship.obj')
axis = Transform.obj_to_mesh('./obj/axis.obj')
#axis = e.importObject('./axis.obj')
e.clear_screen()
objmodel = ship

OFFSET_x, OFFSET_y = e.width / 2, e.height / 2
theta, fYaw = 0.0, 0.0
matCam, matView = Transform.Matrix4(), Transform.Matrix4()
vOffsetView = Transform.Float3(0,0,1)
matProj = Transform.perspective(90.0, e.aspect_ratio, 0.10, 1000.0)

edges = True
scale = 100
camScale = 0.10
zRot = Transform.get_rotation_matrix_z(theta * 0.50)
xRot = Transform.get_rotation_matrix_x(theta)

while True:
    e.window.screen.blit(background, (0,0)) # TODO: fix refresh for screen

    for event in pygame.event.get():
        if event.type == QUIT: e.quit()
    
    # Basic input controls for camera
    if pygame.key.get_pressed()[K_RIGHT]:  e.vCam[0] += e.camstep
    elif pygame.key.get_pressed()[K_LEFT]: e.vCam[0] -= e.camstep
    elif pygame.key.get_pressed()[K_UP]:   e.vCam[1] += e.camstep
    elif pygame.key.get_pressed()[K_DOWN]: e.vCam[1] -= e.camstep

    # First Person Shooter controls
    if pygame.key.get_pressed()[K_w]:   e.vCam = Transform.vector_add(e.vCam, e.vForward)
    elif pygame.key.get_pressed()[K_s]: e.vCam = Transform.vector_sub(e.vCam, e.vForward)
    elif pygame.key.get_pressed()[K_q]: e.yaw += e.yawstep
    elif pygame.key.get_pressed()[K_e]: e.yaw -= e.yawstep
    elif pygame.key.get_pressed()[K_d]: e.vCam[0] -= e.camstep
    elif pygame.key.get_pressed()[K_a]: e.vCam[0] += e.camstep

    # Rotate y axis by yaw value
    yRot = Transform.get_rotation_matrix_y(e.yaw)
    
    # World matrix
    matWorldRot = np.dot(zRot, xRot)
    e.matWorld = np.dot(e.matWorld, matWorldRot)
    matWorld = np.dot(e.matWorld, e.matTrans)
    
    # Look, target and forward vectors
    vTarget = Transform.Float4(0,0,1)
    e.vLook = Transform.matrix_multiply_vector(yRot, vTarget)
    vTarget = Transform.vector_add(e.vCam, e.vLook)
    e.vForward = Transform.vector_mul(e.vLook, 1)

    # Look-at matrix
    Transform.lookat(matView, e.vCam, vTarget, e.vUp)

    for triangle in objmodel:
        viewPlane, normalPlane = Transform.get_clipping_planes()
        triProj = []; triOffset = []; triProj_norm = []
        p1, p2, p3 = triangle[0], triangle[1], triangle[2]

        p1 = Transform.extend_vector_ones(p1)
        p2 = Transform.extend_vector_ones(p2)
        p3 = Transform.extend_vector_ones(p3)

        
        # Clip world space
        clipped_triangles = [] 
        #tri1, tri2 = Transform.triangle_clip(viewPlane, normalPlane, [p1v, p2v, p3v])
        tri = Triangle.transform(triangle, matWorld, matView)
        #tri = Triangle.transform(tri, matView)
        tri1, tri2 = Transform.triangle_clip(viewPlane, normalPlane, tri)
        
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

            P1, P2, P3 = Triangle.get_points(triOffset)
            line1 = Line.line(P1, P2)
            line2 = Line.line(P1, P3)
            line_norm = Line.normal(line1, line2)
            # if face is visible
            if line_norm > 0:
                triQueue.append(triOffset)

        for triangle in triQueue:
            Triangle.draw(e.window.screen, triangle, linecolor=e.linecolor,\
                          edgecolor=e.edgecolor, with_edges=True)
    
    e.tick()
