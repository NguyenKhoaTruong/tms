import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def kmeans_algorithm(data, n_clusters, max_iter=300, tol=1e-4):
    """
    Thực hiện thuật toán K-means trên dữ liệu và lưu trữ lịch sử centroids.

    Parameters:
    - data: Dữ liệu đầu vào.
    - n_clusters: Số lượng cụm.
    - max_iter: Số lần lặp tối đa.
    - tol: Điều kiện dừng dựa trên sự thay đổi nhỏ của centroids.

    Returns:
    - centroids_history: Lịch sử centroids sau mỗi lần lặp.
    """
    centroids_history = []

    kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, tol=tol)
    kmeans.fit(data)
    centroids_history.append(kmeans.cluster_centers_.copy())

    while True:
        prev_centroids = kmeans.cluster_centers_.copy()
        kmeans.fit(data)
        centroids_history.append(kmeans.cluster_centers_.copy())
        if np.linalg.norm(prev_centroids - kmeans.cluster_centers_) < tol:
            break

    return centroids_history


def plot_kmeans_iterations(data, centroids_history):
    """
    Hiển thị biểu đồ qua các lần thực hiện của thuật toán K-means.

    Parameters:
    - data: Dữ liệu đầu vào.
    - centroids_history: Lịch sử centroids sau mỗi lần lặp.
    """
    fig, axs = plt.subplots(
        1, len(centroids_history), figsize=(5 * len(centroids_history), 5)
    )

    for i, centroids in enumerate(centroids_history):
        labels = (
            KMeans(n_clusters=len(centroids), init=centroids, n_init=1)
            .fit(data)
            .labels_
        )
        axs[i].scatter(data[:, 0], data[:, 1], c=labels, cmap="viridis")
        axs[i].scatter(
            centroids[:, 0],
            centroids[:, 1],
            marker="X",
            s=200,
            linewidths=3,
            color="r",
            label="Centroids",
        )
        axs[i].legend()
        axs[i].set_title(f"Iteration {i + 1}")

    plt.tight_layout()
    plt.show()


# Tạo dữ liệu mẫu
data, labels = make_blobs(n_samples=100, centers=10)

# Thực hiện thuật toán K-means và lưu trữ lịch sử centroids
n_clusters = 10
centroids_history = kmeans_algorithm(data, n_clusters)

# Hiển thị biểu đồ qua các lần thực hiện của thuật toán K-means
plot_kmeans_iterations(data, centroids_history)
