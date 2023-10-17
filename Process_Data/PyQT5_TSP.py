import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Algorithm.No_Cluster.PyQT5_Branch_Bound import Branch_Bound
from Algorithm.No_Cluster.PyQT5_Brute_Force import Brute_Force
from Algorithm.No_Cluster.PyQT5_Randomized_Tour import Randomized_Tour
from Algorithm.No_Cluster.PyQT5_Nearest_Neighbor import Nearest_Neighbor
from Algorithm.No_Cluster.PyQT5_Lin_Kernighan_Heuristic import Lin_Kernighan_Heuristic
from Algorithm.No_Cluster.PyQT5_Greedy_Algorithms import Greedy_Algorithms
from Algorithm.No_Cluster.PyQT5_Hill_Climbing import Hill_Climbing
from Algorithm.No_Cluster.PyQT5_OPT import two_OPT
from Map_.PyQT5_Map_Route import Show_Map_TSP
from Process_Data.PyQT5_Route_Time import Route_Time_Min
from Caculator.PyQT5_Data_Real import show_Real_Data
from Caculator.PyQT5_distanceMatrix import distance_Matrix

import numpy as np
import itertools


class use_TSP:
    def __init__(
        self,
        dataSelectCluster,
        dataMainWindow,
        dataOrigin,
        layoutMap,
        data_array,
        on,
        off,
        start_Point,
    ):
        self.data_TSP = []
        self.speed = 25
        self.main_option_TSP(
            dataSelectCluster,
            dataMainWindow,
            dataOrigin,
            layoutMap,
            data_array,
            on,
            off,
            start_Point,
        )

    def convert_String_Route(self, data):
        coordinates_str = data.split("->")
        data_New = []
        for coord_str in coordinates_str:
            lat, lon = coord_str.split(",")
            lat, lon = float(lat), float(lon)
            data_New.append([lat, lon])
        return data_New

    def convent_Data_Route(self, data):
        data_Route = []
        for coord_str in data:
            lat, lon = coord_str.split(",")
            lat, lon = float(lat), float(lon)
            data_Route.append([lat, lon])

        # Chuyển đổi dữ liệu thành chuỗi
        data_Route_New = "->".join([f"{lat:.7f},{lon:.7f}" for lat, lon in data_Route])
        return data_Route_New

    def main_option_TSP(
        self,
        data,
        dataMainWindow,
        dataOrigin,
        layoutMap,
        data_array,
        on,
        off,
        start_Point,
    ):
        for value in data:
            self.data_TSP.append([value[0], value[1]])
        self.data_TSP.append(start_Point)
        distances = distance_Matrix.calculate_distances(
            self.data_TSP
        )  # Tính toán khoảng cách giữa các điểm:

        points = self.data_TSP

        if dataMainWindow.cbTSP.currentText() == "Branch And Bound":
            path, min_cost = Branch_Bound.tsp_branch_and_bound(
                points, distances, start_Point, on, off
            )
            for_path = Branch_Bound.format_path_to_string(path, points)
            dataMap = for_path.split("->")

            dataResult = []

            for value in dataMap:
                lat, lon = value.split(",")
                lat = float(lat)
                lon = float(lon)
                dataResult.append((lat, lon))

            time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

            distance_Real, time_Real = show_Real_Data().convent_route(for_path)
            Show_Map_TSP(for_path, min_cost, layoutMap, time, distance_Real, time_Real)

        elif dataMainWindow.cbTSP.currentText() == "Brute Force":
            min_cost, path = Brute_Force.brute_force_tsp(
                points, distances, start_Point, on, off
            )

            for_path = [points[i] for i in path]
            for_path = "->".join([f"{coord[0]} , {coord[1]}" for coord in for_path])
            time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

            distance_Real, time_Real = show_Real_Data().convent_route(for_path)
            Show_Map_TSP(for_path, min_cost, layoutMap, time, distance_Real, time_Real)

        elif dataMainWindow.cbTSP.currentText() == "Randomized Tour":
            dataConvent = []
            point_array = np.array(points)
            start_point_index = np.where(np.all(point_array == start_Point, axis=1))[0][
                0
            ]

            path, min_cost = Randomized_Tour.randomized_tour(
                distances, start_point_index, on, off
            )
            for i in range(len(path)):
                point_index = path[i]
                point = points[point_index]
                dataConvent.append([point[0], point[1]])
            for_path = "->".join([f"{coord[0]} , {coord[1]}" for coord in dataConvent])

            time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

            distance_Real, time_Real = show_Real_Data().convent_route(for_path)
            Show_Map_TSP(for_path, min_cost, layoutMap, time, distance_Real, time_Real)

        elif dataMainWindow.cbTSP.currentText() == "Nearest Neighbor":
            start_point_index = np.argmin(
                np.linalg.norm(np.array(points) - np.array(start_Point), axis=1)
            )

            path, min_cost = Nearest_Neighbor.tsp_nearest_neighbor(
                distances, start_point_index, points, on, off
            )
            path = "->".join([f"{coord[0]} , {coord[1]}" for coord in path])
            time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

            distance_Real, time_Real = show_Real_Data().convent_route(path)
            Show_Map_TSP(path, min_cost, layoutMap, time, distance_Real, time_Real)

        elif dataMainWindow.cbTSP.currentText() == "Line Kernighan Heuristic":
            start_point_index = np.argmin(
                np.linalg.norm(np.array(points) - np.array(start_Point), axis=1)
            )
            path, min_cost = Lin_Kernighan_Heuristic.lin_kernighan(
                points, distances, on, off, start_point_index
            )

            for_path = [
                Lin_Kernighan_Heuristic.format_lat_lon(points[i]) for i in min_cost
            ]
            data_Route = self.convent_Data_Route(for_path)

            time = Route_Time_Min.calculate_total_time(min_cost, self.speed)
            distance_Real, time_Real = show_Real_Data().convent_route(
                "->".join(for_path)
            )

            Show_Map_TSP(
                data_Route, min_cost, layoutMap, time, distance_Real, time_Real
            )

        elif dataMainWindow.cbTSP.currentText() == "Greedy Algorithm":
            # Tìm thứ tự và tổng khoảng cách tối thiểu
            path, min_cost = Greedy_Algorithms.greedy_tsp(
                start_Point, points, distances, on, off
            )

            # Chuyển đổi min_path sang dạng lat, lon
            def format_lat_lon(point):
                return "{:.8f}, {:.8f}".format(point[0], point[1])

            formatted_min_path = [format_lat_lon(point) for point in path]
            data_Route = self.convent_Data_Route(formatted_min_path)

            time = Route_Time_Min.calculate_total_time(min_cost, self.speed)
            distance_Real, time_Real = show_Real_Data().convent_route(data_Route)

            Show_Map_TSP(
                data_Route, min_cost, layoutMap, time, distance_Real, time_Real
            )

        elif dataMainWindow.cbTSP.currentText() == "Hill Climbing":
            num_iterations = 1000
            path, min_cost = Hill_Climbing.hill_climbing(
                distances, start_Point, points, on, off, num_iterations
            )

            # Convert best_order to lat and lon
            best_lat_lon_order = Hill_Climbing.convert_to_lat_lon(path, points)
            for_path = "->".join(
                [f"{coord[0]} , {coord[1]}" for coord in best_lat_lon_order]
            )
            time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

            distance_Real, time_Real = show_Real_Data().convent_route(for_path)
            Show_Map_TSP(for_path, min_cost, layoutMap, time, distance_Real, time_Real)

        elif dataMainWindow.cbTSP.currentText() == "2-OPT":

            def route_start_point(initial_route, point_start):
                best_distance = float("inf")
                best_order = []
                for perm in itertools.permutations(initial_route):
                    current_order = [point_start] + list(perm)
                    current_distance = two_OPT.calculate_total_distance(
                        points, current_order, on, off, distances
                    )

                    optimized_order = two_OPT.two_opt(
                        current_order, distances, points, on, off
                    )
                    optimized_distance = two_OPT.calculate_total_distance(
                        points, optimized_order, on, off, distances
                    )

                    if optimized_distance < best_distance:
                        best_distance = optimized_distance
                        best_order = optimized_order.copy()
                return best_distance, best_order

            # Tạo lộ trình ban đầu

            points_start = points.index(start_Point)
            num_points = len(points)
            initial_route = list(range(num_points))
            initial_route.remove(
                points_start
            )  # xóa điểm bắt đầu trong danh sách route

            path = two_OPT.two_opt(initial_route, distances, points, on, off)
            distance_2opt, path = route_start_point(initial_route, points_start)

            optimized_points = [points[i] for i in path]
            optimized_points = "->".join(
                [f"{coord[0]} , {coord[1]}" for coord in optimized_points]
            )

            time = Route_Time_Min.calculate_total_time(
                two_OPT.calculate_total_distance(points, path, on, off, distances),
                self.speed,
            )
            distance_Real, time_Real = show_Real_Data().convent_route(optimized_points)

            Show_Map_TSP(
                optimized_points,
                two_OPT.calculate_total_distance(points, path, on, off, distances),
                layoutMap,
                time,
                distance_Real,
                time_Real,
            )
