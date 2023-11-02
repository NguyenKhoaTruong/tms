# # import numpy as np
# # from sklearn.cluster import KMeans
# # from geopy.distance import great_circle
# # import matplotlib.pyplot as plt

# # # Tạo dữ liệu mẫu (latitude, longitude)
# # data = [
# #     [10.79873893, 106.58475074],
# #     [10.76494905, 106.63425263],
# #     [10.80654415, 106.63419073],
# #     [10.76407979, 106.57976891],
# #     [10.7400531, 106.73387648],
# #     [10.79008932, 106.64003442],
# #     [10.82361435, 106.68602501],
# #     [10.76510526, 106.60136309],
# #     [10.754276, 106.65038487],
# #     [10.73252319, 106.70693794],
# #     [10.77968236, 106.63120246],
# #     [10.82526124, 106.70667993],
# #     [10.73769961, 106.72571768],
# #     [10.82866704, 106.67410763],
# #     [10.77849179, 106.66544417],
# #     [10.7410835, 106.70203763],
# #     [10.82395543, 106.69219394],
# #     [10.83674148, 106.68341207],
# #     [10.83382762, 106.67059324],
# #     [10.92673758, 106.55686148],
# #     [10.74950402, 106.65453533],
# #     [10.95901629, 106.50469228],
# #     [10.7547127, 106.633261],
# #     [10.69472676, 106.58839643],
# #     [10.86442298, 106.58982154],
# #     [10.76906319, 106.65309533],
# #     [10.73935071, 106.62920119],
# #     [10.76761123, 106.68591328],
# #     [10.76904968, 106.6657765],
# #     [10.75364472, 106.6133353],
# #     [10.82728301, 106.81193994],
# #     [10.76295414, 106.65702261],
# #     [10.75631753, 106.69231771],
# #     [10.80530015, 106.67858332],
# #     [10.75511243, 106.69004244],
# #     [10.6855854, 106.62249707],
# #     [10.79623274, 106.7405364],
# #     [10.74838756, 106.70536196],
# #     [10.82428508, 106.68272749],
# #     [10.83493002, 106.66219502],
# #     [10.82608672, 106.81733426],
# #     [10.86822489, 106.73579149],
# #     [10.73663306, 106.61394474],
# #     [10.76027751, 106.66189974],
# #     [10.74433337, 106.65502917],
# #     [10.85905418, 106.77776524],
# #     [10.80140875, 106.61857143],
# #     [10.82793967, 106.72155997],
# #     [10.8009655, 106.65353683],
# #     [10.7495301, 106.7084913],
# #     [10.75422204, 106.65166155],
# #     [10.7854681, 106.64193117],
# #     [10.8345276, 106.66475696],
# #     [10.83091125, 106.61499504],
# #     [10.66685789, 106.72514617],
# #     [10.75313396, 106.70073883],
# #     [10.81524199, 106.67207383],
# #     [10.63321175, 106.76237679],
# #     [10.77569148, 106.63053734],
# #     [10.78796334, 106.699553],
# #     [10.77059664, 106.66947987],
# #     [10.78661084, 106.64514608],
# #     [10.80091801, 106.65822372],
# #     [10.79501296, 106.72188185],
# #     [10.73380934, 106.70672371],
# #     [10.71850927, 106.74344459],
# #     [10.82839675, 106.62040336],
# #     [10.79911036, 106.68928578],
# #     [10.84141666, 106.74553243],
# #     [10.74285159, 106.61222465],
# #     [10.69713383, 106.59701609],
# #     [10.88967811, 106.59629605],
# #     [10.79777172, 106.65901639],
# #     [10.73362232, 106.67453329],
# #     [10.80604494, 106.66638702],
# #     [10.73155845, 106.6042846],
# #     [10.78684742, 106.67529388],
# #     [10.77469691, 106.67481141],
# #     [10.77034333, 106.6292236],
# #     [10.77184099, 106.67001309],
# #     [10.76848879, 106.6680193],
# #     [10.89545954, 106.62185635],
# #     [10.75422933, 106.66689835],
# #     [10.81400104, 106.61363473],
# #     [10.85086822, 106.66312291],
# #     [10.82270239, 106.62942746],
# #     [10.77499786, 106.6309953],
# #     [10.76841465, 106.61687605],
# #     [10.77446015, 106.65657468],
# #     [10.7933844, 106.64185857],
# #     [10.68408575, 106.55215376],
# #     [10.79737064, 106.62031109],
# #     [10.77849039, 106.66544494],
# # ]

# # # Khởi tạo K-means với số cụm là 3
# # kmeans = KMeans(n_clusters=10, random_state=0)


# # threshold_distance_km = 10  # Ngưỡng khoảng cách (đơn vị km)
# # for i in range(len(data)):  # Số lần lặp tối đa
# #     kmeans.fit(data)
# #     labels = kmeans.labels_

# #     # Tính khoảng cách từ các điểm dữ liệu đến centroid (sử dụng great-circle distance)
# #     distances_km = [
# #         great_circle(data[j], kmeans.cluster_centers_[labels[j]]).kilometers
# #         for j in range(len(data))
# #     ]
# #     new_data = []
# #     new_data_wrong = []
# #     for j in range(len(data)):
# #         if distances_km[j] <= threshold_distance_km:
# #             new_data.append(data[j])
# #         else:
# #             new_data_wrong.append(data[j])

# #     if len(new_data) < len(data):
# #         kmeans = KMeans(n_clusters=10, random_state=0)
# #         data = new_data
# #     print("check vlaue new data", new_data)
# #     print("check vlaeu new wrong data", new_data_wrong)

# # combined_data = new_data

# # # Kết quả cuối cùng
# # print("Centroids (danh sách đúng):\n", kmeans.cluster_centers_)

# # # Hiển thị thông tin các điểm của từng cụm (danh sách đúng)
# # for cluster_label in range(3):
# #     cluster_data = np.array(
# #         [data[i] for i in range(len(data)) if labels[i] == cluster_label]
# #     )
# #     print(f"Cluster {cluster_label} ({len(cluster_data)} điểm):")
# #     for point in cluster_data:
# #         print(f"Latitude: {point[0]}, Longitude: {point[1]}")

# # # Hiển thị kết quả sử dụng Matplotlib (danh sách đúng và danh sách sai gộp lại)
# # combined_data = np.array(combined_data)
# # plt.scatter(combined_data[:, 1], combined_data[:, 0], c=kmeans.labels_, cmap="viridis")
# # plt.scatter(
# #     kmeans.cluster_centers_[:, 1],
# #     kmeans.cluster_centers_[:, 0],
# #     s=200,
# #     c="red",
# #     label="Centroids (danh sách đúng và danh sách sai)",
# # )
# # plt.xlabel("Longitude")
# # plt.ylabel("Latitude")
# # plt.title("K-means Clustering Result (danh sách đúng và danh sách sai gộp lại)")
# # plt.legend()
# # plt.show()
# import numpy as np
# from sklearn.cluster import KMeans
# from geopy.distance import great_circle
# import matplotlib.pyplot as plt

# # Danh sách các điểm dữ liệu (lat, lon)
# data = np.array(
#     [
#         [10.79873893, 106.58475074],
#         [10.76494905, 106.63425263],
#         [10.80654415, 106.63419073],
#         [10.76407979, 106.57976891],
#         [10.7400531, 106.73387648],
#         [10.79008932, 106.64003442],
#         [10.82361435, 106.68602501],
#         [10.76510526, 106.60136309],
#         [10.754276, 106.65038487],
#         [10.73252319, 106.70693794],
#         [10.77968236, 106.63120246],
#         [10.82526124, 106.70667993],
#         [10.73769961, 106.72571768],
#         [10.82866704, 106.67410763],
#         [10.77849179, 106.66544417],
#         [10.7410835, 106.70203763],
#         [10.82395543, 106.69219394],
#         [10.83674148, 106.68341207],
#         [10.83382762, 106.67059324],
#         [10.92673758, 106.55686148],
#         [10.74950402, 106.65453533],
#         [10.95901629, 106.50469228],
#         [10.7547127, 106.633261],
#         [10.69472676, 106.58839643],
#         [10.86442298, 106.58982154],
#         [10.76906319, 106.65309533],
#         [10.73935071, 106.62920119],
#         [10.76761123, 106.68591328],
#         [10.76904968, 106.6657765],
#         [10.75364472, 106.6133353],
#         [10.82728301, 106.81193994],
#         [10.76295414, 106.65702261],
#         [10.75631753, 106.69231771],
#         [10.80530015, 106.67858332],
#         [10.75511243, 106.69004244],
#         [10.6855854, 106.62249707],
#         [10.79623274, 106.7405364],
#         [10.74838756, 106.70536196],
#         [10.82428508, 106.68272749],
#         [10.83493002, 106.66219502],
#         [10.82608672, 106.81733426],
#         [10.86822489, 106.73579149],
#         [10.73663306, 106.61394474],
#         [10.76027751, 106.66189974],
#         [10.74433337, 106.65502917],
#         [10.85905418, 106.77776524],
#         [10.80140875, 106.61857143],
#         [10.82793967, 106.72155997],
#         [10.8009655, 106.65353683],
#         [10.7495301, 106.7084913],
#         [10.75422204, 106.65166155],
#         [10.7854681, 106.64193117],
#         [10.8345276, 106.66475696],
#         [10.83091125, 106.61499504],
#         [10.66685789, 106.72514617],
#         [10.75313396, 106.70073883],
#         [10.81524199, 106.67207383],
#         [10.63321175, 106.76237679],
#         [10.77569148, 106.63053734],
#         [10.78796334, 106.699553],
#         [10.77059664, 106.66947987],
#         [10.78661084, 106.64514608],
#         [10.80091801, 106.65822372],
#         [10.79501296, 106.72188185],
#         [10.73380934, 106.70672371],
#         [10.71850927, 106.74344459],
#         [10.82839675, 106.62040336],
#         [10.79911036, 106.68928578],
#         [10.84141666, 106.74553243],
#         [10.74285159, 106.61222465],
#         [10.69713383, 106.59701609],
#         [10.88967811, 106.59629605],
#         [10.79777172, 106.65901639],
#         [10.73362232, 106.67453329],
#         [10.80604494, 106.66638702],
#         [10.73155845, 106.6042846],
#         [10.78684742, 106.67529388],
#         [10.77469691, 106.67481141],
#         [10.77034333, 106.6292236],
#         [10.77184099, 106.67001309],
#         [10.76848879, 106.6680193],
#         [10.89545954, 106.62185635],
#         [10.75422933, 106.66689835],
#         [10.81400104, 106.61363473],
#         [10.85086822, 106.66312291],
#         [10.82270239, 106.62942746],
#         [10.77499786, 106.6309953],
#         [10.76841465, 106.61687605],
#         [10.77446015, 106.65657468],
#         [10.7933844, 106.64185857],
#         [10.68408575, 106.55215376],
#         [10.79737064, 106.62031109],
#         [10.77849039, 106.66544494],
#     ]
# )
# # Số lượng cụm ban đầu
# k = 10


# # Tạo một hàm để thực hiện K-means và hiển thị kết quả
# def perform_kmeans_and_plot(data, k, min_distance):
#     while True:
#         # Khởi tạo K-means với số cụm ban đầu
#         kmeans = KMeans(n_clusters=k, init="k-means++", random_state=0)
#         kmeans.fit(data)

#         # Kiểm tra điều kiện khoảng cách cho mỗi cụm
#         for i in range(k):
#             cluster_points = data[kmeans.labels_ == i]
#             cluster_center = kmeans.cluster_centers_[i]
#             if any(
#                 great_circle(point, cluster_center).kilometers > min_distance
#                 for point in cluster_points
#             ):
#                 # Nếu có điểm nào không thỏa mãn điều kiện, tạo ra cụm mới
#                 new_center = cluster_points.mean(axis=0)
#                 kmeans.cluster_centers_[i] = new_center

#         # Gán lại các điểm vào các cụm
#         new_labels = kmeans.predict(data)
#         if np.array_equal(kmeans.labels_, new_labels):
#             # Nếu không còn thay đổi trong việc gán các điểm vào các cụm
#             break
#         kmeans.labels_ = new_labels
#         k += 1  # Tăng số lượng cụm khi cần thiết

#     # Hiển thị kết quả trên biểu đồ
#     for i in range(k):
#         plt.scatter(
#             data[kmeans.labels_ == i][:, 1],
#             data[kmeans.labels_ == i][:, 0],
#             label=f"Cluster {i+1}",
#         )

#     plt.scatter(
#         kmeans.cluster_centers_[:, 1],
#         kmeans.cluster_centers_[:, 0],
#         s=100,
#         c="black",
#         label="Centroids",
#     )
#     plt.xlabel("Longitude")
#     plt.ylabel("Latitude")
#     plt.title("K-means Clustering")
#     plt.legend()
#     plt.show()


# # Điều chỉnh min_distance và hiển thị kết quả
# min_distance_values = [5, 10, 20]  # Các giá trị min_distance bạn muốn thử
# for min_distance in min_distance_values:
#     print(f"Min Distance: {min_distance} km")
#     perform_kmeans_and_plot(data, k, min_distance)
# import matplotlib.pyplot as plt

# # Tạo 4 hình ảnh mẫu
# image1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# image2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# image3 = [[0, 0, 0], [255, 255, 255], [128, 128, 128]]
# image4 = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]

# # Tạo subplot và hiển thị hình ảnh trong mỗi ô con
# fig, axs = plt.subplots(2, 2, figsize=(6, 6))
# fig.subplots_adjust(wspace=0.5, hspace=0.5)

# axs[0, 0].imshow(image1, cmap="gray")
# axs[0, 0].set_title("Hình 1")

# axs[0, 1].imshow(image2, cmap="gray")
# axs[0, 1].set_title("Hình 2")

# axs[1, 0].imshow(image3, cmap="gray")
# axs[1, 0].set_title("Hình 3")

# axs[1, 1].imshow(image4, cmap="gray")
# axs[1, 1].set_title("Hình 4")

# # Hiển thị các hình ảnh
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, MiniBatchKMeans
import time

# Tạo tập dữ liệu mô phỏng
np.random.seed(0)
X = np.random.randn(500, 2)

# Số lượng cụm và số lần lặp được thay thế
num_Clutered = [10, 20, 30, 40, 50]
n_Iterations = [200, 400, 600, 800, 1000]

plt.figure(figsize=(15, 12))

for i, num_clusters in enumerate(num_Clutered):
    for j, n_iterations in enumerate(n_Iterations):
        # Áp dụng thuật toán K-means và đo thời gian thực hiện
        start_time = time.time()
        kmeans = KMeans(n_clusters=num_clusters, max_iter=n_iterations, random_state=0)
        kmeans.fit(X)
        kmeans_time = time.time() - start_time

        # Áp dụng thuật toán Mini Batch K-means và đo thời gian thực hiện
        start_time = time.time()
        minibatch_kmeans = MiniBatchKMeans(
            n_clusters=num_clusters,
            max_iter=n_iterations,
            random_state=0,
            batch_size=50,
        )
        minibatch_kmeans.fit(X)
        minibatch_kmeans_time = time.time() - start_time

        # Hiển thị kết quả và thời gian thực hiện bằng Matplotlib
        plt.subplot(len(num_Clutered), len(n_Iterations), i * len(n_Iterations) + j + 1)

        # Kết quả K-means
        plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
        plt.scatter(
            kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            marker="x",
            s=200,
            linewidths=3,
            color="r",
        )
        plt.title(
            f"K-means Clustering\nClusters: {num_clusters}, Iterations: {n_iterations}\nTime: {kmeans_time:.2f} seconds"
        )

        # Kết quả Mini Batch K-means
        plt.subplot(
            len(num_Clutered),
            len(n_Iterations),
            i * len(n_Iterations) + j + 1 + len(num_Clutered) * len(n_Iterations),
        )
        plt.scatter(X[:, 0], X[:, 1], c=minibatch_kmeans.labels_, cmap="viridis")
        plt.scatter(
            minibatch_kmeans.cluster_centers_[:, 0],
            minibatch_kmeans.cluster_centers_[:, 1],
            marker="x",
            s=200,
            linewidths=3,
            color="r",
        )
        plt.title(
            f"Mini Batch K-means Clustering\nClusters: {num_clusters}, Iterations: {n_iterations}\nTime: {minibatch_kmeans_time:.2f} seconds"
        )

plt.tight_layout()
plt.show()
