import pygame
import window, _mesh as mesh
import time

window = window.Window(500, 500, "CUBE")
cube = mesh.create_cube()

point1 = (2, 19, 25)
point2 = (0.10, 0.4, 0.2)


while True:
    window.screen.fill((0,0,0)) # blackscreen
    p1, p2 = cube.project(point1[0], point1[1], point1[2]) 
    cube.rotX += 0.01
    cube.rotY += 0.01
    cube.rotZ += 0.01
    pygame.draw.line(window.screen, (100,240, 5), (point1[0],point1[1]), (p1,p2), width=2)
    window.update()
    time.sleep(0.75)

