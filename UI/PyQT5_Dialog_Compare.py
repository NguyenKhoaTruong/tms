import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWidgets import QVBoxLayout, QDialog
from Algorithm.Cluster.Randomized_Tour import Randomized_Tour_Cluster
from Algorithm.Cluster.Christofides_Algorithm import Christofides
from Algorithm.Cluster.Ant_ColonyOptimization import Ant
from Process_Data.PyQT5_distanceMatrix import distance_Matrix
from Process_Data.PyQT5_Data_Real import show_Real_Data
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Algorithm.Cluster.Tabu_Search import Tabu
from Process_Data.PyQT5_Data import data_Proc
import Map_.css_Map_Route as css
import numpy as np


class DialogCompare(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.web_view = QWebEngineView()
        self.data_Title = ["Random Tour", "Christofides", "Ant Colony", "Tabu Search"]
        self.data_Matrix = []
        self.ui(data)

    def ui(self, data):
        self.setWindowTitle("Compare TSP")
        self.layout_ = QVBoxLayout()
        self.setLayout(self.layout_)
        self.resize(600, 450)
        self.show_HTML(data)

    def cal_Algorithm(self, point, start_Point, mode_Start, mode_Return):
        try:
            data = [
                point,
                start_Point,
                mode_Start,
                mode_Return,
            ]  # cấu hình code gọn hơn
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
            return self.data_Matrix
        except ValueError as e:
            print("Log Error", e)

    def cal_RandomTour(self, point, start_Point, mode_Start, mode_Return):
        print("check value type point", type(point))
        try:
            if mode_Start == True and start_Point not in point:
                point.insert(0, start_Point)  # Sai dòng này là np adarrray
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

    def add_HTML(self, point, start_Point, modeStart, modeReturn):
        list_Total = ""
        distance, time = self.cal_Real(point, start_Point, modeStart, modeReturn)
        for index, value in enumerate(self.data_Title):
            list_Total += f"""
            <div class="route-main"> 
                <div id="text-show" class="route">
                    <div class="title-text">{value}</br></div>
                        <div class="title-text">
                            KM - Direction: {self.data_Matrix[index]} KM </br>
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

    def cal_Real(self, point, start_Point, modeStart, modeReturn):
        try:
            if modeStart == True and start_Point not in point:
                point.insert(0, start_Point)
            elif modeReturn == True and modeStart == True and start_Point not in point:
                point.insert(0, start_Point)
                point.append(start_Point)
            distance, time = show_Real_Data().data_Real(point)
            return distance, time
        except ValueError as e:
            print("Log Error", e)

    def show_HTML(self, data):
        start_Point = data.cbStart.currentData()
        start_Point = [start_Point[1], start_Point[2]]
        modeStart = data.modeStartPoint.isChecked()
        modeReturn = data.modeReturn.isChecked()
        point = data.selected_cluster
        self.cal_Algorithm(point, start_Point, modeStart, modeReturn)
        html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                {css.css_DialogCompare()}
            </head>
            <body>
                <div class="container">
                    {self.add_HTML(point, start_Point, modeStart, modeReturn)}
                <div>
            </body>
            </html>
            """
        self.web_view.setHtml(html)
        self.layout_.addWidget(self.web_view)
        # giải phóng bộ nhớ khi tắt
        self.deleteLater()
