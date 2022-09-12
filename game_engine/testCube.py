import window, _mesh as mesh

window = window.Window(500, 500, "CUBE")
cube = mesh.create_cube()


while True:
    cube.rotX += 0.001  
    cube.rotY += 0.01   
    cube.rotZ += 0.001  
    cube.render(window)
    window.update()
