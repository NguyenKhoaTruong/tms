class two_OPT:
    def __init__(self):
        print("Thuật toán 2-OPT")
        # hàm tính thời gian

    def calculate_total_distance(points, route, on, off, distances):
        # tính khoảng cách giữa các điểm và quay về điểm ban đầu
        total_distance = 0
        if on == True:
            for i in range(len(route) - 1):
                total_distance += distances[route[i]][route[i + 1]]
            total_distance += distances[route[-1]][route[0]]
        elif off == True:
            for i in range(len(route) - 1):
                total_distance += distances[route[i]][route[i + 1]]
        return total_distance

    # hàm tính thuật toán
    def two_opt(route, distances, points, on, off):
        def calculate_total_distance(points, route, on, off):
            # tính khoảng cách giữa các điểm và quay về điểm ban đầu
            total_distance = 0
            if on == True:
                for i in range(len(route) - 1):
                    total_distance += distances[route[i]][route[i + 1]]
                total_distance += distances[route[-1]][route[0]]
            elif off == True:
                for i in range(len(route) - 1):
                    total_distance += distances[route[i]][route[i + 1]]
            return total_distance

        best_route = route.copy()
        improved = True
        while improved:
            improved = False
            for i in range(1, len(route) - 1):
                for j in range(i + 1, len(route)):
                    new_route = route[:i] + route[i : j + 1][::-1] + route[j + 1 :]
                    new_distance = calculate_total_distance(points, new_route, on, off)
                    if new_distance < calculate_total_distance(
                        points, best_route, on, off
                    ):
                        best_route = new_route
                        improved = True

            route = best_route
        if on == True:
            best_route.append(best_route[0])
        return best_route
