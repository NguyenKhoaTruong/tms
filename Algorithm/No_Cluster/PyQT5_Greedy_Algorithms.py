import numpy as np


class Greedy_Algorithms:
    def __init__(self):
        print("Greedy_Algorithms")

    def greedy_tsp(origin, points, distances, on, off):
        num_points = len(points)
        visited = [False] * num_points
        path = [origin]
        current_point = origin
        total_distance = 0.0

        for _ in range(num_points):
            min_distance = float("inf")
            nearest_point_idx = None

            for i in range(num_points):
                if not visited[i]:
                    distance = distances[
                        np.where(
                            (np.array(points) == np.array(current_point)).all(axis=1)
                        )[0][0]
                    ][i]
                    if distance < min_distance:
                        min_distance = distance
                        nearest_point_idx = i

            if nearest_point_idx is not None:
                nearest_point = points[nearest_point_idx]
                path.append(nearest_point)
                total_distance += min_distance
                current_point = nearest_point
                visited[nearest_point_idx] = True

        path = path[1:]
        if on == True:
            path.append(origin)
            total_distance += distances[
                np.where((np.array(points) == np.array(current_point)).all(axis=1))[0][
                    0
                ]
            ][np.where((np.array(points) == np.array(origin)).all(axis=1))[0][0]]
        elif off == True:
            total_distance
        return path, total_distance
