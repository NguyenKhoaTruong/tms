from sklearn.cluster import KMeans
import numpy as np


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
        lat = items[5]
        lon = items[6]
        point.append([lat, lon])
    return point


def data_ShowMap(data_Center, data_Radius, all_Points):
    html_content = f"""<script>function initMap(){{var map = new google.maps.Map(document.getElementById('map'),{{center:{{lat:{data_Center[0][0]},lng:{data_Center[0][1]}}},zoom:}});for (var i=0; i<{len(data_Center)};i++){{var center =new google.maps.LatLng({data_Center}[i][0],{data_Center}[i][1]);var marker =new google.maps.Marker({{position:center,map:map,title:'Data Point'}});var circle =new google.maps.Circle({{center:center,radius:{list(data_Radius)}[i],strokeColor:'#FF0000',strokeOpacity:0.8,strokeWeight:2,fillColor:'#d59696',fillOpacity: 0.35,map:map}});}} {all_Points}.forEach(function(point){{var marker =new google.maps.Marker({{position:new google.maps.LatLng(point[0],point[1]),map:map,title:'Data Point'}});}});}}</script>"""
    return html_content


def fun_GetPointTrip(data, num_Cluster):
    try:
        data_Map = ""
        data_Matrix, data_Point, data_Center = cluster(data, num_Cluster)
        radius = show_radius_Cluster(data_Point, data_Center)
        all_Point = get_DataPoint(data)
        data_Map = data_ShowMap(data_Center.tolist(), radius, all_Point)
        return data_Map, data_Point, data_Matrix
    except ValueError as e:
        raise ("Log Error", e)
