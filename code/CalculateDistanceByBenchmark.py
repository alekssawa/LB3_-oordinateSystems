import numpy as np

def CalcOfDistancesCartesian3D(num_pairs):
    points_array = np.random.uniform(-10, 10, (num_pairs, 2, 3))

    #for i, pair in enumerate(points_array):
        #print(
        #    f"{i + 1} {pair[0][0]:.2f} {pair[0][1]:.2f} {pair[0][2]:.2f}   "
        #    f"|   {pair[1][0]:.2f} {pair[1][1]:.2f} {pair[1][2]:.2f}")

    distances = np.sqrt(
        (points_array[:, 1, 0] - points_array[:, 0, 0]) ** 2 +
        (points_array[:, 1, 1] - points_array[:, 0, 1]) ** 2 +
        (points_array[:, 1, 2] - points_array[:, 0, 2]) ** 2
    )

    rounded_distances = np.round(distances, 2)

    for i, d in enumerate(rounded_distances):
        print(f"Пара {i + 1}: Расстояние: {d}")

    return rounded_distances

def CalcOfDistancesPolar2D(num_pairs):
    pairs = []
    for _ in range(num_pairs):
        pair = np.zeros((2, 2))
        pair[0][0] = np.random.uniform(0, 10)
        pair[0][1] = np.random.uniform(0, 2 * np.pi)
        pair[1][0] = np.random.uniform(0, 10)
        pair[1][1] = np.random.uniform(0, 2 * np.pi)
        pairs.append(pair)


    for i, pair in enumerate(pairs, start=1):
        #print(f"{i}: Точка 1: r: {pair[0][0]:.2f}, theta:  {pair[0][1]:.2f} rad ({round(np.degrees(pair[0][1]), 2)}°)   "
        #      f"|   Точка 2: r: {pair[1][0]:.2f}, theta:   {pair[1][1]:.2f}rad ({round(np.degrees(pair[1][1]), 2)}°)")
        d = round(np.sqrt(
            (pair[0][0] ** 2 + pair[1][0] ** 2 - 2 * pair[0][0] * pair[1][0] * np.cos(pair[1][1] - pair[0][1]))), 2)
        print(f"{i} Відстань між точками: {d}")


    return pairs

def CalcOfDistancesSphericalThroughTheSphereVolume(num_pairs):
    pairs = []
    for _ in range(num_pairs):
        pair = np.zeros((2, 3))
        pair[0][0] = np.random.uniform(0, 10)
        pair[0][1] = np.random.uniform(0, 2 * np.pi)
        pair[0][2] = np.random.uniform(0, np.pi)
        pair[1][0] = np.random.uniform(0, 10)
        pair[1][1] = np.random.uniform(0, 2 * np.pi)
        pair[1][2] = np.random.uniform(0, np.pi)
        pairs.append(pair)

    for i, pair in enumerate(pairs, start=1):
        #print(f"{i}: Точка 1: r: {pair[0][0]:.2f}, theta:  {pair[0][1]:.2f} rad ({round(np.degrees(pair[0][1]), 2)}°), phi(Широта): {pair[0][2]:.2f} rad ({round(np.degrees(pair[0][2]), 2)}°)  "
        #      f"|   Точка 2: r: {pair[1][0]:.2f}, theta:   {pair[1][1]:.2f} rad ({round(np.degrees(pair[1][1]), 2)}°), phi(Широта): {pair[1][2]:.2f} rad ({round(np.degrees(pair[1][2]), 2)}°)")

        d = round(np.sqrt((pair[0][0] ** 2 + pair[1][0] ** 2 - 2 * pair[0][0] * pair[1][0] * (np.sin(pair[0][1]) * np.sin(pair[1][1])
                                                                                              * np.cos(pair[0][2] - pair[1][2])) + np.cos(pair[0][1]) * np.cos(pair[1][1]))), 2)
        print(f"{i} Відстань між точками: {d}")


def CalcOfDistancesSphericalOnTheSphereSurface(num_pairs):
    pairs = []
    r = 6371
    for _ in range(num_pairs):
        pair = np.zeros((2, 3))
        pair[0][0] = np.random.uniform(-np.pi, np.pi)
        pair[0][1] = np.random.uniform(-np.pi / 2, np.pi / 2)
        pair[1][0] = np.random.uniform(-np.pi, np.pi)
        pair[1][1] = np.random.uniform(-np.pi / 2, np.pi / 2)
        pairs.append(pair)

    for i, pair in enumerate(pairs, start=1):
        #print(f"{i}: Точка 1: theta(Долгота): {pair[0][0]:.2f} rad ({round(np.degrees(pair[0][0]), 2)}°), phi(Широта): {pair[0][1]:.2f} rad ({round(np.degrees(pair[0][1]), 2)}°)  "
        #     f"|   Точка 2: theta(Долгота): {pair[1][0]:.2f} rad ({round(np.degrees(pair[1][0]), 2)}°), phi(Широта): {pair[1][1]:.2f} rad ({round(np.degrees(pair[1][1]), 2)}°)")
        d = round(r * np.arccos(np.sin(pair[0][1]) * np.sin(pair[1][1]) + np.cos(pair[0][1]) * np.cos(pair[1][1]) * np.cos(pair[0][0] - pair[1][0])), 2)
        print(f"{i} Відстань між точками: {d}")