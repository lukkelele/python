from matplotlib import pyplot as p

step = 0.1


def draw_boundary():
    lst = []
    points = []
    start = -2
    f = start
    while f <= 2:
        while start <= 2:
            z = f"{f}, {start}"
            lst.append(z)
            start += step
        f += step
        start = -2
    for point in lst:
        s = point.split(",")
        p.scatter(float(s[0]), float(s[1]))


draw_boundary()

#print(c)

#p.subplot(2,2,1)



p.show()


a = np.arange(-2, 2.1, 0.1)
nx, ny = (200, 200)
x = np.linspace(-0.1, 0.1, nx)
y = np.linspace(-2, 2, ny)
xv, yv = np.meshgrid(x, y)
zz = xv
h = p.contour(x, y, zz)
p.axis("off")
p.colorbar()
p.show()





def determine_point(z, neighbors, k):
    s = 0
    for n in neighbors:
        s += int(n[3])
    if k == 1:
        if s == 1:
            p.scatter(z[0], z[1], color="g")
        else:
            p.scatter(z[0], z[1], color="r")
    elif k == 3:
        if s > 1:
            p.scatter(z[0], z[1], color="g")
        else:
            p.scatter(z[0], z[1], color="r")
    elif k == 5:
        if s > 2:
            p.scatter(z[0], z[1], color="g")
        else:
            p.scatter(z[0], z[1], color="r")
    elif k == 7:
        if s > 3:
            p.scatter(z[0], z[1], color="g")
        else:
            p.scatter(z[0], z[1], color="r")
    else:
        print("The number could not be run as a value of neighbors.\n"+
              "Make sure the numbers are odd.")
    

