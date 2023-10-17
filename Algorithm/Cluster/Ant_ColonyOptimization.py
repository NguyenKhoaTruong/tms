import networkx as nx
import random
from geopy.distance import great_circle


class Ant:
    def __init__(self):
        print("Ant Colony Optimization")

    def convent_Route(self, route, point):
        route_Convert = [point[i] for i in route]
        return route_Convert

    def calculate_cost(self, graph, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]["distance"]
        return cost

    def calculate_distance(self, coord1, coord2):
        return great_circle(coord1, coord2).kilometers

    def ant_colony_optimization(
        self,
        on_Return,
        graph,
        num_ants,
        num_iterations,
        alpha,
        beta,
        evaporation_rate,
        start_node,
    ):
        num_nodes = len(graph.nodes())
        best_path = None
        best_cost = float("inf")
        try:
            for _ in range(num_iterations):
                ants = [[] for _ in range(num_ants)]

                for ant in ants:
                    ant.append(start_node)

                for _ in range(num_nodes - 1):
                    for ant in ants:
                        current_node = ant[-1]
                        unvisited_nodes = set(range(num_nodes)) - set(ant)

                        probabilities = []
                        total_pheromone = 0
                        for node in unvisited_nodes:
                            pheromone = graph[current_node][node]["pheromone"]
                            distance = graph[current_node][node]["distance"]
                            total_pheromone += (pheromone**alpha) * (distance**beta)

                        for node in unvisited_nodes:
                            pheromone = graph[current_node][node]["pheromone"]
                            distance = graph[current_node][node]["distance"]
                            probability = (
                                (pheromone**alpha) * (distance**beta)
                            ) / total_pheromone
                            probabilities.append(probability)

                        next_node = random.choices(
                            list(unvisited_nodes), probabilities
                        )[0]
                        ant.append(next_node)
            if on_Return == True:
                for ant in ants:
                    ant.append(start_node)

                for i in range(num_ants):
                    path = ants[i]
                    cost = self.calculate_cost(graph, path)
                    if cost < best_cost:
                        best_cost = cost
                        best_path = path
                    for j in range(num_nodes):
                        graph[path[j]][path[j + 1]]["pheromone"] += 1 / cost

                for edge in graph.edges():
                    graph[edge[0]][edge[1]]["pheromone"] *= 1 - evaporation_rate
                return best_path, best_cost
            else:
                for i in range(num_ants):
                    path = ants[i]
                    cost = self.calculate_cost(graph, path)
                    if cost < best_cost:
                        best_cost = cost
                        best_path = path
                    for j in range(num_nodes - 1):
                        graph[path[j]][path[j + 1]]["pheromone"] += 1 / cost

                for edge in graph.edges():
                    graph[edge[0]][edge[1]]["pheromone"] *= 1 - evaporation_rate

                best_path.remove(start_node)
                best_path = [start_node] + best_path
                return best_path, best_cost
        except ValueError as e:
            print("Log Error", e)

    def use_Ant(self, point, start_Point, on_Return, mode_Start):
        try:
            if mode_Start == True:
                point.insert(0, start_Point)
            num_nodes = len(point)
            random.seed(42)
            graph = nx.complete_graph(num_nodes)
            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):
                    distance = self.calculate_distance(point[i], point[j])
                    graph[i][j]["distance"] = distance
                    graph[j][i]["distance"] = distance
                    graph[i][j]["pheromone"] = 1.0
                    graph[j][i]["pheromone"] = 1.0

            start_node = 0
            best_path, best_cost = self.ant_colony_optimization(
                on_Return,
                graph,
                num_ants=20,
                num_iterations=100,
                alpha=1,
                beta=2,
                evaporation_rate=0.5,
                start_node=start_node,
            )
            route = self.convent_Route(best_path, point)
            cost = round(best_cost, 3)
            return route, cost
        except ValueError as e:
            print("Log Error", e)


# coordinate_list = [
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

# start_coordinate = [10.810362958119587, 106.6649108539821]

# Ant().use_Ant(coordinate_list, start_coordinate, True)
