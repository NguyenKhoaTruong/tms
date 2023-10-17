import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations


class Lin_Kernighan_Heuristic_Cluster:
    def __init__(self):
        print("Lin_Kernighan_Heuristic_Cluster")

    def format_lat_lon(point):
        return "{:.8f},{:.8f}".format(point[0], point[1])

    def lin_kernighan(points, distances, on, off, start_point_index=0):
        def total_distance(path, distances):
            # hàm tính khoảng cách giữa các điểm và quay về điểm ban đầu
            total = 0
            if on == True:
                for i in range(len(path) - 1):
                    total += distances[path[i]][path[i + 1]]
                total += distances[path[-1]][path[0]]  # Quay về điểm xuất phát
            elif off == True:
                for i in range(len(path) - 1):
                    total += distances[path[i]][path[i + 1]]
            return total

        n = len(points)
        best_distance = np.inf
        best_path = []

        for perm in permutations(range(n)):
            # Di chuyển điểm xuất phát đến vị trí được chỉ định bằng tham số start_point_index
            perm = list(perm)
            start_point = perm.pop(start_point_index)
            perm.insert(0, start_point)
            # Áp dụng Lin-Kernighan Heuristic
            improved = True
            while improved:
                improved = False
                for i in range(n - 1):
                    for j in range(i + 2, n):
                        if j - i == 1:
                            continue
                        new_perm = (
                            perm[: i + 1] + perm[i + 1 : j + 1][::-1] + perm[j + 1 :]
                        )
                        new_distance = total_distance(new_perm, distances)
                        if new_distance < total_distance(perm, distances):
                            perm = new_perm
                            improved = True

            # Lưu lại kết quả tốt nhất
            current_distance = total_distance(perm, distances)
            if current_distance < best_distance:
                best_distance = current_distance
                best_path = perm
        # if on == True:
        #     best_path=best_path.append(best_path[0])

        return best_path, best_distance
