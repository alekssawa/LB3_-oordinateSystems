import numpy as np

from CalculateDistance import CalcOfDistancesCartesian2D, CalcOfDistancesCartesian3D, \
    CalcOfDistancesPolar2D, CalcOfDistancesSphericalThroughTheSphereVolume, \
    CalcOfDistancesSphericalOnTheSphereSurface

from ConvertationSystem import matrix2D, matrix2_2D, matrix3D, matrix2_3D, print_2d_array, print_3d_array\
    , PolarToCartesian, CartesianToPolar, SphericalToCartesian, CartesianToSpherical

from Generator import GeneratorCartesian2D, GeneratorCartesian3D, GeneratorPolar\
    , GeneratorSphericalThroughTheSphereVolume, GeneratorSphericalOnTheSphereSurface


print('========================================================================')
print('\nКоординати у полярній системі координат:')
print_2d_array(matrix2D)

print('\nКоординати у декартовій системі координат:')
PolarToCartesian(matrix2D[0][0], matrix2D[0][1], 0)
PolarToCartesian(matrix2D[1][0], matrix2D[1][1], 1)

print('\nКоординати після зворотного перетворення у полярній системі координат:')
CartesianToPolar(matrix2_2D[0][0], matrix2_2D[0][1], 0)
CartesianToPolar(matrix2_2D[1][0], matrix2_2D[1][1], 1)

print('\n========================================================================')
print('\nКоординати у сферичній системі координат:')
print_3d_array(matrix3D)

print('\nКоординати у декартовій системі координат:')
SphericalToCartesian(matrix3D[0][0], (matrix3D[0][1]), (matrix3D[0][2]), 0)
SphericalToCartesian(matrix3D[1][0], (matrix3D[1][1]), (matrix3D[1][2]), 1)

print('\nКоординати після зворотного перетворення у сферичній системі координат:')
CartesianToSpherical(matrix2_3D[0][0], (matrix2_3D[0][1]), (matrix2_3D[0][2]), 0)
CartesianToSpherical(matrix2_3D[1][0], (matrix2_3D[1][1]), (matrix2_3D[1][2]), 1)

print('\n========================================================================')
print('\nОбчислення відстані між точками у двовимірному просторі декартовій системі координат:')

x1, y1, x2, y2 = GeneratorCartesian2D()

CalcOfDistancesCartesian2D(x1, x2, y1, y2)

print('\nОбчислення відстані між точками у тривимірному просторі декартовій системі координат:')

x1, y1, z1, x2, y2, z2 = GeneratorCartesian3D()

CalcOfDistancesCartesian3D(x1, x2, y1, y2, z1, z2)

print('\n========================================================================')
print('\nОбчислення відстані між точками у двовимірному просторі полярній системі координат:')

r1, theta1, r2, theta2 = GeneratorPolar()

CalcOfDistancesPolar2D(r1, theta1, r2, theta2)

print('\n========================================================================')
print("\nОбчислення відстані між точками у сферичній системі координат через об'єм сфери:")

r1, theta1, phi1, r2, theta2, phi2 = GeneratorSphericalThroughTheSphereVolume()

CalcOfDistancesSphericalThroughTheSphereVolume(r1, theta1, phi1, r2, theta2, phi2)

print('\n========================================================================')
print("\nОбчислення відстані між точками у сферичній системі координат по поверхні сфери:")

r, theta1, phi1, theta2, phi2 = GeneratorSphericalOnTheSphereSurface()

CalcOfDistancesSphericalOnTheSphereSurface(r, theta1, phi1, theta2, phi2)
print('\n========================================================================')
