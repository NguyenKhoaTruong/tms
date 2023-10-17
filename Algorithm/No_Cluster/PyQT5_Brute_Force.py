import itertools
import numpy as np


class Brute_Force:
    def __init__(self):
        print("Thuật toán Brute_Force TSP")

    def brute_force_tsp(points, distance_matrix, start_point, on, off):
        def total_distance(route, distance_matrix):
            total = 0
            if on == True:
                for i in range(len(route) - 1):
                    total += distance_matrix[route[i]][route[i + 1]]
                total += distance_matrix[route[-1]][route[0]]
            elif off == True:
                for i in range(len(route) - 1):
                    total += distance_matrix[route[i]][route[i + 1]]
            return total

        point_array = np.array(points)
        start_index = np.where(np.all(point_array == start_point, axis=1))[0][0]
        shortest_distance = float("inf")
        shortest_route = None
        all_routes = list(
            itertools.permutations([i for i in range(len(points)) if i != start_index])
        )
        for route in all_routes:
            route = (start_index,) + route
            distance = total_distance(route, distance_matrix)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_route = route
        if on == True:
            shortest_route = shortest_route + (shortest_route[0],)
        return shortest_distance, shortest_route
