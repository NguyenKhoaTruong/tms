import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTextEdit
from Process_Data.PyQT5_Data_Real import show_Real_Data
import Map_.css_Map_Route as css
from dotenv import load_dotenv
import os


class Show_Map_TSP:
    def __init__(
        self, dataPoint, dataDistances, ui_map, dataTime, distance_Real, time_Real
    ):
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
        self.web_view = QWebEngineView()
        self.text_show = QTextEdit()
        self.show_Content(
            dataPoint, dataDistances, dataTime, distance_Real, time_Real, ui_map
        )

    def convent_Data(self, dataPoint):  # Convent data point
        data_ = []

        coordinates_str = dataPoint.split("->")
        for coord_str in coordinates_str:
            lat, lon = coord_str.split(",")
            lat, lon = float(lat), float(lon)
            data_.append([lat, lon])
        return data_

    def show_Location(self, data):  # Show Location Point:
        list_Point = "<ul>"
        for index, coords in enumerate(data):
            list_Point += (
                f"<li>Point {index+1} : Lat: {coords[0]} /  Lon: {coords[1]}</li>"
            )
        list_Point += "</ul>"

        return list_Point

    def show_Content(
        self, dataPoint, dataDistances, dataTime, distance_Real, time_Real, ui_map
    ):
        self.data_Convent = self.convent_Data(dataPoint)
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Google Maps Directions</title>
            <script src="https://maps.googleapis.com/maps/api/js?key={self.api_Key}&libraries=geometry&callback=initMap" async defer">
            </script>
            {css.type_Cs_Cluster()}
            <script>
                const data = {self.data_Convent};
                const start_Point={self.data_Convent[0][0]}
                const end_Point={self.data_Convent[0][1]}

                function initMap() {{
                    const map = new google.maps.Map(document.getElementById('map'), {{
                        zoom: 5
                    }});

                    const directionsService = new google.maps.DirectionsService();
                    const directionsRenderer = new google.maps.DirectionsRenderer({{
                        map: map,
                        suppressMarkers: true
                    }});
                    
                    // Convert dữ liệu từ biến data thành danh sách waypoints
                    const waypoints = data.map(point => ({{
                        location: new google.maps.LatLng(point[0], point[1])
                    }}));

                    const request = {{
                        origin: waypoints[0].location,
                        destination: waypoints[waypoints.length - 1].location,
                        waypoints: waypoints.slice(1, waypoints.length - 1),
                        travelMode: google.maps.TravelMode.DRIVING
                    }};
                    for (let i = 0; i < {len(self.data_Convent)}; i++) {{
                        new google.maps.Marker({{
                            position: {{ lat: {self.data_Convent}[i][0], lng: {self.data_Convent}[i][1]}},
                            map: map,
                            label: (i + 1).toString(),
                            zIndex: 20
                        }});
                    }}
                    
                    directionsService.route(request, function(result, status) {{
                        if (status == 'OK') {{
                            directionsRenderer.setDirections(result);
                        }}
                    }});
                }}
            </script>
        </head>
        <body onload="initMap()">
            <div id="text-show" class="container">
                <div class="title-text">
                Route:</br>
                {self.show_Location(self.data_Convent)}
                </div></br>
                <div class="title-text">
                KM - Direction: {round(dataDistances,3)} Km </br> 
                Time - Direction: {dataTime} Minutes
                </div></br>
                <div class="title-text">
                KM - Route: {distance_Real}</br>
                Time - Route: {time_Real}
                </div></br>       
            </div>
            <div id="map" style="height: 1000px; width: 100%;"></div>
        </body>
        </html>
        """

        if ui_map.count() >= 1:
            item = ui_map.itemAt(0)
            ui_map.removeItem(item)
        self.web_view.setHtml(html)
        ui_map.addWidget(self.web_view)
