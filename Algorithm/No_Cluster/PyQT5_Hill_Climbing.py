import numpy as np


class Hill_Climbing:
    def __init__(self):
        print("Hill_Climbing")

    def hill_climbing(distances, start_point, dataPoints, on, off, num_iterations=1000):
        def calculate_total_distance(points_order, distances):
            total_distance = 0
            if on == True:
                for i in range(len(points_order) - 1):
                    total_distance += distances[points_order[i]][points_order[i + 1]]
                total_distance += distances[points_order[-1]][points_order[0]]
            elif off == True:
                for i in range(len(points_order) - 1):
                    total_distance += distances[points_order[i]][points_order[i + 1]]
            return total_distance

        def find_nearest_point(start_point, points):
            start_point = np.array(start_point)
            distances = np.linalg.norm(points - start_point, axis=1)
            return np.argmin(distances)

        num_points = len(distances)

        current_order = list(range(num_points))

        start_index = find_nearest_point(start_point, dataPoints)

        current_order.remove(start_index)
        current_order.insert(0, start_index)

        current_distance = calculate_total_distance(current_order, distances)

        for _ in range(num_iterations):
            # Generate a random neighbor by swapping two points
            neighbor_order = current_order.copy()

            i, j = np.random.choice(range(1, num_points), size=2, replace=True)
            neighbor_order[i], neighbor_order[j] = neighbor_order[j], neighbor_order[i]

            neighbor_distance = calculate_total_distance(neighbor_order, distances)

            # If the neighbor has a shorter distance, move to the neighbor
            if neighbor_distance < current_distance:
                current_order = neighbor_order
                current_distance = neighbor_distance
        if on == True:
            current_order.append(current_order[0])

        return current_order, current_distance

    def convert_to_lat_lon(order, points):
        lat_lon_order = [(points[i][0], points[i][1]) for i in order]
        return lat_lon_order
