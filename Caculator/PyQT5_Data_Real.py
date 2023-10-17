from dotenv import load_dotenv
from datetime import datetime
import googlemaps
import os

class show_Real_Data:
    def __init__(self):
        load_dotenv()
        self.api_Key=os.getenv("API_KEY")
        self.gmaps = googlemaps.Client(key=self.api_Key)
    def convent_route(self,data_route):

        coordinates = data_route.split("->")

        waypoints = []

        for coord in coordinates:
            
            lat_str, lon_str = coord.split(",")
            
            latitude = float(lat_str.strip())
            longitude = float(lon_str.strip())
            
            waypoints.append((latitude, longitude))

        return self.data_Real(waypoints)
    
    def data_Real(self,way_point):
        directions_result = self.gmaps.directions(
            origin=way_point[0],
            destination=way_point[-1],
            waypoints=way_point[1:-1],
            mode="driving",
            departure_time=datetime.now()
        )
        total_distance = 0
        total_time = 0
        
        for leg in directions_result[0]['legs']:
            total_distance += leg['distance']['value']  # Tổng khoảng cách (đơn vị mét)
            total_time += leg['duration']['value']      # Tổng thời gian di chuyển (đơn vị giây)
        
        total_distance_text = f"{total_distance / 1000:.2f} km"  # Đổi đơn vị thành km
        total_time_text = f"{total_time // 3600} giờ {total_time % 3600 // 60} phút"  # Đổi đơn vị thành giờ và phút
        
        return total_distance_text, total_time_text


        