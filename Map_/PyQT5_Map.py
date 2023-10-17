import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Algorithm.No_Cluster.PyQT5_Brute_Force import Brute_Force
from Process_Data.PyQT5_distanceMatrix import distance_Matrix
from Process_Data.PyQT5_Route_Time import Route_Time_Min
from Process_Data.PyQT5_Data_Real import show_Real_Data
import Map_.css_Map_Route as css
from dotenv import load_dotenv
import os


class ShowMapCluster:
    def __init__(self, dataPoints, dataLayout):
        print("đã show map")
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
        self.web_view = QWebEngineView()
        self.show_Map(dataPoints, dataLayout)

    def calculator_Distance(self, points):
        distances = distance_Matrix.calculate_distances(points)
        return distances

    def distance_Brute_Brute(self, dataPoints, distances):
        distance_Brute, route = Brute_Force.brute_force_tsp(
            dataPoints, distances, dataPoints[0], False, True
        )
        return distance_Brute, route

    def time_Route(self, distance):
        time_Direction = Route_Time_Min.calculate_total_time(distance, 20)
        return time_Direction

    def convent_Route(self, route, dataPoints):
        route_Convent = [dataPoints[i] for i in route]
        return route_Convent

    def show_Real(self, route):
        route_ = "->".join([f"{coord[0]} , {coord[1]}" for coord in route])
        distance, time = show_Real_Data().convent_route(route_)
        return distance, time

    def show_List_Point(self, route):
        list_Point = "<ul>"
        for index, coords in enumerate(route):
            list_Point += (
                f"<li>Point {index+1} : Lat: {coords[0]} /  Lon: {coords[1]}</li>"
            )
        list_Point += "</ul>"
        return list_Point

    def show_Map(self, dataPoints, dataLayout):
        distance = self.calculator_Distance(dataPoints)

        distance_, route_ = self.distance_Brute_Brute(dataPoints, distance)

        time_ = self.time_Route(distance_)

        route__ = self.convent_Route(route_, dataPoints)

        distance_Real, time_Real = self.show_Real(route__)

        html_content = f"""
       <!DOCTYPE html>
        <html>
        <head>
            <title>Google Maps Example</title>
            <script src="https://maps.googleapis.com/maps/api/js?key={self.api_Key}&callback=initMap" async defer>
            </script>
            {css.type_Cs_Cluster()}
            <script>
                function initMap() {{
                    var map = new google.maps.Map(document.getElementById('map'), {{
                        center: {{lat: {dataPoints[0][0]}, lng:{dataPoints[0][1]}}},
                        zoom:5 
                    }});
       
                    {dataPoints}.forEach(function (point) {{
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
                <div id="text-show" class="container">
                <div class="title-text">
                Route:</br>
                {self.show_List_Point(route__)}
                </div></br>
                <div class="title-text">
                KM - Direction:{round(distance_,3)} KM</br> 
                Time - Direction:{time_} Minutes
                </div></br>
                <div class="title-text">
                KM - Route: {distance_Real}</br>
                Time - Route: {time_Real}
                </div></br>       
            </div>
            <div id="map" style="height: 2000px; width: 100%;"></div>
        </body>
        </html>
        """
        self.web_view.setHtml(html_content)
        dataLayout.addWidget(self.web_view)
