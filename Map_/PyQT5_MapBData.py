import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Process_Data.PyQT5_Data_Real import show_Real_Data
import Map_.css_Map_Route as css


class Map_BData:
    def __init__(self):
        self.data = []
        print("Show Map BDataa")

    def show_HTML(
        self,
        data_Point,
        dataDistances,
        maker_ShipTo,
        key,
    ):
        try:
            for items in data_Point:
                self.data.append({"lat": items[0], "lng": items[1]})
            distance, time = show_Real_Data().show_WayPoint(self.data)
            distance = round(distance, 3)
            time = round(time, 3)
        except ValueError as e:
            print("Log Error", e)
        html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps Directions</title>
                <script src="https://maps.googleapis.com/maps/api/js?key={key}&libraries=geometry&callback=initMap" async defer">
                </script>
                {css.css_Map_Cluster()}
                <script>
                    const start_Point={data_Point[0][0]}
                    const end_Point={data_Point[0][1]}
                    function initMap() {{
                        const service = new google.maps.DirectionsService;
                        const station={self.data}
                        const map = new google.maps.Map(document.getElementById('map'), {{
                            center: {{lat: 10.8, lng: 106.6}},
                            zoom: 7
                        }});
                        map.setCenter(new google.maps.LatLng(start_Point,end_Point));
                        map.setZoom(5);
                        {data_Point}.forEach(function (point,index) {{
                            var marker = new google.maps.Marker({{
                                position: new google.maps.LatLng(point[0], point[1]),
                                map: map,
                                label: (index + 1).toString()
                            }});
                        }});
                        for (var i = 0, parts = [], max = 25 - 1; i < station.length; i = i + max)
                            parts.push(station.slice(i, i + max + 1));

                        var service_callback = function (response, status) {{
                            if (status != 'OK') {{
                                console.log('Directions request failed due to ' + status);
                                return;
                            }}
                            var renderer = new google.maps.DirectionsRenderer;
                            renderer.setMap(map);
                            renderer.setOptions({{ suppressMarkers: true, preserveViewport: true }});
                            renderer.setDirections(response);
                        }};
                        for (var i = 0; i < parts.length; i++) {{
                            var waypoints = [];
                            for (var j = 1; j < parts[i].length - 1; j++)
                                waypoints.push({{ location: parts[i][j], stopover: false }});
                            var service_options = {{
                                origin: parts[i][0],
                                destination: parts[i][parts[i].length - 1],
                                waypoints: waypoints,
                                travelMode: 'WALKING'
                            }};
                            service.route(service_options, service_callback);
                        }}
                    }}
                </script>
            </head>
            <body onload="initMap()">
                <div class="main-menu">
                    <div class="container-main">
                        <div id="text-show" class="container">
                            <div class="title-text">
                                <table>
                                    <tr>
                                        <th>SEQ</th>
                                        <th>SHIP TO CODE</th>
                                        <th>ETA</th>
                                        <th>ETD</th>
                                    </tr>
                                    {maker_ShipTo}
                                </table>
                            </div> 
                        </div>
                    </div>
                    <div class="route-main">
                        <div id="text-show" class="route">
                            <div class="title-text">
                                KM - Direction:{str(dataDistances)[:5]} KM</br>
                            </div>
                            <div class="title-text">
                                KM - Route:{distance} KM</br>
                            </div>  
                            <div class="title-text">
                                Time - Route:{time} Hour</br>
                            </div> 
                        </div>
                    </div>
                    <div id="map" style="height: 830px; width: 100%;"></div>
                </div>
            </body>
            </html>
            """
        print('check vlaue data htmkl',html)
        return html
