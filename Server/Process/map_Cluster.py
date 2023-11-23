from dotenv import load_dotenv
import os
class MapCluster:
    def __init__(self):
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
    def setValueAllPoint(self,data):
        _data=[]
        for items in data:
            for item in items:
                _data.append(item)
        return _data
    def showMap(self,*args):
        _point=args[0]
        _center=args[1]
        _radius=args[2]
        _all_Point=self.setValueAllPoint(_point)
        _html = f"""
        <!DOCTYPE html>
            <html>
            <head>
                <title>Map Cluster</title>
                <script src="https://maps.googleapis.com/maps/api/js?key={self.api_Key}&callback=initMap" async defer></script>
                <script>
                    function initMap() {{
                        var map = new google.maps.Map(document.getElementById('map'), {{
                            center: {{lat: {_center[0][0]}, lng: {_center[0][1]}}},
                            zoom: 12
                        }});
                        
                        for (var i = 0; i < {len(_center)}; i++) {{
                            var center = new google.maps.LatLng({_center}[i][0], {_center}[i][1]);

                            var marker = new google.maps.Marker({{
                            position: center,
                            map: map,
                            title: 'Data Point'
                            }});

                            var circle = new google.maps.Circle({{
                            center: center,
                            radius: {list(_radius)}[i],
                            strokeColor: '#FF0000',
                            strokeOpacity: 0.8,
                            strokeWeight: 2,
                            fillColor: '#d59696',
                            fillOpacity: 0.35,
                            map: map
                            }});
                        }}
                        
                        {_all_Point}.forEach(function (point) {{
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
        return _html