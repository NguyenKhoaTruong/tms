# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans, MiniBatchKMeans
# from sklearn.datasets import make_blobs

# n_samples = 100
# n_clusters = 10
# X, y = make_blobs(n_samples=n_samples, centers=n_clusters, random_state=0)

# kmeans = KMeans(n_clusters=n_clusters, random_state=0)
# mini_batch_kmeans = MiniBatchKMeans(n_clusters=n_clusters, random_state=0)

# kmeans.fit(X)
# mini_batch_kmeans.fit(X)

# # Dự đoán trên tập kiểm tra
# kmeans_test_labels = kmeans.predict(X)
# mini_batch_kmeans_test_labels = mini_batch_kmeans.predict(X)

# # Trực quan hóa kết quả
# plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", s=50)
# plt.title("Dữ liệu ban đầu (Ground Truth)")

# plt.subplot(1, 2, 2)
# plt.scatter(X[:, 0], X[:, 1], c=kmeans_test_labels, cmap="viridis", s=50)
# plt.scatter(
#     kmeans.cluster_centers_[:, 0],
#     kmeans.cluster_centers_[:, 1],
#     c="red",
#     marker="x",
#     s=200,
#     label="Centroids",
# )
# plt.title("K-Means Clustering")

# # plt.show()

# plt.figure(figsize=(12, 5))

# plt.subplot(2, 2, 3)
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", s=50)
# plt.title("Dữ liệu ban đầu (Ground Truth)")

# plt.subplot(2, 2, 4)
# plt.scatter(X[:, 0], X[:, 1], c=mini_batch_kmeans_test_labels, cmap="viridis", s=50)
# plt.scatter(
#     mini_batch_kmeans.cluster_centers_[:, 0],
#     mini_batch_kmeans.cluster_centers_[:, 1],
#     c="red",
#     marker="x",
#     s=200,
#     label="Centroids",
# )
# plt.title("Mini-Batch K-Means Clustering")

# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans, MiniBatchKMeans
# import time

# np.random.seed(0)
# X = np.random.randn(500, 2)
# print("check value data X", X, type(X))
# n_clusters = 10
# n_iterations = 1000

# start_time = time.time()
# kmeans = KMeans(n_clusters=n_clusters, max_iter=n_iterations, random_state=1000)
# kmeans.fit(X)
# kmeans_time = time.time() - start_time

# start_time = time.time()
# minibatch_kmeans = MiniBatchKMeans(
#     n_clusters=n_clusters, max_iter=n_iterations, random_state=1000
# )
# minibatch_kmeans.fit(X)
# minibatch_kmeans_time = time.time() - start_time

# plt.figure(figsize=(24, 24))

# plt.subplot(1, 2, 1)
# plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
# plt.scatter(
#     kmeans.cluster_centers_[:, 0],
#     kmeans.cluster_centers_[:, 1],
#     marker="x",
#     s=200,
#     linewidths=3,
#     color="r",
# )
# plt.title("K-means Clustering")
# plt.xlabel("Time: {:.2f} seconds".format(kmeans_time))

# plt.subplot(1, 2, 2)
# plt.scatter(X[:, 0], X[:, 1], c=minibatch_kmeans.labels_, cmap="viridis")
# plt.scatter(
#     minibatch_kmeans.cluster_centers_[:, 0],
#     minibatch_kmeans.cluster_centers_[:, 1],
#     marker="x",
#     s=200,
#     linewidths=3,
#     color="r",
# )
# plt.title("Mini Batch K-means Clustering")
# plt.xlabel("Time: {:.2f} seconds".format(minibatch_kmeans_time))


# plt.subplot(3, 2, 3)
# plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
# plt.scatter(
#     kmeans.cluster_centers_[:, 0],
#     kmeans.cluster_centers_[:, 1],
#     marker="x",
#     s=200,
#     linewidths=3,
#     color="r",
# )
# plt.title("K-means Clustering")
# plt.xlabel("Time: {:.2f} seconds".format(kmeans_time))

# plt.subplot(3, 2, 4)
# plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
# plt.scatter(
#     kmeans.cluster_centers_[:, 0],
#     kmeans.cluster_centers_[:, 1],
#     marker="x",
#     s=200,
#     linewidths=3,
#     color="r",
# )
# plt.title("K-means Clustering")
# plt.xlabel("Time: {:.2f} seconds".format(kmeans_time))

# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans, MiniBatchKMeans
# import time

# # Tạo tập dữ liệu mô phỏng
# np.random.seed(0)
# X = np.random.randn(500, 2)

# # Số lượng cụm và số lần lặp được thay thế
# num_Clutered = [10, 20, 30, 40, 50]
# n_Iterations = [200, 400, 600, 800, 1000]
# random_State = n_Iterations.copy()
# plt.figure(figsize=(24, 24))

# for i in range(len(num_Clutered)):
#     num_clusters = num_Clutered[i]
#     n_iterations = n_Iterations[i]
#     random_States = random_State[i]
#     # Áp dụng thuật toán K-means và đo thời gian thực hiện
#     start_time = time.time()
#     kmeans = KMeans(
#         n_clusters=num_clusters, max_iter=n_iterations, random_state=random_States
#     )
#     kmeans.fit(X)
#     kmeans_time = time.time() - start_time

#     # Áp dụng thuật toán Mini Batch K-means và đo thời gian thực hiện
#     start_time = time.time()
#     minibatch_kmeans = MiniBatchKMeans(
#         n_clusters=num_clusters, max_iter=n_iterations, random_state=random_States
#     )
#     minibatch_kmeans.fit(X)
#     minibatch_kmeans_time = time.time() - start_time
#     print("check len num clstered", num_Clutered)
#     plt.subplot(len(num_Clutered), 2, i * 2 + 1)

#     # Kết quả K-means
#     plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
#     plt.scatter(
#         kmeans.cluster_centers_[:, 0],
#         kmeans.cluster_centers_[:, 1],
#         marker="x",
#         s=200,
#         linewidths=3,
#         color="r",
#     )
#     plt.title(
#         f"K-means Clustering\nClusters: {num_clusters}, Iterations: {n_iterations}\nTime: {kmeans_time:.2f} seconds"
#     )

#     # Kết quả Mini Batch K-means
#     plt.subplot(len(num_Clutered), 2, i * 2 + 2)
#     plt.scatter(X[:, 0], X[:, 1], c=minibatch_kmeans.labels_, cmap="viridis")
#     plt.scatter(
#         minibatch_kmeans.cluster_centers_[:, 0],
#         minibatch_kmeans.cluster_centers_[:, 1],
#         marker="x",
#         s=200,
#         linewidths=3,
#         color="r",
#     )
#     plt.title(
#         f"Mini Batch K-means Clustering\nClusters: {num_clusters}, Iterations: {n_iterations}\nTime: {minibatch_kmeans_time:.2f} seconds"
#     )

# plt.tight_layout()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans, MiniBatchKMeans
# from sklearn.datasets import make_blobs
# from sklearn.metrics import silhouette_score

# # Tạo dữ liệu giả định
# n_samples = 1500
# n_features = 2
# n_clusters = 10
# X, _ = make_blobs(
#     n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42
# )

# # Áp dụng K-means
# kmeans = KMeans(n_clusters=n_clusters)
# kmeans_labels = kmeans.fit_predict(X)
# kmeans_inertia = kmeans.inertia_

# # Áp dụng Mini Batch K-means
# mini_batch_kmeans = MiniBatchKMeans(n_clusters=n_clusters)
# mini_batch_labels = mini_batch_kmeans.fit_predict(X)
# mini_batch_inertia = mini_batch_kmeans.inertia_

# # Vẽ biểu đồ cho K-means
# plt.figure(figsize=(12, 4))
# plt.subplot(121)
# plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap="viridis")
# plt.scatter(
#     kmeans.cluster_centers_[:, 0],
#     kmeans.cluster_centers_[:, 1],
#     s=200,
#     c="red",
#     label="Centroids",
# )
# plt.title("K-means Clustering")
# plt.legend()
# plt.xlabel(f"Inertia: {kmeans_inertia:.2f}")

# # Vẽ biểu đồ cho Mini Batch K-means
# plt.subplot(122)
# plt.scatter(X[:, 0], X[:, 1], c=mini_batch_labels, cmap="viridis")
# plt.scatter(
#     mini_batch_kmeans.cluster_centers_[:, 0],
#     mini_batch_kmeans.cluster_centers_[:, 1],
#     s=200,
#     c="red",
#     label="Centroids",
# )
# plt.title("Mini Batch K-means Clustering")
# plt.legend()
# plt.xlabel(f"Inertia: {mini_batch_inertia:.2f}")

# plt.show()

# # Đánh giá chất lượng phân cụm bằng Silhouette Score
# print("check value data kmean label", kmeans_labels)
# silhouette_kmeans = silhouette_score(X, kmeans_labels)
# silhouette_mini_batch_kmeans = silhouette_score(X, mini_batch_labels)


# print(f"Silhouette Score for K-means: {silhouette_kmeans}")
# print(f"Silhouette Score for Mini Batch K-means: {silhouette_mini_batch_kmeans}")
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def add(self, dataval):
#         # Use list append method to add element
#         if dataval not in self.stack:
#             self.stack.append(dataval)
#             return True
#         else:
#             return False

#     # Use list pop method to remove element
#     def remove(self):
#         if len(self.stack) <= 0:
#             return "No element in the Stack"
#         else:
#             return self.stack.pop()


# AStack = Stack()
# AStack.add("Mon")
# AStack.add("Tue")

# AStack.add("Wed")
# AStack.add("Thu")

# print(AStack.remove())
# # print(AStack.remove())
# import numpy as np
# from sklearn.cluster import KMeans, MiniBatchKMeans
# import matplotlib.pyplot as plt

# # Tạo dữ liệu ngẫu nhiên
# np.random.seed(0)
# X = np.random.rand(100, 2)

# # Sử dụng K-Means
# kmeans = KMeans(n_clusters=3)
# kmeans.fit(X)
# kmeans_labels = kmeans.labels_
# kmeans_centers = kmeans.cluster_centers_
# kmeans_inertia = kmeans.inertia_

# # Sử dụng Mini-Batch K-Means
# mini_batch_kmeans = MiniBatchKMeans(n_clusters=3, batch_size=10)
# mini_batch_kmeans.fit(X)
# mini_batch_labels = mini_batch_kmeans.labels_
# mini_batch_centers = mini_batch_kmeans.cluster_centers_
# mini_batch_inertia = mini_batch_kmeans.inertia_

# # Trực quan hóa dữ liệu và trung tâm cụm
# plt.figure(figsize=(18, 6))

# plt.subplot(1, 3, 1)
# plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap="viridis")
# plt.scatter(kmeans_centers[:, 0], kmeans_centers[:, 1], c="red", marker="x")
# plt.title(f"K-Means\nInertia: {kmeans_inertia:.2f}")

# plt.subplot(2, 3, 2)
# plt.scatter(X[:, 0], X[:, 1], c=mini_batch_labels, cmap="viridis")
# plt.scatter(mini_batch_centers[:, 0], mini_batch_centers[:, 1], c="red", marker="x")
# plt.title(f"Mini-Batch K-Means\nInertia: {mini_batch_inertia:.2f}")
# plt.subplot(3, 3, 3)
# plt.scatter(X[:, 0], X[:, 1], c=mini_batch_labels, cmap="viridis")
# plt.scatter(mini_batch_centers[:, 0], mini_batch_centers[:, 1], c="red", marker="x")
# plt.title(f"Mini-Batch K-Means\nInertia: {mini_batch_inertia:.2f}")
# plt.show()
from sklearn.mixture import GaussianMixture
import numpy as np

# Tạo dữ liệu mẫu
np.random.seed(0)
X = np.random.randn(100, 2)

# Tạo mô hình GMM với số lượng phân phối Gaussian là 3 (ví dụ)
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

# Lấy giá trị Inertia từ mô hình GMM
inertia = gmm.aic(X)

print("Inertia:", inertia)
