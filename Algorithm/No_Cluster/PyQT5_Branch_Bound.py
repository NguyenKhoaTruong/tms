import numpy as np
import itertools


class Branch_Bound:
    def __init__(self):
        print("Thuật toán Branch_Bound")

    def format_path_to_string(path, points):
        path_string = ""
        for i in range(len(path)):
            lat, lon = points[path[i]]
            path_string += f"{lat}, {lon}"
            if i < len(path) - 1:
                path_string += "->"
        return path_string

    def tsp_branch_and_bound(points, distance_matrix, start_point, on, off):
        start_point = points.index(start_point)

        num_points = len(points)
        min_cost = np.inf
        best_path = None

        def calculate_path_cost(path):
            cost = 0
            if on == True:
                for i in range(num_points - 1):
                    cost += distance_matrix[path[i]][path[i + 1]]
                cost += distance_matrix[path[-1]][path[0]]
            elif off == True:
                for i in range(len(path) - 1):
                    cost += distance_matrix[path[i]][path[i + 1]]
            return cost

        if off == True:
            num_points = [p for p in range(num_points) if p != start_point]
            all_permutations = itertools.permutations(num_points)  # mới
        elif on == True:
            all_permutations = itertools.permutations(range(0, num_points))
        for perm in all_permutations:
            current_path = [start_point] + list(perm)  # mới
            current_cost = calculate_path_cost(current_path)
            if on == True:
                current_cost += distance_matrix[current_path[-2]][current_path[-1]]
            elif off == True:
                current_cost = calculate_path_cost(current_path)
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = current_path

        return best_path, min_cost
