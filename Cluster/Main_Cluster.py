import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Cluster.MiniBatchKMeans import Mini_Bath_KMean
from Cluster.MeanShift import Mean_Shift_
from Cluster.GausianMixture import Gausian
from Cluster.Kmean_Fixed import Kmean_
from dotenv import load_dotenv
import numpy as np
import os


class Main_Clustering:
    def __init__(self):
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
        print("Main Clusting")

    def convent_All_Locations(self, point_Location):
        location = []
        for items in point_Location:
            for value in items:
                location.append(list(value))
        return location

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

    def haversine_distance(self, coord1, coord2):
        R = 6371
        lat1, lon1 = np.radians(list(coord1))
        lat2, lon2 = np.radians(list(coord2))

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

        distance = R * c
        return distance

    def get_DataShowMap(self, selected_Text, data, num_Cluster):
        try:
            if selected_Text == "Gausian Mixture":
                data_Center, data_Point = Gausian().get_DataShowMap(data, num_Cluster)
            elif selected_Text == "Mean Shift":
                data_Center, data_Point = Mean_Shift_().get_DataShowMap(data)
            elif selected_Text == "Mini Batch K Mean":
                data_Center, data_Point = Mini_Bath_KMean().get_DataMap(
                    data, num_Cluster
                )
            elif selected_Text == "K_Means":
                data_Center, data_Point = Kmean_().get_DataShowMap(data, num_Cluster)
            else:
                print("Xử lý ngoại lệ")
            data_Radius = self.show_radius_Cluster(data_Point, data_Center)
            data_All_Location = self.convent_All_Locations(data_Point)
            return data_Center, data_All_Location, data_Radius
        except ValueError as e:
            raise ("Log Error", e)

    def show_DataHTML(self, selected_Text, data, num_Cluster):
        data_Center, data_Point, data_Radius = self.get_DataShowMap(
            selected_Text, data, num_Cluster
        )
        html_content = f"""
        <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps</title>
                <script src="https://maps.googleapis.com/maps/api/js?key={self.api_Key}&callback=initMap" async defer></script>
                <script>
                    function initMap() {{
                        var map = new google.maps.Map(document.getElementById('map'), {{
                            center: {{lat: {data_Center[0][0]}, lng: {data_Center[0][1]}}}, // Điểm trung tâm ban đầu
                            zoom: 12 // Độ phóng ban đầu
                        }});
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
                        {data_Point}.forEach(function (point) {{
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
                    <div id="map" style="height: 830px; width: 100%;">
                    </div>
                </body>
            </html>
            """
        return html_content
