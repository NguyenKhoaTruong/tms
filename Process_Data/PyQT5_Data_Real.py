from datetime import datetime
from dotenv import load_dotenv
import requests
import googlemaps
import os


class show_Real_Data:
    def __init__(self):
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
        self.gmaps = googlemaps.Client(key=self.api_Key)

    def convent_route(self, data_route):
        coordinates = data_route.split("->")

        waypoints = []

        for coord in coordinates:
            lat_str, lon_str = coord.split(",")

            latitude = float(lat_str.strip())
            longitude = float(lon_str.strip())

            waypoints.append((latitude, longitude))

        return self.data_Real(waypoints)

    def data_Real(self, way_point):
        directions_result = self.gmaps.directions(
            origin=way_point[0],
            destination=way_point[-1],
            waypoints=way_point[1:-1],
            mode="driving",
            departure_time=datetime.now(),
        )
        total_distance = 0
        total_time = 0

        for leg in directions_result[0]["legs"]:
            total_distance += leg["distance"]["value"]
            total_time += leg["duration"]["value"]
        total_distance_text = f"{total_distance / 1000:.2f} km"
        total_time_text = f"{total_time // 3600} giờ {total_time % 3600 // 60} phút"
        return total_distance_text, total_time_text

    def time_Order_Route(self, way_point):
        data_Time = []
        origin = (way_point[0][0], way_point[0][1])
        destination = (way_point[-1][0], way_point[-1][1])
        for i in range(1, len(way_point)):
            waypoint = (way_point[i][0], way_point[i][1])
            directions_result = self.gmaps.directions(
                origin,
                destination,
                waypoints=[waypoint],
                mode="driving",
                departure_time=datetime.now(),
            )
            if directions_result:
                start_location = directions_result[0]["legs"][0]["start_location"]
                end_location = directions_result[0]["legs"][0]["end_location"]
                duration = directions_result[0]["legs"][0]["duration"]["text"]
                origin = (end_location["lat"], end_location["lng"])
                data_Time.append(duration)
            else:
                print(f"Không tìm thấy thông tin từ điểm {i} đến điểm {i+1}.")
        data_Time = self.covenrt_Time_Order(data_Time)
        return data_Time

    def covenrt_Time_Order(self, data):
        time = []
        for item in data:
            time_str = "".join(filter(str.isdigit, item))
            minutes = int(time_str)
            time.append(minutes)
        return time

    def get_distance(self, origin, destination):
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={self.api_Key}&mode=driving"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "OK":
            distance = data["rows"][0]["elements"][0]["distance"]["value"]
            return distance / 1000
        return None

    def get_NameLocation(self, point):
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "latlng": f"{point[0]},{point[1]}",
            "key": self.api_Key,
        }

        response = requests.get(base_url, params=params)
        data = response.json()
        if data["status"] == "OK":
            result = data["results"][0]
            address_components = result["address_components"]
            street_number = None
            route = None
            locality = None
            administrative_area_level_2 = None
            administrative_area_level_1 = None
            country = None

            for component in address_components:
                types = component["types"]
                if "street_number" in types:
                    street_number = component["long_name"]
                elif "route" in types:
                    route = component["long_name"]
                elif "locality" in types:
                    locality = component["long_name"]
                elif "administrative_area_level_2" in types:
                    administrative_area_level_2 = component["long_name"]
                elif "administrative_area_level_1" in types:
                    administrative_area_level_1 = component["long_name"]
                elif "country" in types:
                    country = component["long_name"]
            return {
                "street_number": street_number,
                "route": route,
                "locality": locality,
                "administrative_area_level_2": administrative_area_level_2,
                "administrative_area_level_1": administrative_area_level_1,
                "country": country,
            }
        else:
            return None

    def show_WayPoint(self, point):
        total_distance = 0
        total_duration = 0
        for i in range(len(point) - 1):
            start_point = f"{point[i]['lat']},{point[i]['lng']}"
            end_point = f"{point[i + 1]['lat']},{point[i + 1]['lng']}"
            url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_point}&destination={end_point}&mode=driving&key={self.api_Key}"
            response = requests.get(url)
            data = response.json()
            if data["status"] == "OK":
                route = data["routes"][0]
                distance = route["legs"][0]["distance"]["value"]
                duration = route["legs"][0]["duration"]["value"]
                total_distance += distance
                total_duration += duration
        cost = total_distance / 1000
        time = total_duration / 3600
        return cost, time
