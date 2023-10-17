from geopy.distance import great_circle
from sklearn.cluster import KMeans
import numpy as np
import itertools
def format_path_to_string(path, points):
    path_String = []
    for i in range(len(path)):
        lat, lon = points[path[i]]
        path_String.append([lat, lon])
    return path_String
def convert_Data(data_Cluster):
    data_array = np.array(data_Cluster)     
    array_Matrix = np.array([[item[2], item[3], float(item[5]), float(item[6])] for item in data_array]) 
    return data_array,array_Matrix 
def divide_Data(data_Cluster):
    data_Select,matrix_Select=convert_Data(data_Cluster)
    num_clusters=0
    if len(data_Select)>10 and len(data_Select)<=15:
        num_clusters = 3
    elif len(data_Select)>15 and len(data_Select)<=25:
        num_clusters= 5
    return num_clusters
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
def cluster(data_Cluster):
    data_Matrix=[]
    data_Point=[]
    num_clusters=divide_Data(data_Cluster)
    data,matrix_data=convert_Data(data_Cluster)
    kmeans = KMeans(n_clusters=int(num_clusters))
    kmeans.fit(matrix_data)

    label_Data=kmeans.labels_
    for i in range(int(num_clusters)):
        cluster_data = [data_Cluster[j] for j in range(len(data_Cluster)) if label_Data[j] == i]
        data_Matrix.append(cluster_data)
    for i in range(int(num_clusters)):
        cluster_points = matrix_data[label_Data == i]
        data_Point.append(cluster_points)
    points=convent_Data_Point(data_Matrix) 
    return data_Matrix,points
def route_To_Order(route, data_Order):
    orders=[]
    for item in data_Order:
        lat = item[5]
        lon = item[6]
        if [lat, lon] in route:
            order=item[1]
            orders.append(order)
    return orders
def show_Result(points,start_Point,matrix):
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
        return shortest_distance, shortest_route
    points.append(start_Point)
    distance = calculate_distances(points)
    cost, route = brute_force_tsp(points, distance, start_Point)
    route_ = format_path_to_string(route, points)
    route_Order = route_To_Order(route_,matrix)
    return route_Order
def fun_GetPointTrip(data,start_Point):
    data_Order=[]
    data_Matrix,data_Point = cluster(data)
    num_Trip = len(data_Matrix)
    for index,value in enumerate(data_Point):
        route=show_Result(data_Point[index],start_Point,data_Matrix[index])
        data_Order.append(route)
    return data_Order
# data=[
#     ['MC220509000004',1230700002,0.0,0.0,1.0,10.771136,106.695072],
#     ['MC2204030071',1230700003,0.0,0.0,1.0,10.447162,106.327136],
#     ['MC220426000001',1230700004,0.0,0.0,1.0,10.851344 ,104.704646],
#     ['MC2204030078',1230700005,0.0,0.0,1.0,10.423718 , 106.158803],
#     ['MC2204030077',1230700006,0.0,0.0,1.0,10.916539  ,106.106612],
#     ['MC220510000001',1230700007,0.0,0.0,1.0,10.858458 , 108.388389],
#     ['MC190703000012',1230700008,0.0,0.0,1.0,10.824141,  106.692206],
#     ['MC190703000013',1230700009,0.0,0.0,1.0,10.824257 , 106.692249],
#     ['MC190703000014',1230700010,0.0,0.0,1.0,10.833772 , 106.670660],
#     ['MC190703000015',1230700011,0.0,0.0,1.0,10.754418 , 106.651638],
#     ['MC190703000016',1230700012,0.0,0.0,1.0,10.737763 , 106.725514],
#     ['MC190703000017',1230700013,0.0,0.0,1.0,10.780984,  106.631563]
# ]
# start_Point=[10.447161,106.327116]
# fun_GetPointTrip(data,start_Point)


