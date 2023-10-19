import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Algorithm.Cluster.Branch_Bound import Branch_Bound_Cluster
from Algorithm.Cluster.Brute_Force import Brute_Force_Cluster
from Algorithm.Cluster.Randomized_Tour import Randomized_Tour_Cluster
from Algorithm.Cluster.Nearest_Neighbor import Nearest_Neighbor_Cluster
from Algorithm.Cluster.Lin_Kernighan_Heuristic import Lin_Kernighan_Heuristic_Cluster
from Algorithm.Cluster.Greedy_Algorithms import Greedy_Algorithms_Cluster
from Algorithm.Cluster.Hill_Climbing import Hill_Climbing_Cluster
from Algorithm.Cluster.Tabu_Search import Tabu
from Algorithm.Cluster.Ant_ColonyOptimization import Ant
from Algorithm.Cluster.Christofides_Algorithm import Christofides
from Map_.PyQT5_Map_Route_Cluster import Show_Map_TSP_Cluster
from Process_Data.PyQT5_Route_Time import Route_Time_Min
from Caculator.PyQT5_distanceMatrix import distance_Matrix
import numpy as np
import json


class use_TSP_Cluster:
    def __init__(
        self,
        dataSelectCluster,
        dataMainWindow,
        dataOrigin,
        layoutMap,
        pointCenter,
        data_array,
        start_Point,
        on_Return,
        off_Return,
        data_ShipTo,
        mode_Start,
    ):
        dataMainWindow.btn_Back.show()
        dataMainWindow.btn_Compare.show()
        self.data_TSP = []
        self.speed = 25
        self.main_option_TSP(
            dataSelectCluster,
            dataMainWindow,
            dataOrigin,
            layoutMap,
            pointCenter,
            data_array,
            start_Point,
            on_Return,
            off_Return,
            data_ShipTo,
            mode_Start,
        )

    def convent_Data_Route(self, data):
        data_Route = []
        for coord_str in data:
            lat, lon = coord_str.split(",")
            lat, lon = float(lat), float(lon)
            data_Route.append([lat, lon])
        data_Route_New = "->".join([f"{lat:.7f},{lon:.7f}" for lat, lon in data_Route])
        return data_Route_New

    def branch_Bound_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        path, min_cost = Branch_Bound_Cluster.tsp_branch_and_bound(
            points, distances, start_Point, on, off
        )
        for_path = Branch_Bound_Cluster.format_path_to_string(path, points)
        time = Route_Time_Min.calculate_total_time(min_cost, self.speed)
        Show_Map_TSP_Cluster(
            for_path,
            min_cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def brute_Force_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        min_cost, path = Brute_Force_Cluster.brute_force_tsp(
            points, distances, start_Point, on, off
        )
        for_path = [points[i] for i in path]
        for_path = "->".join([f"{coord[0]} , {coord[1]}" for coord in for_path])
        time = Route_Time_Min.calculate_total_time(min_cost, self.speed)
        Show_Map_TSP_Cluster(
            for_path,
            min_cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def randomized_Tour_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        dataConvent = []

        point_array = np.array(points)
        start_point_index = np.where(np.all(point_array == start_Point, axis=1))[0][0]
        path, min_cost = Randomized_Tour_Cluster.randomized_tour(
            distances, start_point_index, on, off
        )
        for i in range(len(path)):
            point_index = path[i]
            point = points[point_index]
            dataConvent.append([point[0], point[1]])
        for_path = "->".join([f"{coord[0]} , {coord[1]}" for coord in dataConvent])
        time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

        Show_Map_TSP_Cluster(
            for_path,
            min_cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def nearest_Neighbor_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        start_point_index = np.argmin(
            np.linalg.norm(np.array(points) - np.array(start_Point), axis=1)
        )
        path, min_cost = Nearest_Neighbor_Cluster.tsp_nearest_neighbor(
            distances, start_point_index, points, on, off
        )
        path = "->".join([f"{coord[0]} , {coord[1]}" for coord in path])
        time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

        Show_Map_TSP_Cluster(
            path,
            min_cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def line_Kernighan_Heuristic_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        start_point_index = np.argmin(
            np.linalg.norm(np.array(points) - np.array(start_Point), axis=1)
        )
        path, min_cost = Lin_Kernighan_Heuristic_Cluster.lin_kernighan(
            points, distances, on, off, start_point_index
        )
        for_path = [
            Lin_Kernighan_Heuristic_Cluster.format_lat_lon(points[i]) for i in path
        ]
        data_Route = self.convent_Data_Route(for_path)
        time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

        Show_Map_TSP_Cluster(
            data_Route,
            min_cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def greedy_Algorithm_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        path, min_cost = Greedy_Algorithms_Cluster.greedy_tsp(
            start_Point, points, distances, on, off
        )

        def format_lat_lon(point):
            return "{:.8f}, {:.8f}".format(point[0], point[1])

        for_path = [format_lat_lon(point) for point in path]
        for_path = self.convent_Data_Route(for_path)
        time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

        Show_Map_TSP_Cluster(
            for_path,
            min_cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def tabu_Search(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        cost, route = Tabu().use_Tabu(points, start_Point, on, mode_Start)

        route = "->".join([f"{coord[0]} , {coord[1]}" for coord in route])
        time = 0  # Hiện tại chưa cần tính time
        Show_Map_TSP_Cluster(
            route,
            cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def ant_Colony(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        route, cost = Ant().use_Ant(points, start_Point, on, mode_Start)

        route = "->".join([f"{coord[0]} , {coord[1]}" for coord in route])
        time = 0  # Hiện tại chưa cần tính time
        Show_Map_TSP_Cluster(
            route,
            cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def christofides(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        route, cost = Christofides().use_Christofides(
            points, start_Point, on, mode_Start
        )

        route = "->".join([f"{coord[0]} , {coord[1]}" for coord in route])
        time = 0  # Hiện tại chưa cần tính time
        Show_Map_TSP_Cluster(
            route,
            cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def hill_Climbing_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        num_iterations = 1000
        path, min_cost = Hill_Climbing_Cluster.hill_climbing(
            distances, start_Point, points, on, off, num_iterations
        )

        for_path = Hill_Climbing_Cluster.convert_to_lat_lon(path, points)
        for_path = "->".join([f"{coord[0]} , {coord[1]}" for coord in for_path])

        time = Route_Time_Min.calculate_total_time(min_cost, self.speed)

        Show_Map_TSP_Cluster(
            for_path,
            min_cost,
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def opt_TSP(
        self,
        points,
        distances,
        start_Point,
        layoutMap,
        pointCenter,
        data_array,
        on,
        off,
        data_ShipTo,
        mode_Start,
    ):
        def calculate_total_distance(points, route, on, off):
            total_distance = 0
            if on == True:
                for i in range(len(route) - 1):
                    total_distance += distances[route[i]][route[i + 1]]
                total_distance += distances[route[-1]][route[0]]
            elif off == True:
                for i in range(len(route) - 1):
                    total_distance += distances[route[i]][route[i + 1]]
            return total_distance

        def two_opt(route):
            best_route = route.copy()
            improved = True
            while improved:
                improved = False
                for i in range(1, len(route) - 1):
                    for j in range(i + 1, len(route)):
                        new_route = route[:i] + route[i : j + 1][::-1] + route[j + 1 :]
                        new_distance = calculate_total_distance(
                            points, new_route, on, off
                        )
                        if new_distance < calculate_total_distance(
                            points, best_route, on, off
                        ):
                            best_route = new_route
                            improved = True
                route = best_route
            if on == True:
                best_route.append(best_route[0])
            return best_route

        # Fix 07/10/23023
        # if mode_Start == True:
        #     points.insert(0, start_Point)
        num_points = len(points)
        initial_route = list(range(num_points))
        path = two_opt(initial_route)
        for_path = [points[i] for i in path]
        for_path = "->".join([f"{coord[0]} , {coord[1]}" for coord in for_path])
        time = Route_Time_Min.calculate_total_time(
            calculate_total_distance(points, path, on, off), self.speed
        )
        Show_Map_TSP_Cluster(
            for_path,
            calculate_total_distance(points, path, on, off),
            layoutMap,
            pointCenter,
            time,
            data_array,
            data_ShipTo,
            mode_Start,
            on,
        )

    def main_option_TSP(
        self,
        data,
        dataMainWindow,
        dataOrigin,
        layoutMap,
        pointCenter,
        data_array,
        start_Point,
        on_Return,
        off_Return,
        data_ShipTo,
        mode_Start,
    ):
        for value in data:
            self.data_TSP.append([value[0], value[1]])
        if mode_Start == True:
            self.data_TSP.append(start_Point)
            points = self.data_TSP
        else:
            points = self.data_TSP
            start_Point = points[0]
        distances = distance_Matrix.calculate_distances(points)

        if dataMainWindow.cbTSP.currentText() == "Branch And Bound":
            self.branch_Bound_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )

        elif dataMainWindow.cbTSP.currentText() == "Brute Force":
            self.brute_Force_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )

        elif dataMainWindow.cbTSP.currentText() == "Randomized Tour":
            self.randomized_Tour_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )

        elif dataMainWindow.cbTSP.currentText() == "Nearest Neighbor":
            self.nearest_Neighbor_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )

        elif dataMainWindow.cbTSP.currentText() == "Line Kernighan Heuristic":
            self.line_Kernighan_Heuristic_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )

        elif dataMainWindow.cbTSP.currentText() == "Greedy Algorithm":
            self.greedy_Algorithm_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )

        elif dataMainWindow.cbTSP.currentText() == "Hill Climbing":
            self.hill_Climbing_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )

        elif dataMainWindow.cbTSP.currentText() == "2-OPT":
            self.opt_TSP(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )
        elif dataMainWindow.cbTSP.currentText() == "Tabu Search":
            self.tabu_Search(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )
        elif dataMainWindow.cbTSP.currentText() == "Ant Colony":
            self.ant_Colony(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )
        elif dataMainWindow.cbTSP.currentText() == "Christofides":
            self.christofides(
                points,
                distances,
                start_Point,
                layoutMap,
                pointCenter,
                data_array,
                on_Return,
                off_Return,
                data_ShipTo,
                mode_Start,
            )
