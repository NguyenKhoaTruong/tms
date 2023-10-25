from geopy.distance import great_circle
import itertools
import random
import math
import numpy as np


def brute_force_tsp(points, distance_matrix, start_point):
    def total_distance(route, distance_matrix):
        total = 0
        for i in range(len(route) - 1):
            total += distance_matrix[route[i]][route[i + 1]]
        total += distance_matrix[route[-1]][route[0]]
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
    shortest_route = shortest_route + (shortest_route[0],)
    return shortest_route, shortest_distance


# Randomized Tour
def randomized_tour(distance_matrix, start_point_index):
    n = len(distance_matrix)
    tour = [i for i in range(n)]
    random.shuffle(tour)
    start_index = tour.index(start_point_index)
    tour.insert(0, tour.pop(start_index))
    total_distance = 0
    for i in range(n - 1):
        total_distance += distance_matrix[tour[i]][tour[(i + 1) % n]]
    return tour, total_distance


# Christofides Algorithm
def convent_Route(route, point):
    route_Convert = [point[i] for i in route]
    return route_Convert


def use_Christofides(point, start_Point, mode_Start):
    try:
        if mode_Start == True:
            point.insert(0, start_Point)
        n = len(point)
        G = nx.complete_graph(n)

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = (
                math.sin(dlat / 2) ** 2
                + math.cos(math.radians(lat1))
                * math.cos(math.radians(lat2))
                * math.sin(dlon / 2) ** 2
            )
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            return R * c

        dist_matrix = [
            [haversine(lat1, lon1, lat2, lon2) for lat2, lon2 in point]
            for lat1, lon1 in point
        ]
        tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True)
        tsp_tour = tsp_tour[:-1]
        total_distance = sum(dist_matrix[i][j] for i, j in zip(tsp_tour, tsp_tour[1:]))
        route = convent_Route(tsp_tour, point)
        cost = round(total_distance, 3)
        return route, cost
    except ValueError as e:
        raise ("Log Error", e)


# Nearest_Neighbor


def tsp_nearest_neighbor(distance_matrix, start_point_index, points):
    def find_nearest_neighbor(distance_matrix, current_vertex, visited):
        nearest_neighbor = None
        min_distance = float("inf")
        for v in range(len(distance_matrix)):
            if not visited[v] and distance_matrix[current_vertex][v] < min_distance:
                nearest_neighbor = v
                min_distance = distance_matrix[current_vertex][v]
        return nearest_neighbor

    num_vertices = len(distance_matrix)
    visited = [False] * num_vertices
    path = [start_point_index]
    current_vertex = start_point_index
    visited[start_point_index] = True
    total_distance = 0.0

    for _ in range(num_vertices - 1):
        nearest_neighbor = find_nearest_neighbor(
            distance_matrix, current_vertex, visited
        )
        path.append(nearest_neighbor)
        visited[nearest_neighbor] = True
        total_distance += distance_matrix[current_vertex][nearest_neighbor]
        current_vertex = nearest_neighbor
    tsp_path_latlon = [(points[idx][0], points[idx][1]) for idx in path]
    return tsp_path_latlon, total_distance


def calculate_distances(data):
    def euclidean_distance(point1, point2):
        distances = great_circle(point1, point2).kilometers
        return distances

    num_points = len(data)
    distances = [[0 for _ in range(num_points)] for _ in range(num_points)]

    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = euclidean_distance(data[i], data[j])
            distances[i][j] = distance
            distances[j][i] = distance
    return distances


def format_path_to_string(path, points):
    path_String = []
    for i in range(len(path)):
        lat, lon = points[path[i]]
        path_String.append([lat, lon])
    return path_String


def route_To_Order(route, data_Order):
    orders = []
    for item in data_Order:
        lat = item[5]
        lon = item[6]
        if [lat, lon] in route:
            order = item[1]
            orders.append(order)
    return orders


def show_Result(points, start_Point, matrix, name_Algorithm):
    try:
        order_StartPoint = [
            "MCStart",
            "Điểm bắt đầu",
            0.0,
            0.0,
            1.0,
            start_Point[0],
            start_Point[1],
        ]
        if start_Point and start_Point not in points:
            points.insert(0, start_Point)
            matrix.insert(0, order_StartPoint)
        distance = calculate_distances(points)
        if name_Algorithm == "Brute Force":
            route, cost = brute_force_tsp(points, distance, start_Point)
        elif name_Algorithm == "Nearest Neighbor":
            route, cost = tsp_nearest_neighbor(distance, 0, start_Point)
        elif name_Algorithm == "Randomized Tour":
            route, cost = randomized_tour(distance, 0)
        route_ = format_path_to_string(route, points)
        route_Order = route_To_Order(route_, matrix)
        return route_Order
    except ValueError as e:
        raise ("Log Error", e)


def funtion_Algorithm(data_Point, data_Matrix, start_Point, name_Algorithm):
    data_Order = []
    for index, value in enumerate(list(data_Point)):
        route = show_Result(
            list(data_Point[index]),
            start_Point,
            list(data_Matrix[index]),
            name_Algorithm,
        )
        data_Order.append(route)
        # print("check value data order", data_Order)
    return data_Order
