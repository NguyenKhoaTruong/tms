import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from geopy.distance import great_circle


class distance_Matrix:
    def __init__(self):
        print("Distacne---Matrix")

    def cal_Distance(self, point, start_point):
        point_Data = []
        for value in point:
            if value:
                value.append(start_point)
                point_Data.append(value)

        def convent_Data_Distance(point_Data):
            data = []
            for value in point_Data:
                lat = value[0]
                lon = value[1]
                data.append([lat, lon])
            return data

        data_ = convent_Data_Distance(point_Data)
        return data_

    def calculate_distances(data):
        def euclidean_distance(point1, point2):
            distances = great_circle(point1, point2).kilometers

            distances = round(distances, 3)

            return distances

        num_points = len(data)
        distances = [[0 for _ in range(num_points)] for _ in range(num_points)]

        for i in range(num_points):
            for j in range(i + 1, num_points):
                distance = euclidean_distance(data[i], data[j])
                distances[i][j] = distance
                distances[j][i] = distance
        return distances
