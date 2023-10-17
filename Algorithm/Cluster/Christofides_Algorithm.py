import networkx as nx
import math


class Christofides:
    def __init__(self):
        print("Christofides Algorithm")

    def convent_Route(self, route, point):
        route_Convert = [point[i] for i in route]
        return route_Convert

    def use_Christofides(self, point, start_Point, on_Return, mode_Start):
        try:
            if mode_Start == True:
                point.insert(0, start_Point)
            n = len(point)
            G = nx.complete_graph(n)

            def haversine(lat1, lon1, lat2, lon2):
                R = 6371
                dlat = math.radians(lat2 - lat1)
                dlon = math.radians(lon2 - lon1)
                a = (
                    math.sin(dlat / 2) ** 2
                    + math.cos(math.radians(lat1))
                    * math.cos(math.radians(lat2))
                    * math.sin(dlon / 2) ** 2
                )
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                return R * c

            dist_matrix = [
                [haversine(lat1, lon1, lat2, lon2) for lat2, lon2 in point]
                for lat1, lon1 in point
            ]
            tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True)
            if on_Return == True:
                total_distance = sum(
                    dist_matrix[i][j] for i, j in zip(tsp_tour, tsp_tour[1:])
                )
            else:
                tsp_tour = tsp_tour[:-1]
                total_distance = sum(
                    dist_matrix[i][j] for i, j in zip(tsp_tour, tsp_tour[1:])
                )
            route = self.convent_Route(tsp_tour, point)
            cost = round(total_distance, 3)
            return route, cost
        except ValueError as e:
            print("Log Error", e)


# points = [
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
# start_Points = [10.807025404400537, 106.66423534659137]
# Christofides().use_Christofides(points, start_Points, True)
