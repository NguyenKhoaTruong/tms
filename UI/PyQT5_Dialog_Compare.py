import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWidgets import QVBoxLayout, QDialog
from Algorithm.Cluster.Randomized_Tour import Randomized_Tour_Cluster
from Algorithm.Cluster.Nearest_Neighbor import Nearest_Neighbor_Cluster
from Algorithm.Cluster.Christofides_Algorithm import Christofides
from Process_Data.PyQT5_distanceMatrix import distance_Matrix
from Algorithm.Cluster.Brute_Force import Brute_Force_Cluster
from Algorithm.Cluster.Ant_ColonyOptimization import Ant
from Process_Data.PyQT5_Data_Real import show_Real_Data
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Algorithm.Cluster.Tabu_Search import Tabu
from Process_Data.PyQT5_Data import data_Proc
import Map_.css_Map_Route as css
from PyQt5.QtGui import QIcon
import numpy as np
from datetime import datetime, timedelta


class DialogCompare(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.web_view = QWebEngineView()
        self.data_Title = [
            "Random Tour",
            "Christofides",
            "Ant Colony",
            "Tabu Search",
            # "Brute Force",
            "Nearest Neighbor",
        ]
        self.data_Matrix = []
        self.data_Route = []
        self.ui(data)

    def ui(self, data):
        self.setWindowTitle("Compare TSP")
        self.layout_ = QVBoxLayout()
        self.setLayout(self.layout_)
        self.resize(800, 550)
        self.show_HTML(data)
        icon = QIcon("logo.ico")
        self.setWindowIcon(icon)

    def cal_Algorithm(self, point, start_Point, mode_Start, mode_Return):
        try:
            route_Random, distance_Random = self.cal_RandomTour(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(distance_Random)
            self.data_Route.append(route_Random)
            route_Chris, distance_Chris = self.cal_Christofides(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(distance_Chris)
            self.data_Route.append(route_Chris)
            route_Tabu, distance_Tabu = self.cal_Tabu(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(distance_Tabu)
            self.data_Route.append(route_Tabu)
            route_Ant, distance_Ant = self.cal_Ant(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(distance_Ant)
            self.data_Route.append(route_Ant)
            distance_Nearest, cost_Nearest = self.cal_NearestNeighbor(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(cost_Nearest)
            self.data_Route.append(distance_Nearest)
            # brute = self.cal_BruteForce(point, start_Point, mode_Start, mode_Return)
            # self.data_Matrix.append(brute)
            return self.data_Route, self.data_Matrix
        except ValueError as e:
            print("Log Error", e)

    def cal_RandomTour(self, point, start_Point, mode_Start, mode_Return):
        try:
            if mode_Start == True and start_Point not in point:
                point.insert(0, start_Point)
            distance = distance_Matrix.calculate_distances(point)
            route, cost = Randomized_Tour_Cluster.randomized_tour(
                distance, 0, mode_Return, not mode_Return
            )
            data_Route = self.convent_Path(route, point)
            return data_Route, cost
        except ValueError as e:
            print("Log Error", e)

    def convent_Path(self, path, point):
        data = []
        for i in range(len(path)):
            point_index = path[i]
            points = point[point_index]
            data.append([points[0], points[1]])
        return data

    def cal_Christofides(self, point, start_Point, mode_Start, mode_Return):
        try:
            route, cost = Christofides().use_Christofides(
                point, start_Point, mode_Return, mode_Start
            )
            return route, cost
        except ValueError as e:
            print("Log Error", e)

    def cal_Tabu(self, point, start_Point, mode_Start, mode_Return):
        try:
            cost, route = Tabu().use_Tabu(point, start_Point, mode_Return, mode_Start)
            return route, cost
        except ValueError as e:
            print("Log Error", e)

    def cal_Ant(self, point, start_Point, mode_Start, mode_Return):
        try:
            route, cost = Ant().use_Ant(point, start_Point, mode_Return, mode_Start)
            return route, cost
        except ValueError as e:
            print("Log Error", e)

    def cal_NearestNeighbor(self, point, start_Point, mode_Start, mode_Return):
        try:
            # distance_matrix, start_point_index, points, on, off
            if mode_Start == True and start_Point not in point:
                point.insert(0, start_Point)
            distance = distance_Matrix.calculate_distances(point)
            route, cost = Nearest_Neighbor_Cluster.tsp_nearest_neighbor(
                distance, 0, point, mode_Return, not mode_Return
            )
            return route, cost
        except ValueError as e:
            raise ("Log Error", e)

    # def cal_BruteForce(self, point, start_Point, mode_Start, mode_Return):
    #     try:
    #         if mode_Start == True and start_Point not in point:
    #             point.insert(0, start_Point)
    #         distance = distance_Matrix.calculate_distances(point)
    #         cost, route = Brute_Force_Cluster.brute_force_tsp(
    #             point, distance, start_Point, mode_Return, not mode_Return
    #         )
    #         return cost
    #     except ValueError as e:
    #         raise ("Log Error", e)

    def convent_Point(self, data):
        data_ = []
        for value in data:
            data_.append({"lat": value[0], "lng": value[1]})
        return data_

    def cal_Real(self, point, start_Point, modeStart, modeReturn):
        try:
            if modeStart == True and start_Point not in point:
                point.insert(0, start_Point)
            elif modeReturn == True and modeStart == True:
                point.insert(0, start_Point)
                point.append(start_Point)
            distance, time = show_Real_Data().data_Real(self.convent_Point(point))
            return distance, time
        except ValueError as e:
            print("Log Error", e)

    def hilight_Item(self, temp, matrix):
        def change_Background(x):
            return abs(x - float(temp[:-2]))

        item_Change = min(matrix, key=change_Background)
        return item_Change

    def get_Point(self, data):
        temp = []
        for items in data:
            if items not in temp:
                temp.append(items)
        return temp

    def get_ParamTime(self, data):
        data_Time = []
        start_Time = data.input_STime.currentText()
        before_Time = data.input_WBTime.text()
        service_Time = data.input_SETime.text()
        after_Time = data.input_WATime.text()
        congestion_Time = data.input_CTime.text()
        time_format = "%H:%M"
        formatted_time = datetime.strptime(start_Time, time_format)
        timer = formatted_time.time()
        data_Time.append(
            [
                timer,
                int(before_Time),
                int(service_Time),
                int(after_Time),
                congestion_Time,
            ]
        )
        return data_Time

    def calculator_ETA_ETD(self, point, time_Ship):
        try:
            time_Delivery = ""
            time = datetime.combine(datetime.today(), time_Ship[0])
            before_Time = time_Ship[1]
            service_Time = time_Ship[2]
            after_Time = time_Ship[3]
            if time_Ship[4] == "0" or time_Ship[4] == "1":
                congestion_Time = int(time_Ship[4])
            else:
                congestion_Time = float(time_Ship[4])
            for i in range(len(point)):
                origin = f"{point[i][0]},{point[i][1]}"
                destination = (
                    f"{point[i + 1][0]},{point[i + 1][1]}"
                    if i + 1 < len(point)
                    else origin
                )

                distance = show_Real_Data().get_distance(origin, destination)
                if distance is not None:
                    traffic_Time = distance + (distance * congestion_Time)
                    estimated_time = (
                        time
                        + timedelta(minutes=before_Time)
                        + timedelta(minutes=traffic_Time)
                        + timedelta(minutes=service_Time)
                        + timedelta(minutes=after_Time)
                    )
                    time = estimated_time
            start_Time = datetime.combine(datetime.today(), time_Ship[0])
            time_Delivery = self.time_Route(start_Time, time)
            return time_Delivery
        except ValueError as e:
            raise ("Log Error", e)

    def time_Route(self, start_Time, end_Time):
        time = end_Time - start_Time
        hours, remainder = divmod(time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        str_Time = f"""{hours} giờ {minutes} phút"""
        return str_Time

    def add_HTML(self, point, start_Point, modeStart, modeReturn, data):
        try:
            data_Distance = []
            data_Time = []
            list_Total = ""
            for items in self.data_Route:
                distance, time = self.cal_Real(
                    items, start_Point, modeStart, modeReturn
                )
                time__ = self.calculator_ETA_ETD(items, self.get_ParamTime(data)[0])
                data_Distance.append(distance)
                data_Time.append(time__)
            item_Change = self.hilight_Item(distance, self.data_Matrix)
            for index, value in enumerate(self.data_Title):
                list_Total += f"""
                <div class="route-main"> 
                    <div id="text-show" class={"route-min"if item_Change == self.data_Matrix[index] else "route"}>
                        <div class="title-text">{value}</br></div>
                            <div class="title-text">
                                KM - Direction: {round(self.data_Matrix[index],3)} KM </br>
                            </div>
                            <div class="title-text">
                                KM - Route: {data_Distance[index][:-2]} KM </br>
                            </div>  
                            <div class="title-text">
                                Time - Route: {data_Time[index]} </br>
                            </div>
                    </div>
                </div> 
                """

            return list_Total
        except ValueError as e:
            print("Log Error", e)

    def show_HTML(self, data):
        try:
            start_Point = data.cbStart.currentData()
            start_Point = [start_Point[1], start_Point[2]]
            modeStart = data.modeStartPoint.isChecked()
            modeReturn = data.modeReturn.isChecked()
            text_Trip = data.cbCluster.currentText()
            point = data.data_Point[int(text_Trip[-1]) - 1].tolist()
            self.cal_Algorithm(point, start_Point, modeStart, modeReturn)
            content_HTML = self.add_HTML(
                point, start_Point, modeStart, modeReturn, data
            )
            html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    {css.css_DialogCompare()}
                </head>
                <body>
                    <div class="main">
                        <div class="container">
                            {content_HTML}
                        <div>
                        <div class="tab-des">
                            <div class="normal">
                                <span class="icon-normal">•</span>
                                <span class="text-normal">Low Accuracy</span>
                            </div>
                            <div class="best">
                                <span class="icon-best">•</span>
                                <span class="text-best">High Precision</span>
                            </div>
                        </div>
                    </div>
                </body>
                </html>
                """
            self.web_view.setHtml(html)
            self.layout_.addWidget(self.web_view)
        except ValueError as e:
            print("Log Error", e)
