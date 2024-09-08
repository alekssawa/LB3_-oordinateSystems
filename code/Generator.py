import numpy as np


def GeneratorCartesian2D():
    x1 = round(np.random.uniform(-10, 10), 2)
    y1 = round(np.random.uniform(-10, 10), 2)
    x2 = round(np.random.uniform(-10, 10), 2)
    y2 = round(np.random.uniform(-10, 10), 2)

    print(f"Точка 1: x: {x1}, y: {y1}")
    print(f"Точка 2: x: {x2}, y: {y2}")

    return x1, y1, x2, y2


def GeneratorCartesian3D():
    x1 = round(np.random.uniform(-10, 10), 2)
    y1 = round(np.random.uniform(-10, 10), 2)
    z1 = round(np.random.uniform(-10, 10), 2)
    x2 = round(np.random.uniform(-10, 10), 2)
    y2 = round(np.random.uniform(-10, 10), 2)
    z2 = round(np.random.uniform(-10, 10), 2)

    print(f"Точка 1: x: {x1}, y: {y1}, z: {z1}")
    print(f"Точка 2: x: {x2}, y: {y2}, z: {z2}")

    return x1, y1, z1, x2, y2, z2

def GeneratorPolar():
    r1 = round(np.random.uniform(0, 10), 2)
    theta1 = round(np.random.uniform(0, 2 * np.pi), 2)
    r2 = round(np.random.uniform(0, 10), 2)
    theta2 = round(np.random.uniform(0, 2 * np.pi), 2)

    print(f"Точка 1: r: {r1}, theta: {theta1} rad ({round(np.degrees(theta1),2)}°)")
    print(f"Точка 2: r: {r2}, theta: {theta2} rad ({round(np.degrees(theta2),2)}°)")

    return r1, theta1, r2, theta2

def GeneratorSphericalThroughTheSphereVolume():
    r1 = round(np.random.uniform(0, 10), 2)
    theta1 = round(np.random.uniform(0, 2 * np.pi), 2)
    phi1 = round(np.random.uniform(0, np.pi), 2)
    r2 = round(np.random.uniform(0, 10), 2)
    theta2 = round(np.random.uniform(0, 2 * np.pi), 2)
    phi2 = round(np.random.uniform(0, np.pi), 2)

    print(f"Точка 1: r: {r1}, theta(Долгота): {theta1} rad ({round(np.degrees(theta1),2)}°), phi(Широта): {phi1} rad ({round(np.degrees(phi1),2)}°)")
    print(f"Точка 2: r: {r2}, theta(Долгота): {theta2} rad ({round(np.degrees(theta2),2)}°), phi(Широта): {phi2} rad ({round(np.degrees(phi2),2)}°)")

    return r1, theta1,phi1, r2, theta2, phi2

def GeneratorSphericalOnTheSphereSurface():
    r = 6371
    theta1 = round(np.random.uniform(-np.pi, np.pi), 2)
    phi1 = round(np.random.uniform(-np.pi / 2, np.pi / 2), 2)
    theta2 = round(np.random.uniform(-np.pi, np.pi), 2)
    phi2 = round(np.random.uniform(-np.pi / 2, np.pi / 2), 2)

    print(f"r: {r}")
    print(f"Точка 1: theta(Долгота): {theta1} rad ({round(np.degrees(theta1),2)}°), phi(Широта): {phi1} rad ({round(np.degrees(phi1),2)}°)")
    print(f"Точка 2: theta(Долгота): {theta2} rad ({round(np.degrees(theta2),2)}°), phi(Широта): {phi2} rad ({round(np.degrees(phi2),2)}°)")

    return r, theta1,phi1, theta2, phi2