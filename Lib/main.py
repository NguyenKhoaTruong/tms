import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Lib.process_Data import process_Data
from Lib.divide_Data import use_Kmean
from Lib.caculator_Distacne import distance_Matrix
from Algorithm.Cluster.Brute_Force import Brute_Force_Cluster


class main_Process:
    def __init__(self):
        self.distance_Matrix = []
        self.data_Order = []
        self.route = []
        self.cost = []

    def fun_Process_Input(self):
        # Lọc và lấy dữ liệu
        data_Order = process_Data().drop_Dulicate_Data()
        return data_Order

    def fun_GetPointTrip(self):
        # Point
        data_Point = use_Kmean().data_Kmean(self.fun_Process_Input())
        num_Trip = len(data_Point)
        return data_Point, num_Trip

    def fun_GetParameter(self, start_point):
        point, num_trip = self.fun_GetPointTrip()

        def format_path_to_string(path, points):
            path_String = []
            for i in range(len(path)):
                lat, lon = points[path[i]]
                path_String.append([lat, lon])
            return path_String

        for value in point:
            value.append(start_point)
            distance = distance_Matrix.calculate_distances(value)
            cost, route = Brute_Force_Cluster.brute_force_tsp(
                value, distance, start_point, True, False
            )
            route_ = format_path_to_string(route, value)
            route_Order = self.route_To_Order(route_, self.fun_Process_Input())
            self.data_Order.append(route_Order)
        # Hiển thị kết quả:
        self.show_Order(num_trip, self.data_Order)

    def show_Order(self, trip, order):
        for i in range(trip):
            print(f"Trip {i+1} :")
            print(f"Order: {order[i]}")

    def route_To_Order(self, route, data_Order):  # coi lại hàm này.
        data_Route = [point[:2] for point in route]
        data_Order_ = [[float(order[0][5]), float(order[0][6])] for order in data_Order]
        data = []
        for lat_lon in data_Order_:
            if lat_lon in data_Route:
                index = data_Route.index(lat_lon)
                data.append(data_Order[index][0][1])
        return data


start_point = (10.740346775668945, 106.66111865328268)
main_Process().fun_GetParameter(start_point)
