import numpy as np
import random


class Tabu:
    def __init__(self):
        print("Tabu Search")

    def calculate_distance(self, route, distance, point):
        return sum([distance[route[i - 1]][route[i]] for i in range(point)])

    def convent_route(self, route, point):
        route_Convert = [point[i] for i in route]
        return route_Convert

    def cal_Matrix(self, point, num_Points):
        distance_Matrix = np.zeros((num_Points, num_Points))
        for i in range(num_Points):
            for j in range(num_Points):
                lat1, lon1 = point[i]
                lat2, lon2 = point[j]
                radius = 6371
                dlat = np.radians(lat2 - lat1)
                dlon = np.radians(lon2 - lon1)
                a = (
                    np.sin(dlat / 2) ** 2
                    + np.cos(np.radians(lat1))
                    * np.cos(np.radians(lat2))
                    * np.sin(dlon / 2) ** 2
                )
                c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
                distance = radius * c
                distance_Matrix[i][j] = distance
        return distance_Matrix

    def use_Tabu(self, point, start_Point, on_Return, mode_Start):
        if mode_Start == True:
            point.insert(0, start_Point)
        num_points = len(point)
        num_iterations = 1000
        tabu_list_size = 10
        dist_matrix = self.cal_Matrix(point, num_points)
        initial_solution = list(range(num_points))
        initial_solution.remove(0)
        initial_solution.insert(0, 0)
        best_solution = initial_solution.copy()
        best_distance = self.calculate_distance(best_solution, dist_matrix, num_points)
        distance, route = self.process_tabu(
            num_iterations,
            tabu_list_size,
            best_solution,
            best_distance,
            num_points,
            dist_matrix,
            on_Return,
            point,
        )
        return distance, route

    def process_tabu(
        self,
        num_iterations,
        tabu_list_size,
        best_solution,
        best_distance,
        num_points,
        dist_matrix,
        on_Return,
        point,
    ):
        try:
            tabu_list = []
            for _ in range(num_iterations):
                neighbors = []
                for i in range(1, num_points):
                    for j in range(i + 1, num_points):
                        neighbor = best_solution.copy()
                        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                        neighbors.append(neighbor)

                min_distance = float("inf")
                for neighbor in neighbors:
                    distance = self.calculate_distance(
                        neighbor, dist_matrix, num_points
                    )
                    if distance < min_distance and neighbor not in tabu_list:
                        min_distance = distance
                        best_neighbor = neighbor

                if min_distance < best_distance:
                    best_solution = best_neighbor
                    best_distance = min_distance
                    tabu_list.append(best_neighbor)
                    if len(tabu_list) > tabu_list_size:
                        tabu_list.pop(0)
            if on_Return == True:
                best_solution.append(best_solution[0])
                distance_to_start = dist_matrix[best_solution[-2]][best_solution[-1]]
                best_distance += distance_to_start
            route = self.convent_route(best_solution, point)
            cost = round(best_distance, 3)
            return cost, route
        except ValueError as e:
            print("Log Error", e)


# start_Point = [10.810362958119587, 106.6649108539821]
# point = [
#     [10.771135858264335, 106.69507196790613],
#     [11.03297581, 106.3542277],
#     [10.89934761, 106.413231],
#     [11.02517305, 106.3870693],
#     [10.95523884, 106.6061324],
#     [10.89015757, 106.6345503],
#     [10.8965339, 106.6406705],
#     [10.92449731, 106.5581646],
#     [11.00698019, 106.3945347],
#     [10.75799883, 106.6517412],
#     [10.6478613, 106.5443319],
#     [10.828227407730115, 106.7733690828174],
#     [10.827237159791236, 106.679470496312],
#     [10.811710745264808, 106.63303318975827],
#     [10.817867359243692, 106.61473196280781],
#     [10.952184023450435, 106.89048764418078],
#     [11.08452259156998, 107.17174401903856],
#     [10.972936342924847, 106.90877480185128],
#     [10.412331038586013, 107.19334947422125],
#     [10.7411685976066, 106.9311067916584],
#     [10.911455351812652, 106.8608174650592],
#     [10.910847184835376, 106.69956076807442],
#     [10.907563319424014, 106.71699805894866],
#     [10.911086195059935, 106.70034263189507],
#     [10.971847491113245, 106.7337902322077],
#     [10.896296714153396, 106.72605694602625],
#     [11.130025001767287, 106.60041292421302],
#     [10.919692700754005, 106.73034889412152],
#     [10.99520075891292, 106.70779289631317],
#     [10.946243697773696, 106.74889584074957],
#     [10.743486664230028, 106.660556613498],
#     [10.755351564939886, 106.72962652564206],
#     [10.751027390235278, 106.61127699631155],
#     [10.828195794307579, 106.7733690828174],
#     [10.62991908399019, 106.71692132514566],
#     [10.751035676989272, 106.61127196263875],
#     [10.755872771815007, 106.74292579631158],
#     [10.875662663730843, 106.73057725822333],
#     [10.860849185863177, 106.68894959631228],
#     [10.83968566264628, 106.64933706747692],
#     [10.835404478048432, 106.63442136747699],
#     [10.79873892744089, 106.58475073864138],
# ]
# Tabu().use_Tabu(point, start_Point, False, True)
