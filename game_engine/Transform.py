# http://jerome.jouvie.free.fr/opengl-tutorials/Lesson8.php
from functools import reduce
import numpy as np
import pywavefront
import math

FOV = 90.0
HALF_PI = math.pi * 0.5
PI = math.pi
TWO_PI = math.pi * 2.0


def Float(x=0.0):
    """Return a vector consisting of 1 float (x)"""
    return np.float32(x)

def Float2(x=0.0, y=0.0):
    """Return a vector consisting of 2 floats (x, y)"""
    return np.array([x, y], dtype=np.float32)

def Float3(x=0.0, y=0.0, z=0.0):
    """Return a vector consisting of 3 floats (x, y, z)"""
    return np.array([x, y, z], dtype=np.float32)

def Float4(x=0.0, y=0.0, z=0.0, w=0.0):
    """Return a vector consisting of 4 floats (x, y, z, w)"""
    return np.array([x, y, z, w], dtype=np.float32)

def Matrix3():
    """Return a 3x3 identity matrix"""
    return np.eye(3, dtype=np.float32)

def Matrix4():
    """Return a 4x4 identity matrix"""
    return np.eye(4, dtype=np.float32)

def transform(m, v):
    """Transformation matrix"""
    return np.asarray(m * np.asmatrix(v).T)[:, 0]

def length(v):
    """Get vector length"""
    return math.sqrt(np.sum(v * v))

def normalize(v):
    """Normalize vector"""
    m = length(v)
    if m == 0:
        return v
    return v / m

def clamp_radian(rad):
    """Clamp radian angle"""
    return (rad % TWO_PI) if (TWO_PI < rad) or (rad < 0.0) else rad

def radian_to_degree(radian):
    """Convert radians to degrees"""
    return clamp_radian(radian) / TWO_PI * 360.0

def matrix_multiply_vector(m, v):
    x, y, z, w = v[0], v[1], v[2], v[3]
    X = x * m[0,0] + y * m[1,0] + z * m[2,0] + w * m[3,0]
    Y = x * m[0,1] + y * m[1,1] + z * m[2,1] + w * m[3,1]
    Z = x * m[0,2] + y * m[1,2] + z * m[2,2] + w * m[3,2]
    W = x * m[0,3] + y * m[1,3] + z * m[2,3] + w * m[3,3]
    return Float4(X, Y, Z, W)

def matrix_multiply_vector4(m, v):
    x, y, z, w = v[0], v[1], v[2], v[3]
    X = x * m[0,0] + y * m[1,0] + z * m[2,0]
    Y = x * m[0,1] + y * m[1,1] + z * m[2,1] 
    Z = x * m[0,2] + y * m[1,2] + z * m[2,2]
    W = x * m[0,3] + y * m[1,3] + z * m[2,3] 
    return Float3(X, Y, Z)

def vector_add_w(v1, v2):
    x = float(v1[0] + v2[0])
    y = float(v1[1] + v2[1])
    z = float(v1[2] + v2[2])
    w = float(v1[3] + v2[3])
    return Float4(x, y, z, w)

def vector_dot(v1, v2):
    x = v1[0] * v2[0]
    y = v1[1] * v2[1]
    z = v1[2] * v2[2]
    return x + y + z

def vector_mul(v1, a):
    x = v1[0] * a
    y = v1[1] * a
    z = v1[2] * a
    return Float3(x,y,z)

def vector_add(v1, v2):
    x = float(v1[0] + v2[0])
    y = float(v1[1] + v2[1])
    z = float(v1[2] + v2[2])
    return Float3(x, y, z)

def vector_sub(v1, v2):
    x = float(v1[0] - v2[0])
    y = float(v1[1] - v2[1])
    z = float(v1[2] - v2[2])
    return Float3(x, y, z)

def vector_div(v1, k):
    x = float(v1[0] / k)
    y = float(v1[1] / k) 
    z = float(v1[2] / k) 
    return Float3(x, y, z)

def is_rotation_matrix(R):
    """Check if matrix is a valid rotation matrix"""
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6

def matrix_rotation(rotation_matrix, rx, ry, rz):
    """Rotate matrix"""
    ch = math.cos(ry)
    sh = math.sin(ry)
    ca = math.cos(rz)
    sa = math.sin(rz)
    cb = math.cos(rx)
    sb = math.sin(rx)

    rotation_matrix[:, 0] = [ch*ca, sh*sb - ch*sa*cb, ch*sa*sb + sh*cb, 0.0]
    rotation_matrix[:, 1] = [sa, ca*cb, -ca*sb, 0.0]
    rotation_matrix[:, 2] = [-sh*ca, sh*sa*cb + ch*sb, -sh*sa*sb + ch*cb, 0.0]

def matrix_to_vectors(rotation_matrix, axis_x, axis_y, axis_z, normalize=False):
    """"""
    if normalize:
        rotation_matrix[0, 0:3] = normalize(rotation_matrix[0, 0:3])
        rotation_matrix[1, 0:3] = normalize(rotation_matrix[1, 0:3])
        rotation_matrix[2, 0:3] = normalize(rotation_matrix[2, 0:3])
    axis_x[:] = rotation_matrix[0, 0:3]
    axis_y[:] = rotation_matrix[1, 0:3]
    axis_z[:] = rotation_matrix[2, 0:3]

# TODO: convert format from list -> numpy array?
def getYawPitchRoll(M):
    """Return the yaw, pitch and roll for matrix M"""
    pitch = math.arcsin(-M[2][1])
    threshold = 1e-8
    test = math.cos(pitch)
    if test < threshold:
        roll = math.arctan2(-M[1][0], M[0][0])
        yaw = 0.0
    else:
        roll = math.arctan2(M[0][1], M[1][1])
        yaw = math.arctan2(M[2][0], M[2][2])
    return yaw, pitch, roll

def axis_rotation(axis, radian):
    """Rotate an axis"""
    angle = radian * 0.5
    s = math.sin(angle)
    return Float4(math.cos(angle), axis[0]*s, axis[1]*s, axis[2]*s)

def lerp(vector1, vector2, t):
    return vector1 * (1.0 - t) + vector2 * t

def set_identity_matrix(M):
    M[...] = [[1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]]

def get_translate_matrix(x, y, z):
    T = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [x, y, z, 1]]
    return np.array(T, dtype=np.float32)

def set_translate_matrix(M, x, y, z):
    M[:] = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [x, y, z, 1]]

def matrix_translate(M, x, y, z):
    M[3][0] += x
    M[3][1] += y
    M[3][2] += z

def get_scale_matrix(x, y, z):
    S = [[x, 0, 0, 0],
         [0, y, 0, 0],
         [0, 0, z, 0],
         [0, 0, 0, 1]]
    return np.array(S, dtype=np.float32)

def set_scale_matrix(M, x, y, z):
    M[:] = [[x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]

def matrix_scale(M, x, y, z):
    M[0] *= x
    M[1] *= y
    M[2] *= z

def degree_to_rad(degree):
    rad = (degree / 180) * PI
    return rad

def get_rotation_matrix_x(radian):
    cosT = math.cos(radian)
    sinT = math.sin(radian)
    matrix = np.array(
        [[1.0, 0.0, 0.0, 0.0],
         [0.0, cosT, sinT, 0.0],
         [0.0, -sinT, cosT, 0.0],
         [0.0, 0.0, 0.0, 1.0]], dtype=np.float32)
    return matrix

def get_rotation_matrix_y(radian):
    cosT = math.cos(radian)
    sinT = math.sin(radian)
    matrix = np.array(
        [[cosT, 0.0, -sinT, 0.0],
         [0.0, 1.0, 0.0, 0.0],
         [sinT, 0.0, cosT, 0.0],
         [0.0, 0.0, 0.0, 1.0]], dtype=np.float32)
    return matrix

def get_rotation_matrix_z(radian):
    cosT = math.cos(radian)
    sinT = math.sin(radian)
    matrix = np.array(
        [[cosT, sinT, 0.0, 0.0],
         [-sinT, cosT, 0.0, 0.0],
         [0.0, 0.0, 1.0, 0.0],
         [0.0, 0.0, 0.0, 1.0]], dtype=np.float32)
    return matrix

def matrix_rotate_x(M, radian):
    cosT = math.cos(radian)
    sinT = math.sin(radian)
    R = np.array(
        [[1.0, 0.0, 0.0, 0.0],
         [0.0, cosT, sinT, 0.0],
         [0.0, -sinT, cosT, 0.0],
         [0.0, 0.0, 0.0, 1.0]], dtype=np.float32)
    M[...] = np.dot(M, R)

def matrix_rotate_y(M, radian):
    cosT = math.cos(radian)
    sinT = math.sin(radian)
    R = np.array(
        [[cosT, 0.0, -sinT, 0.0],
         [0.0, 1.0, 0.0, 0.0],
         [sinT, 0.0, cosT, 0.0],
         [0.0, 0.0, 0.0, 1.0]], dtype=np.float32)
    M[...] = np.dot(M, R)

def matrix_rotate_z(M, radian):
    cosT = math.cos(radian)
    sinT = math.sin(radian)
    R = np.array(
        [[cosT, sinT, 0.0, 0.0],
         [-sinT, cosT, 0.0, 0.0],
         [0.0, 0.0, 1.0, 0.0],
         [0.0, 0.0, 0.0, 1.0]], dtype=np.float32)
    M[...] = np.dot(M, R)


def matrix_rotate_axis(M, radian, x, y, z):
    c, s = math.cos(radian), math.sin(radian)
    n = math.sqrt(x * x + y * y + z * z)
    x /= n
    y /= n
    z /= n
    cx, cy, cz = (1 - c) * x, (1 - c) * y, (1 - c) * z
    R = np.array([[cx * x + c, cy * x - z * s, cz * x + y * s, 0],
                  [cx * y + z * s, cy * y + c, cz * y - x * s, 0],
                  [cx * z - y * s, cy * z + x * s, cz * z + c, 0],
                  [0, 0, 0, 1]]).T
    M[...] = np.dot(M, R)

def matrix_rotate(M, rx, ry, rz):
    R = MATRIX4_IDENTITY.copy()
    matrix_rotation(R, rx, ry, rz)
    M[...] = np.dot(M, R)

def extract_location(matrix):
    return Float3(matrix[3, 0], matrix[3, 1], matrix[3, 2])

def extract_rotation(matrix):
    scale = extract_scale(matrix)
    rotation = Matrix4()
    rotation[0, :] = matrix[0, :] / scale[0]
    rotation[1, :] = matrix[1, :] / scale[1]
    rotation[2, :] = matrix[2, :] / scale[2]
    return rotation

def extract_scale(matrix):
    sX = np.linalg.norm(matrix[0, :])
    sY = np.linalg.norm(matrix[1, :])
    sZ = np.linalg.norm(matrix[2, :])
    return Float3(sX, sY, sZ)

def lookat(matrix, eye, target, up):
    f = normalize(target - eye)
    s = np.cross(f, up)
    u = np.cross(s, f)
    matrix[0, 0:3] = s
    matrix[1, 0:3] = u
    matrix[2, 0:3] = f
    matrix[3, 0:3] = [-np.dot(s, eye), -np.dot(u, eye), -np.dot(f, eye)]

def ortho(M, left, right, bottom, top, znear, zfar):
    M[0, 0] = 2.0 / (right - left)
    M[1, 1] = 2.0 / (top - bottom)
    M[2, 2] = -2.0 / (zfar - znear)
    M[3, 0] = -(right + left) / float(right - left)
    M[3, 1] = -(top + bottom) / float(top - bottom)
    M[3, 2] = -(zfar + znear) / float(zfar - znear)
    M[3, 3] = 1.0
    return M

def perspective(fov, aspectRatio, znear, zfar):
    if znear == zfar:
        znear = 0.0
        zfar = znear + 1000.0

    if fov <= 0.0: fov = FOV

    height = np.tan((fov * 0.5) / 180.0 * np.pi) * znear
    width = height * aspectRatio
    depth = zfar - znear

    left = -width; right  = width
    top  = height; bottom = -height

    M = Matrix4()
    M[0, :] = [znear / width, 0.0, 0.0, 0.0]
    M[1, :] = [0.0, znear / height, 0.0, 0.0]
    M[2, :] = [0.0, 0.0, -(zfar + znear) / depth, -1.0]
    M[3, :] = [0.0, 0.0, -2.0 * znear * zfar / depth, 0.0]
    return M

def createCube():
    """Create a unit cube"""
    cube = [ 
            [(0,0,0), (0,1,0), (1,1,0)], [(0,0,0), (1,1,0), (1,0,0)], # South
            [(1,0,0), (1,1,0), (1,1,1)], [(1,0,0), (1,1,1), (1,0,1)], # East
            [(1,0,1), (1,1,1), (0,1,1)], [(1,0,1), (0,1,1), (0,0,1)], # North
            [(0,0,1), (0,1,1), (0,1,0)], [(0,0,1), (0,1,0), (0,0,0)], # West
            [(0,1,0), (0,1,1), (1,1,1)], [(0,1,0), (1,1,1), (1,1,0)], # Top
            [(1,0,1), (0,0,1), (0,0,0)], [(1,0,1), (0,0,0), (1,0,0)], # Bottom
        ]
    return cube

def importObject(path):
    scene = pywavefront.Wavefront(path, collect_faces=True)
    return scene

def obj_to_mesh(path, return_scene=False):
    """Import and convert an .obj file
       Scene can returned as well   """
    scene = importObject(path)
    model = []
    mesh = scene
    for mesh in scene.mesh_list:
        triangle = []
        faces = mesh.faces
        for face in faces:
            for vidx in face:
                vert = scene.vertices[vidx]
                triangle.append(np.array(vert))
            model.append(triangle.copy())
            triangle.clear()
    return model if (return_scene == False) else (model, scene)

def rotation_y(angle):
    rad = angle / 180 * PI
    mat4x4 = np.zeros((4,4), dtype=np.float32)
    mat4x4[0,0] = math.cos(rad)
    mat4x4[0,2] = math.sin(rad)
    mat4x4[1,1] = 1.0
    mat4x4[2,2] = math.cos(rad)
    mat4x4[3,3] = 1.0
    return mat4x4

def rotation_x(angle):
    rotation_x = np.matrix([
        [1.0, 0.0, 0.0],
        [0.0, math.cos(angle), -math.sin(angle)],
        [0.0, math.sin(angle), math.cos(angle)],
    ], dtype=np.float32)
    return rotation_x

def point_at(pos, target, up):
    newForward = vector_sub(target, pos)
    newForward = normalize(newForward)
    a = vector_mul(newForward, vector_dot(up, newForward))
    newUp = vector_sub(up, a)
    newUp = normalize(newUp)

    right = np.cross(newUp, newForward)

    matrix = np.matrix([
        [right[0], right[1], right[2], 0.0],
        [up[0], up[1], up[2], 0.0],
        [newForward[0], newForward[1], newForward[2], 0.0],
        [pos[0], pos[1], pos[2], 1.0]
        ], dtype=np.float32)

    return matrix

def intersection(point, n, startPos, endPos):
    """
    point: on the plane
    n: normal to the plane
    startPos: start position of line
    endPos: end position of line
    """
    startPos = startPos
    endPos = endPos
    n = normalize(n)
    d = float(-1.0 * np.dot(n, point))
    ad = np.dot(startPos, n)
    bd = np.dot(endPos, n)
    t = (-d - ad) / (bd - ad)

    line = vector_sub(endPos, startPos)
    intersection = vector_mul(line, t)

    return np.append(vector_add(startPos, intersection), np.array([0])) #FIXME

def get_dist(p, n):
    vn = normalize(p) 
    nx, ny, nz = n[0], n[1], n[2]
    x, y, z = vn[0], vn[1], vn[2]
    dist = float(nx*x + ny*y + nz*z - np.dot(n, p))
    return dist

def triangle_clip(p, n, tri):
    inside, outside = [], []
    p1, p2, p3 = tri[0], tri[1], tri[2]
    n = normalize(n)
    nx, ny, nz = n[0], n[1], n[2]

    # return shortest distance from point -> plane
    d0, d1, d2 = get_dist(p1,n), get_dist(p2,n), get_dist(p3,n)

    if d0 >= 0: inside.append(p1)
    else:       outside.append(p1)
    if d1 >= 0: inside.append(p2)
    else:       outside.append(p2)
    if d2 >= 0: inside.append(p3)
    else:       outside.append(p3)
    
    insidePointCount, outsidePointCount = len(inside), len(outside)
    
    if insidePointCount == 0:
        # reject -> no vertices are valid
        return None, None

    elif insidePointCount == 3:
        # accept -> all vertices are valid
        tri1 = Matrix4()
        tri1[0, :] = tri[0]
        tri1[1, :] = tri[1]
        tri1[2, :] = tri[2]
        return tri1, None

    elif insidePointCount == 1 and outsidePointCount == 2:
        # Clip triangle, 2 points lie outside
        # < COPY TRIANGLE DATA >
        outTri1, outTri2 = Matrix4(), Matrix4()
        p_in = inside[0]
        p1_out = intersection(p, n, p_in, outside[0])
        p2_out = intersection(p, n, p_in, outside[1])

        outTri1[0, :] = p_in
        outTri1[1, :] = p1_out
        outTri1[2, :] = p2_out
        return outTri1, outTri2

    elif insidePointCount == 2 and outsidePointCount == 1:
        # Clip triangle, 2 points lie inside -> form quad
        # < COPY TRIANGLE DATA >
        tri1, tri2 = Matrix4(), Matrix4()
        p1_in, p2_in = inside[0], inside[1]
        pi3 = intersection(p, n, p1_in, outside[0])
        pi4 = intersection(p, n, p2_in, outside[0])

        tri1[0, :] = p1_in
        tri1[1, :] = p2_in
        tri1[2, :] = pi3

        tri2[0, :] = p2_in
        tri2[1, :] = pi3
        tri2[2, :] = pi4
        return tri1, tri2
















