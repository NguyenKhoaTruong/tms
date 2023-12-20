import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Map_.PyQT5_MapBData import Map_BData
from Process_Data.PyQT5_Data_Real import show_Real_Data
from datetime import time, datetime, timedelta
import Map_.css_Map_Route as css
from dotenv import load_dotenv
import numpy as np
import os


class Show_Map_TSP_Cluster:
    def __init__(
        self,
        dataPoint,
        dataDistances,
        ui_map,
        pointCenter,
        dataTime,
        data_array,
        data_Ship,
        mode_Start,
        on,
    ):
        load_dotenv()
        self.web_view = QWebEngineView()
        self.api_Key = os.getenv("API_KEY")
        self.time = ""
        data_Point = self.convent_Data(dataPoint)
        data_Matrix = self.convent_Data_Matrix(data_array)
        # maker_Point = self.marker_Points(data_Point)
        print('check value data point',data_Point,len(data_Point),type(data_Point))
        eta_ETD = self.calculator_ETA_ETD(data_Point, data_Ship)
        maker_ShipTo = self.marker_ShipTo(
            data_Point, data_Matrix, eta_ETD, mode_Start, on
        )

        self.show_Content(
            data_Point,
            # maker_Point,
            dataDistances,
            dataTime,
            ui_map,
            maker_ShipTo,
        )

    # def
    def convent_DataShipTo(self, point, order):
        data = []
        for item in point:
            lat = item[0]
            lon = item[1]
            for value in order:
                if lat == value[5] and lon == value[6]:
                    add_one = value[7]
                    add_two = value[8]
                    add_three = value[9]
                    data.append([add_one, add_two, add_three])
        return data

    def convent_Data_Matrix(self, data):
        for item in data:
            item[5] = float(item[5])
            item[6] = float(item[6])
        return data

    def convent_Data(self, data_Point):
        data = []
        coordinates_str = data_Point.split("->")
        for coord_str in coordinates_str:
            lat, lon = coord_str.split(",")
            lat, lon = float(lat), float(lon)
            data.append([lat, lon])
        return data

    # def marker_ShipTo(self, data_Ship_To, eta_ETD):
    #     list = "<ul>"
    #     for index, coords in enumerate(data_Ship_To):
    #         eta = eta_ETD[index][0].strftime("%H:%M")
    #         etd = eta_ETD[index][1].strftime("%H:%M")
    #         list += f'<li class="ship-to">{index+1} : {coords[0]} : {eta} | {etd} </li>'
    #     list += "</ul>"
    #     return list
    def marker_ShipTo(self, point, matrix, eta_ETD, mode_Start, on):
        if mode_Start == True:
            address_Point = show_Real_Data().get_NameLocation(point[0])
            if address_Point:
                street_number = address_Point["street_number"]
                district = address_Point["administrative_area_level_2"]
                conscious = address_Point["administrative_area_level_1"]
                # làm gọn biến này
                data_Address = [
                    "",
                    "",
                    "",
                    "",
                    "",
                    point[0][0],
                    point[0][1],
                    f"{street_number}",
                    f"{district}",
                    f"{conscious}",
                ]
            else:
                print("Không tìm thấy địa chỉ")
            new_Data = matrix.tolist()
            # new_Data.insert(0, data_Address)
            # if on == True:
            new_Data.append(data_Address)
            data_ShipTo = self.convent_DataShipTo(point, new_Data)
        else:
            data = []
            for items in point:
                if items not in data:
                    data.append(items)
            data_ShipTo = self.convent_DataShipTo(data, matrix)
        list = ""
        for index, coords in enumerate(data_ShipTo):
            if coords[0] == "None":
                coords[0] = f"{coords[1]}, {coords[2]}"
            eta = eta_ETD[index][0].strftime("%H:%M")
            etd = eta_ETD[index][1].strftime("%H:%M")
            list += f"<tr><td>{index+1}</td><td>{coords[0]}</td><td>{eta}</td><td>{etd}</td></tr>"
        return list

    def marker_Points(self, data_Point):
        list_Point = "<ul>"
        for index, coords in enumerate(data_Point):
            list_Point += (
                f"<li>Point {index+1} : Lat: {coords[0]} /  Lon: {coords[1]}</li>"
            )
        list_Point += "</ul>"
        return list_Point

    def show_Data_Real(self, route):
        route_ = "->".join([f"{coord[0]} , {coord[1]}" for coord in route])
        distance, time = show_Real_Data().convent_route(route_)
        return distance, time

    def calculator_ETA_ETD(self, point, time_Ship):
        print('check valeuy data time ship 0',time_Ship[0],type(time_Ship[0]))
        time = datetime.combine(datetime.today(), time_Ship[0])
        print('check type value start time',time,type(time))
        before_Time = time_Ship[1]
        service_Time = time_Ship[2]
        after_Time = time_Ship[3]
        if time_Ship[4] == "0" or time_Ship[4] == "1":
            congestion_Time = int(time_Ship[4])
        else:
            congestion_Time = float(time_Ship[4])
        eta_ETD = []
        for i in range(len(point)):
            origin = f"{point[i][0]},{point[i][1]}"
            destination = (
                f"{point[i + 1][0]},{point[i + 1][1]}" if i + 1 < len(point) else origin
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
                eta_ETD.append((time, estimated_time))
                time = estimated_time
        start_Time = datetime.combine(datetime.today(), time_Ship[0])
        self.time = self.time_Route(start_Time, time)
        return eta_ETD

    def time_Route(self, start_Time, end_Time):
        time = end_Time - start_Time
        hours, remainder = divmod(time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        str_Time = f"""{hours} giờ {minutes} phút"""
        return str_Time

    def convent_Hour(self, hours):
        hour = hours.hour
        minute = hours.minute
        result = hour + minute
        return result

    def convent_time(self, minute):
        minutes = timedelta(minutes=minute)
        return minutes

    def show_UI(self, ui_map, data):
        if ui_map.count() >= 1:
            item = ui_map.itemAt(0)
            ui_map.removeItem(item)
        self.web_view.setHtml(data)
        ui_map.addWidget(self.web_view)

    def show_Content(
        self,
        data_Point,
        # maker_Point,
        dataDistances,
        dataTime,
        ui_map,
        maker_ShipTo,
    ):
        if len(data_Point) > 20:
            map_Big = Map_BData().show_HTML(
                data_Point,
                dataDistances,
                maker_ShipTo,
                self.api_Key,
            )
            self.show_UI(ui_map, map_Big)
        else:
            distance_Real, time_Real = self.show_Data_Real(data_Point)
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps Directions</title>
                <script src="https://maps.googleapis.com/maps/api/js?key={self.api_Key}&libraries=geometry&callback=initMap" async defer">
                </script>
                {css.css_Map_Cluster()}
                <script>
                    const data = {data_Point};
                    const start_Point={data_Point[0][0]}
                    const end_Point={data_Point[0][1]}

                    function initMap() {{
                        const map = new google.maps.Map(document.getElementById('map'), {{
                            zoom: 7
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
                        // hiển thị các điểm dữ liệu trên bản đồ.
                        data.forEach(function (point,index) {{
                            var marker = new google.maps.Marker({{
                                position: new google.maps.LatLng(point[0], point[1]),
                                map: map,
                                label: (index + 1).toString()
                            }});
                        }});
                        const request = {{
                            origin: waypoints[0].location,
                            destination: waypoints[waypoints.length - 1].location,
                            waypoints: waypoints.slice(1, waypoints.length - 1),
                            travelMode: google.maps.TravelMode.DRIVING
                        }};
                        directionsService.route(request, function(result, status) {{
                            if (status == 'OK') {{
                                directionsRenderer.setDirections(result);
                            }}
                        }});

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
                                KM - Route:{distance_Real[:-2]} KM</br>
                            </div>  
                            <div class="title-text">
                                Time - Route:{self.time}</br>
                            </div>  
                        </div>
                    </div>
                    <div id="map" style="height: 830px; width: 100%;"></div>
                </div>
            </body>
            </html>
            """
            print('check vlaue data html',html)
            self.show_UI(ui_map, html)

        # <body onload="initMap()">
        #     <div class="main-menu">
        #         <div class="container-main">
        #             <div id="text-show" class="container">
        #                 <div class="title-text">
        #                 Ship To | ETA | ETD:</br>
        #                     {maker_Ship_To}
        #                 </div>
        #                 <div class="title-text">
        #                     KM - Direction:{dataDistances} KM</br>
        #                 </div>
        #                 <div class="title-text">
        #                     KM - Route:{distance_Real} KM</br>
        #                  </div>
        #             </div>
        #         </div>
        #         <div id="map" style="height: 1000px; width: 100%;"></div>
        #     </div>
        # </body>
