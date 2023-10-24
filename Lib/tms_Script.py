from geopy.distance import great_circle
from sklearn.cluster import KMeans
import networkx as nx
import numpy as np
import itertools
import random
import math


# Algorithm
# Brute Force:
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


# Ant Colony Optimization
# Tabu Search
# -------------------------------------------------------------------------------------#
def format_path_to_string(path, points):
    path_String = []
    for i in range(len(path)):
        lat, lon = points[path[i]]
        path_String.append([lat, lon])
    return path_String


def convert_Data(data_Cluster):
    data_array = np.array(data_Cluster)
    array_Matrix = np.array([[float(item[5]), float(item[6])] for item in data_array])
    return data_array, array_Matrix


def convent_Data_Point(data):
    point = []
    for value in data:
        sub_Data = []
        if len(value) == 0:
            print("...")
        else:
            for item in value:
                lat = item[5]
                lon = item[6]
                sub_Data.append([float(lat), float(lon)])
            point.append(sub_Data)
    return point


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


def cluster(data_Cluster, num_Cluster):
    data_Matrix = []
    data_Point = []
    num_clusters = num_Cluster
    data, matrix_data = convert_Data(data_Cluster)
    kmeans = KMeans(n_clusters=int(num_clusters))
    kmeans.fit(matrix_data)

    label_Data = kmeans.labels_
    center_Data = kmeans.cluster_centers_

    for i in range(int(num_clusters)):
        cluster_data = [
            data_Cluster[j] for j in range(len(data_Cluster)) if label_Data[j] == i
        ]
        data_Matrix.append(cluster_data)
    for i in range(int(num_clusters)):
        cluster_points = matrix_data[label_Data == i]
        data_Point.append(cluster_points)
    points = convent_Data_Point(data_Matrix)
    return data_Matrix, points, center_Data


def route_To_Order(route, data_Order):
    orders = []
    for item in data_Order:
        lat = item[5]
        lon = item[6]
        if [lat, lon] in route:
            order = item[1]
            orders.append(order)
    return orders


def haversine_distance(coord1, coord2):
    R = 6371  # Bán kính của Trái Đất trong kilômét
    lat1, lon1 = np.radians(list(coord1))
    lat2, lon2 = np.radians(list(coord2))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = R * c
    return distance


def show_radius_Cluster(data_point, data_center):
    radius = []
    for i, group in enumerate(data_point):
        max_distance = 0
        for point in group:
            distance = haversine_distance(point, data_center[i])
            if distance > max_distance:
                max_distance = distance
        radius.append(max_distance)
    radius = np.array(radius) * 1000
    return radius


def get_DataPoint(data):
    point = []
    for items in data:
        for value in items:
            if value not in point:
                point.append(value)
    return point


def show_Result(points, start_Point, matrix, name_Algorithm):
    try:
        if start_Point and start_Point not in points:
            points.append(start_Point)
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


def data_ShowMap(data_Center, data_Radius, all_Points, key):
    html_content = f"""
        <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps Cluster</title>
                <script src="https://maps.googleapis.com/maps/api/js?key={key}&callback=initMap" async defer></script>
                <script>
                    function initMap() {{
                        var map = new google.maps.Map(document.getElementById('map'), {{
                            center: {{lat: {data_Center[0][0]}, lng: {data_Center[0][1]}}}, // Điểm trung tâm ban đầu
                            zoom: 12 // Độ phóng ban đầu
                        }});
                        
                        // Hiển thị điểm trung tâm dữ liệu và đường tròn
                        for (var i = 0; i < {len(data_Center)}; i++) {{
                            var center = new google.maps.LatLng({data_Center}[i][0], {data_Center}[i][1]);
                            var marker = new google.maps.Marker({{
                            position: center,
                            map: map,
                            title: 'Data Point'
                            }});

                            var circle = new google.maps.Circle({{
                            center: center,
                            radius: {list(data_Radius)}[i],
                            strokeColor: '#FF0000',
                            strokeOpacity: 0.8,
                            strokeWeight: 2,
                            fillColor: '#d59696',
                            fillOpacity: 0.35,
                            map: map
                            }});
                        }}
                        
                        // Hiển thị tất cả điểm dữ liệu
                        {all_Points}.forEach(function (point) {{
                            var marker = new google.maps.Marker({{
                                position: new google.maps.LatLng(point[0], point[1]),
                                map: map,
                                title: 'Data Point'
                            }});
                        }});
                    }}
                </script>
            </head>
                <body>
                    <div id="map" style="height: 830px; width: 100%;">
                </body>
            </html>
            """
    return html_content


def fun_GetPointTrip(data, start_Point, num_Cluster, name_Algorithm):
    key = "AIzaSyAXiMLkRaq16MeTMVOFnYWqxDd0TCV3prU"
    data_Order = []
    data_Map = ""
    data_Matrix, data_Point, data_Center = cluster(data, num_Cluster)
    for index, value in enumerate(data_Point):
        route = show_Result(
            data_Point[index], start_Point, data_Matrix[index], name_Algorithm
        )
        data_Order.append(route)
    radius = show_radius_Cluster(data_Point, data_Center)
    all_Point = get_DataPoint(data_Point)
    data_Map = data_ShowMap(data_Center.tolist(), radius, all_Point, key)
    return data_Order


# data = [
#     [
#         "MC220509000004",
#         1230700002,
#         0.0,
#         0.0,
#         1.0,
#         10.827673713865051,
#         106.68736148070087,
#     ],
#     ["MC2204030071", 1230700003, 0.0, 0.0, 1.0, 10.844179819400372, 106.67738144346437],
#     [
#         "MC220426000001",
#         1230700004,
#         0.0,
#         0.0,
#         1.0,
#         10.845808014245465,
#         106.65698530399546,
#     ],
#     ["MC2204030078", 1230700005, 0.0, 0.0, 1.0, 10.829913344037724, 106.67070386216511],
#     ["MC2204030077", 1230700006, 0.0, 0.0, 1.0, 10.85541264037055, 106.78993997441134],
#     [
#         "MC220510000001",
#         1230700007,
#         0.0,
#         0.0,
#         1.0,
#         10.86506889143602,
#         106.80371688756779,
#     ],
#     [
#         "MC190703000012",
#         1230700008,
#         0.0,
#         0.0,
#         1.0,
#         10.854527653159472,
#         106.80939995968937,
#     ],
#     [
#         "MC190703000013",
#         1230700009,
#         0.0,
#         0.0,
#         1.0,
#         10.791102482128817,
#         106.70583697964395,
#     ],
#     [
#         "MC190703000014",
#         1230700010,
#         0.0,
#         0.0,
#         1.0,
#         10.791183609986648,
#         106.69825949982476,
#     ],
#     [
#         "MC190703000015",
#         1230700011,
#         0.0,
#         0.0,
#         1.0,
#         10.782966523027511,
#         106.69814911155156,
#     ],
#     [
#         "MC190703000016",
#         1230700012,
#         0.0,
#         0.0,
#         1.0,
#         10.775324727445424,
#         106.68628599389933,
#     ],
#     [
#         "MC190703000017",
#         1230700013,
#         0.0,
#         0.0,
#         1.0,
#         10.76892116200224,
#         106.68502692753195,
#     ],
# ]
# start_Point = [10.810174157308571, 106.66492499243704]
# num_Cluster = 3
# name_Algorithm = "Randomized Tour"
# fun_GetPointTrip(data, start_Point, num_Cluster, name_Algorithm)

# Vẽ map thêm 3 các thuật toán có thể sử dụng được:
