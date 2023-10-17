import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Algorithm.Cluster.Brute_Force import Brute_Force_Cluster
from Algorithm.Cluster.Branch_Bound import Branch_Bound_Cluster
from Algorithm.Cluster.Greedy_Algorithms import Greedy_Algorithms_Cluster
from Algorithm.Cluster.Hill_Climbing import Hill_Climbing_Cluster
from Algorithm.Cluster.Lin_Kernighan_Heuristic import Lin_Kernighan_Heuristic_Cluster
from Algorithm.Cluster.Nearest_Neighbor import Nearest_Neighbor_Cluster
from Algorithm.Cluster.OPT import two_OPT_Cluster
from Algorithm.Cluster.Randomized_Tour import Randomized_Tour_Cluster
from Process_Data.PyQT5_distanceMatrix import distance_Matrix
from decimal import Decimal, ROUND_DOWN
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Compare_Algorithm.PyQT5_Data_Compare import Data_Compare
import itertools


class Compare:
    def __init__(self, Points, Center, cb_TSP, data_Center, data_Weight, dataLayout):
        self.web_View_Compare = QWebEngineView()
        self.values_Title = []
        self.distance = []
        self.distance_Brute = []
        self.distance_Branch = []
        self.distance_Greedy = []
        self.distance_Hill = []
        self.distance_Lin = []
        self.distance_Nearest = []
        self.distance_OPT = []
        self.distance_Randomized = []
        self.show_Layout(Points, Center, cb_TSP, data_Center, data_Weight, dataLayout)

    def get_Title_TSP(self, cb_TSP):
        data_Title = []
        for index in range(cb_TSP.count()):
            data_Title.append(cb_TSP.itemText(index))
        return data_Title

    def caculator_Distance(self, data_point, data_start):
        distance_Trip = []  # data_point là tổng  các giá trị cụm lấy vào.
        arr_distance = []
        for value in data_point:
            distance_matrix = distance_Matrix.calculate_distances(value)
            arr_distance.append(distance_matrix)
        for index, value in enumerate(data_point):
            self.distance_Brute.append(
                self.distance_Brute_Force_Cluster(value, arr_distance[index], value[0])
            )

            self.distance_Branch.append(
                self.distance_Branch_Bound_Cluster(value, arr_distance[index], value[0])
            )

            self.distance_Greedy.append(
                self.distance_Greedy_Algorithms_Cluster(
                    value[0], value, arr_distance[index]
                )
            )

            self.distance_Hill.append(
                self.distance_Hill_Climbing_Cluster(
                    arr_distance[index], value[0], value, 1000
                )
            )

            self.distance_Lin.append(
                self.distance_Lin_Kernighan_Heuristic_Cluster(
                    value, arr_distance[index], 0
                )
            )

            self.distance_Nearest.append(
                self.distance_Nearest_Neighbor_Cluster(arr_distance[index], 0, value)
            )

            self.distance_OPT.append(
                self.distance_two_OPT_Cluster(value, arr_distance[index])
            )

            self.distance_Randomized.append(
                self.distance_Randomized_Tour_Cluster(arr_distance[index], 0)
            )

        distance_Trip.extend(
            [
                self.distance_Brute,
                self.distance_Branch,
                self.distance_Greedy,
                self.distance_Hill,
                self.distance_Lin,
                self.distance_Nearest,
                self.distance_OPT,
                self.distance_Randomized,
            ]
        )
        return distance_Trip

    def distance_Brute_Force_Cluster(self, points, distances, start_point):
        distance_Brute, path = Brute_Force_Cluster.brute_force_tsp(
            points, distances, start_point, False, True
        )

        return distance_Brute

    def distance_Branch_Bound_Cluster(self, points, distances, start_point):
        path, distance_Branch = Branch_Bound_Cluster.tsp_branch_and_bound(
            points, distances, start_point, False, True
        )

        return distance_Branch

    def distance_Greedy_Algorithms_Cluster(self, start_point, points, distance):
        path, distance_Greedy = Greedy_Algorithms_Cluster.greedy_tsp(
            start_point, points, distance, False, True
        )

        return distance_Greedy

    def distance_Hill_Climbing_Cluster(self, distances, start_point, points, num):
        path, distance_Hill = Hill_Climbing_Cluster.hill_climbing(
            distances, start_point, points, num, False, True
        )

        return distance_Hill

    def distance_Lin_Kernighan_Heuristic_Cluster(self, points, distances, start):
        path, distance_Lin = Lin_Kernighan_Heuristic_Cluster.lin_kernighan(
            points, distances, False, True, start
        )

        return distance_Lin

    def distance_Nearest_Neighbor_Cluster(self, distances, start_point, points):
        path, distance_Nearest = Nearest_Neighbor_Cluster.tsp_nearest_neighbor(
            distances, start_point, points, False, True
        )

        return distance_Nearest

    def distance_two_OPT_Cluster(self, points, distances):
        def route_start_point(initial_route, point_start):
            best_distance = float("inf")
            best_order = []
            for perm in itertools.permutations(initial_route):
                current_order = [point_start] + list(perm)
                optimized_order = two_OPT_Cluster.two_opt(
                    current_order, distances, points
                )
                optimized_distance = two_OPT_Cluster.calculate_total_distance(
                    optimized_order, distances
                )

                if optimized_distance < best_distance:
                    best_distance = optimized_distance
                    best_order = optimized_order.copy()
            return best_distance, best_order

        points_start = 0

        num_points = len(points)

        initial_route = list(range(num_points))

        initial_route.remove(points_start)

        distance_OPT, route = route_start_point(initial_route, points_start)

        return distance_OPT

    def distance_Randomized_Tour_Cluster(self, distance, start_point):
        path, distance_Random = Randomized_Tour_Cluster.randomized_tour(
            distance, start_point, False, True
        )

        return distance_Random

    def show_All_Trip_TSP(
        self, Points, Center, cb_TSP, data_Center, data_Weight, dataLayout
    ):
        self.values_Title = self.get_Title_TSP(cb_TSP)

        self.distance = self.caculator_Distance(Points, Center)
        list_Option = ""
        main_String = ""
        for index, value in enumerate(data_Weight):
            sum_kg = 0
            sum_m3 = 0
            for item in value:
                volume = item[0]
                weight = item[1]
                sum_kg += volume
                sum_m3 += weight
            list_Option += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{self.distance[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(value)} - Orders:{len(value)} 
            </div>
            """

        for index_, value_ in enumerate(self.values_Title):
            main_String += f"""
             <div class=\"container\"> 
                <div class=\"tripline\">
                    <div class=\"title\">
                        {value_}
                        <div class=\"event\">
                            <div class="event-date">Trip: {len(data_Center)}</div>
                                <ul class="sub-events">
                                    <li class=\"sub-event\">
                                        {list_Option}
                                    </li>
                                </ul>
                        </div>
                    </div>
                </div>
            </div>
            """
        # print('check value main string',main_String)
        return main_String

    def show_Layout(self, Points, Center, cb_TSP, data_Center, data_Weight, dataLayout):
        distance = self.caculator_Distance(Points, Center)
        Data_Compare.show_(
            self.web_View_Compare, dataLayout, distance, data_Weight, Center
        )
