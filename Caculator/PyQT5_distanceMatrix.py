from geopy.distance import great_circle
class distance_Matrix():
    def __init__(self):
        print('Distance Matrix')

    def calculate_distances(data):
        def euclidean_distance(point1, point2):
            distances=great_circle(point1, point2).kilometers
            
            distances=round(distances, 3)
            
            return distances
        num_points = len(data)
        distances = [[0 for _ in range(num_points)] for _ in range(num_points)]

        for i in range(num_points):
            for j in range(i + 1, num_points):
                distance = euclidean_distance(data[i], data[j])
                distances[i][j] = distance
                distances[j][i] = distance  # Ma trận đối xứng
        return distances 
