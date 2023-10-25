import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Algorithm.Cluster.Brute_Force import Brute_Force_Cluster
from Algorithm.Cluster.Randomized_Tour import Randomized_Tour_Cluster
from Process_Data.PyQT5_ProcessData import Process_Data_Small
from Process_Data.PyQT5_distanceMatrix import distance_Matrix
from decimal import Decimal, ROUND_DOWN
from Compare_Algorithm.PyQT5_Compare import Compare
import Map_.css_Map_Route as css
from dotenv import load_dotenv
import numpy as np
import os


class Show_Map_Cluster:
    def __init__(
        self,
        dataCenters,
        dataPoints,
        dataLayout,
        layout_Function,
        # btn_compare,
        cb_TSP,
        on,
        off,
        data_Matrix,
        cb_cluster,
        cb_Start,
    ):
        # cb_cluster.setCurrentIndex(0)
        # cb_Start.setCurrentIndex(0)
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
        self.web_view = QWebEngineView()
        self.show_All_Compare = ""
        self.on_Compare = False
        self.values_Title = []
        self.distance = []
        self.all_Points = []
        self.data_Point_Clean = []
        self.distance_Matrix = []
        self.click_count = 0
        # self.change_Compare(layout_Function, dataCenters)
        self.show_Map_HTML(
            dataCenters, dataPoints, dataLayout, cb_TSP, on, off, data_Matrix
        )

    # def change_Compare(self, layout_Function, dataCenters):
    #     if len(dataCenters) > 10:
    #         btn_compare.hide()
    #     else:
    #         # layout_Function.addWidget(btn_compare, 0, 7)
    #         btn_compare.hide()

    def show_Map_HTML(
        self, dataCenters, dataPoints, dataLayout, cb_TSP, on, off, data_Matrix
    ):
        self.show_valueAllPoint(dataPoints)
        data_Center = [list(point) for point in dataCenters]
        data_Kg = self.show_DataKgM(dataPoints, data_Matrix)
        data_Points_ = np.array(self.data_Point_Clean, dtype=object)
        data_Kg_M3_Drops = np.array(data_Kg, dtype=object)
        data_Radius = self.show_radius_Cluster(data_Points_, dataCenters)
        distances_html = self.calculator_Distance_Trip(data_Points_)
        nearest_Neighbor = Process_Data_Small().use_NearestNeighbor(
            distances_html, data_Points_
        )
        self.show_HTMLContent(
            data_Center,
            data_Radius,
            data_Kg_M3_Drops,
            nearest_Neighbor,
            dataCenters,
            dataLayout,
        )

        def show_Data_():
            self.web_view.hide()
            Compare(
                data_Points_,
                data_Center,
                cb_TSP,
                dataCenters,
                data_Kg_M3_Drops,
                dataLayout,
            )

        def show_Data_Cluster_Main():
            remove_layout()
            if dataLayout.count() == 1:
                self.web_view.show()

        def remove_layout():
            item = dataLayout.itemAt(1)
            if item:
                widget_to_delete = item.widget()
                if widget_to_delete:
                    dataLayout.removeWidget(widget_to_delete)
                    widget_to_delete.deleteLater()

        def on_Change_LayOut():
            self.click_count += 1
            if self.click_count % 2 == 1:
                show_Data_()
            else:
                show_Data_Cluster_Main()

        # btn_compare.clicked.connect(on_Change_LayOut)

    def show_DataKgM(self, dataPoints, data_Matrix):
        data_Kg = []
        array_Matrix = np.array(
            [
                [
                    item[2],
                    item[3],
                    float(item[5]),
                    float(item[6]),
                ]
                for item in data_Matrix
            ]
        )
        for items in dataPoints:
            data = []
            for value in items:
                lat = value[0]
                lon = value[1]
                for data_ in array_Matrix:
                    if lat == data_[2] and lon == data_[3]:
                        data.append(data_)
            data_Kg.append(data)
        self.data_Point_Clean = dataPoints
        return data_Kg

    def show_valueAllPoint(self, dataPoints):
        for data in dataPoints:
            for value in data:
                self.all_Points.append([value[0], value[1]])
        return self.all_Points

    def haversine_distance(self, coord1, coord2):
        R = 6371  # Bán kính của Trái Đất trong kilômét
        lat1, lon1 = np.radians(list(coord1))
        lat2, lon2 = np.radians(list(coord2))

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

        distance = R * c
        return distance

    def show_radius_Cluster(self, data_point, data_center):
        radius = []
        for i, group in enumerate(data_point):
            max_distance = 0
            for point in group:
                distance = self.haversine_distance(point, data_center[i])
                if distance > max_distance:
                    max_distance = distance
            radius.append(max_distance)
        radius = np.array(radius) * 1000
        return radius

    def calculator_Distance_Trip(self, data_point):
        try:
            for value in data_point:
                distance_matrix = distance_Matrix.calculate_distances(value)
                self.distance_Matrix.append(distance_matrix)
        except ValueError as e:
            print("Check Log Error Distance", e)
        return self.distance_Matrix

    # def use_BruteForce(self, distance_matrix, data_point, on, off):
    #     try:
    #         data = []
    #         for point, distance in zip(data_point, distance_matrix):
    #             route, distance_bf = Randomized_Tour_Cluster.randomized_tour(
    #                 distance, 0, on, off
    #             )
    #             print("check value data distance_bf", route)
    #             data.append(distance_bf)
    #         return data
    #     except ValueError as e:
    #         print("Check Log Error", e)

    def show_Tree_Trip(self, data_point, distances, data_Center):
        list_Option = ""
        for index, value in enumerate(data_point):
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
            KM:{distances[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return list_Option

    def calculator_Drops(self, drops):
        data_Clean = []
        seen_coordinates = set()

        for item in drops:
            volume, weight, latitude, longitude = item
            coordinates = (latitude, longitude)

            if coordinates not in seen_coordinates:
                data_Clean.append(item)
                seen_coordinates.add(coordinates)
        return data_Clean

    def show_HTMLContent(
        self,
        data_Center,
        data_Radius,
        data_Kg_M3_Drops,
        distances_html,
        dataCenters,
        dataLayout,
    ):
        html_content = f"""
        <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps</title>
                {css.type_cs()}
                <script src="https://maps.googleapis.com/maps/api/js?key={self.api_Key}&callback=initMap" async defer></script>
                <script>
                    function initMap() {{
                        var map = new google.maps.Map(document.getElementById('map'), {{
                            center: {{lat: {data_Center[0][0]}, lng: {data_Center[0][1]}}}, // Điểm trung tâm ban đầu
                            zoom: 12 // Độ phóng ban đầu
                        }});
                        
                        // Hiển thị điểm trung tâm dữ liệu và đường tròn
                        for (var i = 0; i < {len(data_Center)}; i++) {{
                            var center = new google.maps.LatLng({data_Center}[i][0], {data_Center}[i][1]);

                            var marker = new google.maps.Marker({{
                            position: center,
                            map: map,
                            title: 'Data Point'
                            }});

                            var circle = new google.maps.Circle({{
                            center: center,
                            radius: {list(data_Radius)}[i],
                            strokeColor: '#FF0000',
                            strokeOpacity: 0.8,
                            strokeWeight: 2,
                            fillColor: '#d59696',
                            fillOpacity: 0.35,
                            map: map
                            }});
                        }}
                        
                        // Hiển thị tất cả điểm dữ liệu
                        {self.all_Points}.forEach(function (point) {{
                            var marker = new google.maps.Marker({{
                                position: new google.maps.LatLng(point[0], point[1]),
                                map: map,
                                title: 'Data Point'
                            }});
                        }});
                    }}
                </script>
            </head>
                <body>
                <div class="main-menu">
                    <div class="container-main">
                        <div class="container"> 
                            <div class="tripline">
                                <div class="title">
                                    Nearest Neighbor
                                    <div class="event">
                                        <div class="event-date">Trip: {len(data_Center)}</div>
                                            <ul class="sub-events">
                                                <li class="sub-event">
                                                    {self.show_Tree_Trip(data_Kg_M3_Drops,distances_html,dataCenters)}
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                    </div>
                    <div id="map" style="height: 830px; width: 100%;">
                    </div>
                </div>
                </body>
            </html>
            """
        self.web_view.setHtml(html_content)
        dataLayout.addWidget(self.web_view)
