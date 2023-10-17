from math import sqrt
from geopy.distance import great_circle
class Route_Time_Min():
    def __init__(self):
        print('Route Time')
    def calculate_total_time(min_cost, speed_km_per_hour):
        
        total_distance = min_cost    
            
        total_time = total_distance / speed_km_per_hour # Calculate the total time based on the speed
        
        hours = int(total_time)  
        minutes = (total_time - hours) * 60 

        total_time=f"{hours} hour {int(minutes)}"

        return total_time

    def display_total_time(total_time):     # không cần hàm này nữa:
        print("Tổng thời gian di chuyển trong chu trình (phút):", total_time)
        return total_time
        