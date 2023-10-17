import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Algorithm.Cluster.Randomized_Tour import Randomized_Tour_Cluster
from Algorithm.Cluster.Brute_Force import Brute_Force_Cluster
from Algorithm.Cluster.Nearest_Neighbor import Nearest_Neighbor_Cluster
from Process_Data.PyQT5_distanceMatrix import distance_Matrix
import time


class Process_Data_Small:
    def __init__(self):
        print("Process Data")

    def use_NearestNeighbor(self, distance_matrix, data_point):
        try:
            data = []
            # data_Split = self.split_Data(data_point)
            for point, distance in zip(data_point, distance_matrix):
                route, distance_bf = Nearest_Neighbor_Cluster.tsp_nearest_neighbor(
                    distance, 0, point, True, False
                )
                data.append(round(distance_bf, 3))
            return data
        except ValueError as e:
            print("Check Log Error", e)

    def split_Data(self, point):
        try:
            data_Point = []
            data_Distance = []
            for item_Point in point:
                if len(item_Point) > 20 and len(item_Point) < 50:
                    index_Split = len(item_Point) // 3
                    index_TwoSplit = 2 * index_Split

                    point_Index = item_Point[:index_Split]
                    point_Center = item_Point[index_Split - 1 : index_TwoSplit]
                    point_End = item_Point[index_TwoSplit - 1 :]

                    data_Point.extend([point_Index, point_Center, point_End])
                    data_Distance = self.cal_Distance(data_Point)
                else:
                    print("Công Đoạn Tiếp Theo")
            # Tính kết quả thuật toán:
            total = self.use_Algorithm(data_Point, data_Distance)
            return total
        except ValueError as e:
            print("Log Error", e)

    def cal_Distance(self, point):
        try:
            distance = []
            for value in point:
                data_Distance = distance_Matrix.calculate_distances(value)
                distance.append(data_Distance)
            return distance
        except ValueError as e:
            print("Log Error", e)

    def use_Algorithm(self, point, distance):
        try:
            temp = 0
            for itemP, itemD in zip(point, distance):
                start_Point = itemP[0]
                distance_, route = Brute_Force_Cluster.brute_force_tsp(
                    itemP, itemD, start_Point, False, True
                )
                temp += distance_
            return temp
        except ValueError as e:
            print("Log Error", e)


# cụm 2 :81
# cụm 3 :52
