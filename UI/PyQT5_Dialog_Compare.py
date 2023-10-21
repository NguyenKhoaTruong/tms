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


class DialogCompare(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.web_view = QWebEngineView()
        self.data_Title = [
            "Random Tour",
            "Christofides",
            "Ant Colony",
            "Tabu Search",
            "Brute Force",
            "Nearest Neighbor",
        ]
        self.data_Matrix = []
        self.ui(data)

    def ui(self, data):
        self.setWindowTitle("Compare TSP")
        self.layout_ = QVBoxLayout()
        self.setLayout(self.layout_)
        self.resize(800, 600)
        self.show_HTML(data)
        icon = QIcon("logo.ico")
        self.setWindowIcon(icon)

    def cal_Algorithm(self, point, start_Point, mode_Start, mode_Return):
        try:
            random_Tour = self.cal_RandomTour(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(random_Tour)
            chris_To = self.cal_Christofides(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(chris_To)
            tabu = self.cal_Tabu(point, start_Point, mode_Start, mode_Return)
            self.data_Matrix.append(tabu)
            ant = self.cal_Ant(point, start_Point, mode_Start, mode_Return)
            self.data_Matrix.append(ant)
            nearest = self.cal_NearestNeighbor(
                point, start_Point, mode_Start, mode_Return
            )
            self.data_Matrix.append(nearest)
            brute = self.cal_BruteForce(point, start_Point, mode_Start, mode_Return)
            self.data_Matrix.append(brute)
            return self.data_Matrix
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
            return cost
        except ValueError as e:
            print("Log Error", e)

    def cal_Christofides(self, point, start_Point, mode_Start, mode_Return):
        try:
            route, cost = Christofides().use_Christofides(
                point, start_Point, mode_Return, mode_Start
            )
            return cost
        except ValueError as e:
            print("Log Error", e)

    def cal_Tabu(self, point, start_Point, mode_Start, mode_Return):
        try:
            cost, route = Tabu().use_Tabu(point, start_Point, mode_Return, mode_Start)
            return cost
        except ValueError as e:
            print("Log Error", e)

    def cal_Ant(self, point, start_Point, mode_Start, mode_Return):
        try:
            route, cost = Ant().use_Ant(point, start_Point, mode_Return, mode_Start)
            return cost
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
            return cost
        except ValueError as e:
            raise ("Log Error", e)

    def cal_BruteForce(self, point, start_Point, mode_Start, mode_Return):
        try:
            if mode_Start == True and start_Point not in point:
                point.insert(0, start_Point)
            distance = distance_Matrix.calculate_distances(point)
            cost, route = Brute_Force_Cluster.brute_force_tsp(
                point, distance, start_Point, mode_Return, not mode_Return
            )
            return cost
        except ValueError as e:
            raise ("Log Error", e)

    def convent_Point(self, data):
        data_ = []
        for value in data:
            data_.append({"lat": value[0], "lng": value[1]})
        return data_

    def cal_Real(self, point, start_Point, modeStart, modeReturn):
        try:
            if modeStart == True and start_Point not in point:
                point.insert(0, start_Point)
            elif modeReturn == True and modeStart == True and start_Point not in point:
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

    def add_HTML(self, point, start_Point, modeStart, modeReturn):
        try:
            list_Total = ""
            distance, time = self.cal_Real(
                self.get_Point(point), start_Point, modeStart, modeReturn
            )
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
                                KM - Route: {distance} KM </br>
                            </div>  
                            <div class="title-text">
                                Time - Route: {time} </br>
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
            content_HTML = self.add_HTML(point, start_Point, modeStart, modeReturn)
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
                                <span class="text-normal">Normal</span>
                            </div>
                            <div class="best">
                                span class="icon-best">•</span>
                                <span class="text-best">Best</span>
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
