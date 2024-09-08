import numpy as np
import math


matrix2D = np.array([[30, math.pi / 4], [50, 2 * math.pi / 3]])
matrix2_2D = np.zeros((2, 2), dtype=float)

matrix3D = np.array([[40, math.pi / 3, math.pi / 6], [50, math.pi / 2, math.pi / 4]])
matrix2_3D = np.zeros((2, 3), dtype=float)

def PolarToCartesian(r, theta, Num):
    x = round(r * np.cos(theta), 2)
    y = round(r * np.sin(theta), 2)
    matrix2_2D[Num][0] = x
    matrix2_2D[Num][1] = y
    print(f"Точка {Num+1}: x: {matrix2_2D[Num][0]}, y: {matrix2_2D[Num][1]}")

def CartesianToPolar(x, y, Num):
    r = round(np.sqrt(x ** 2 + y ** 2), 2)
    theta = round(np.arctan2(y, x), 2)
    print(f"Точка {Num+1}: r: {r}, theta: {theta} rad ({round(np.degrees(theta),2)}°)")

# 3D
def SphericalToCartesian(r, theta, phi, Num):
    x = r * np.sin(phi) * np.cos(theta)
    y = round(r * np.sin(phi) * np.sin(theta), 2)
    z = round(r * np.cos(phi), 2)
    matrix2_3D[Num][0] = x
    matrix2_3D[Num][1] = y
    matrix2_3D[Num][2] = z
    #print(matrix2_3D[Num][0], matrix2_3D[Num][1], matrix2_3D[Num][2])
    print(f"Точка {Num+1}: x: {matrix2_3D[Num][0]}, y: {matrix2_3D[Num][1]}, z: {matrix2_3D[Num][2]}")


def CartesianToSpherical(x, y, z, Num):
    r = round(np.sqrt(x ** 2 + y ** 2 + z ** 2), 2)
    theta = round(np.arctan2(y, x), 2)
    phi = round(np.arccos(z / r), 2)
    #print(r, theta, phi)
    print(f"Точка {Num+1}: r: {r}, theta: {theta} rad ({round(np.degrees(theta),2)}°), phi: {phi} rad ({round(np.degrees(phi),2)}°)")

def print_2d_array(arr):
    for i, row in enumerate(arr):
        print(f"Точка {i + 1}: r: {row[0]:.2f}, theta: {row[1]:.2f} rad ({round(np.degrees(row[1]),2)}°)")

def print_3d_array(arr):
    for i, row in enumerate(arr):
        print(f"Точка {i + 1}: r: {row[0]:.2f}, theta: {row[1]:.2f} rad ({round(np.degrees(row[1]),2)}°), phi: {row[2]:.2f} rad ({round(np.degrees(row[2]),2)}°)")
