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
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, MiniBatchKMeans
import time

np.random.seed(0)
X = np.random.randn(500, 2)
print("check value data X", X, type(X))
n_clusters = 10
n_iterations = 1000

start_time = time.time()
kmeans = KMeans(n_clusters=n_clusters, max_iter=n_iterations, random_state=1000)
kmeans.fit(X)
kmeans_time = time.time() - start_time

start_time = time.time()
minibatch_kmeans = MiniBatchKMeans(
    n_clusters=n_clusters, max_iter=n_iterations, random_state=1000
)
minibatch_kmeans.fit(X)
minibatch_kmeans_time = time.time() - start_time

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
print("ádasd", X[:, 0])
plt.figure(figsize=(16, 12))  # Điều chỉnh kích thước của hình ảnh

# Vẽ biểu đồ thứ 1
plt.subplot(2, 2, 0)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="x",
    s=200,
    linewidths=3,
    color="r",
)
plt.title("K-means Clustering")
plt.xlabel("Time: {:.2f} seconds".format(kmeans_time))

# Vẽ biểu đồ thứ 2
plt.subplot(2, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=minibatch_kmeans.labels_, cmap="viridis")
plt.scatter(
    minibatch_kmeans.cluster_centers_[:, 0],
    minibatch_kmeans.cluster_centers_[:, 1],
    marker="x",
    s=200,
    linewidths=3,
    color="r",
)
plt.title("Mini Batch K-means Clustering")
plt.xlabel("Time: {:.2f} seconds".format(minibatch_kmeans_time))

# Vẽ biểu đồ thứ 3
plt.subplot(2, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="x",
    s=200,
    linewidths=3,
    color="r",
)
plt.title("K-means Clustering")
plt.xlabel("Time: {:.2f} seconds".format(kmeans_time))

# Vẽ biểu đồ thứ 4
plt.subplot(2, 2, 3)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="x",
    s=200,
    linewidths=3,
    color="r",
)
plt.title("K-means Clustering")
plt.xlabel("Time: {:.2f} seconds".format(kmeans_time))

plt.tight_layout()
plt.show()
