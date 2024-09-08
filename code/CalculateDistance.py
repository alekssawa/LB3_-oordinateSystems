import numpy as np

def CalcOfDistancesCartesian2D(x1, x2, y1, y2):
    d = round(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    print(f"Відстань між точками: {d}")


def CalcOfDistancesCartesian3D(x1, x2, y1, y2, z1, z2):
    d = round(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), 2)
    print(f"Відстань між точками: {d}")


def CalcOfDistancesPolar2D(r1, theta1, r2, theta2):
    d = round(np.sqrt((r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * np.cos(theta2 - theta1))), 2)
    print(f"Відстань між точками: {d}")


def CalcOfDistancesSphericalThroughTheSphereVolume(r1, theta1, phi1, r2, theta2, phi2):
    d = round(np.sqrt((r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * np.sin(theta1) * np.sin(theta2) * np.cos(phi1 - phi2) + np.cos(
        theta1) * np.cos(theta2))), 2)
    print(f"Відстань між точками: {d}")


def CalcOfDistancesSphericalOnTheSphereSurface(r, theta1, phi1, theta2, phi2):
    d = round(r * np.arccos(np.sin(phi1) * np.sin(phi2) + np.cos(phi1) * np.cos(phi2) * np.cos(theta1 - theta2)), 2)
    print(f"Відстань між точками: {d}")