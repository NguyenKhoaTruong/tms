from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import time


class CompareAccuracy:
    def __init__(self):
        print("Compare Accuracy")
        self.num_Clutered = [10, 15, 20, 25, 30]
        self.n_Iterations = [200, 400, 600, 800, 1000]
        self.random_State = self.n_Iterations.copy()

    def show_Accuracy(self, data):
        # Timer
        self.compare_Accuracy(
            data, self.num_Clutered, self.n_Iterations, self.random_State
        )

    def compare_Accuracy(self, data, cluster, num_Iterations, state):
        timer_Kmean = []
        time_MiniKmean = []

        def show_ImgCompare(name_Compare):
            position = [1, 2]
            # Show Image Compare Algorithms
            plt.figure(figsize=(19, 12))
            if name_Compare == "Kmean_MiniBatchKmean":
                self.cal_Kmean(data, cluster, num_Iterations, state)
                self.cal_MiniBatchKmean(
                    data, cluster, num_Iterations, state, position[1]
                )
            elif name_Compare == "Kmean_GaussianMixture":
                self.cal_Kmean(data, cluster, num_Iterations, state)
                self.cal_GausianMixture(
                    data, cluster, num_Iterations, state, position[1]
                )
            elif name_Compare == "GaussianMixture_MiniKmean":
                self.cal_MiniBatchKmean(
                    data, cluster, num_Iterations, state, position[0]
                )
                self.cal_GausianMixture(
                    data, cluster, num_Iterations, state, position[1]
                )
            plt.tight_layout()
            plt.show()

        show_ImgCompare("Kmean_MiniBatchKmean"), show_ImgCompare(
            "Kmean_GaussianMixture"
        ), show_ImgCompare("GaussianMixture_MiniKmean")
        return timer_Kmean, time_MiniKmean

    def cal_Kmean(self, data, cluster, num_Iterations, state):
        for i, items in enumerate(cluster):
            start_time = time.time()
            kmeans = KMeans(
                n_clusters=cluster[i],
                max_iter=num_Iterations[i],
                random_state=state[i],
            )
            kmeans.fit(data)
            kmeans_time = time.time() - start_time
            silhouette_ScoreKmean = silhouette_score(
                data, kmeans.labels_
            )  # Silhouette Score
            # Paint Chart
            plt.subplot(len(self.num_Clutered), 2, i * 2 + 1)
            plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap="viridis")
            plt.scatter(
                kmeans.cluster_centers_[:, 0],
                kmeans.cluster_centers_[:, 1],
                marker="x",
                s=200,
                linewidths=3,
                color="r",
            )
            plt.title(
                f"K-means: Clusters: {cluster[i]}, Iterations: {num_Iterations[i]},Time: {kmeans_time:.2f} seconds\nSilhouette Score:{silhouette_ScoreKmean:.2f},Inertia:{kmeans.inertia_:.2f}"
            )

    def cal_MiniBatchKmean(self, data, cluster, num_Iterations, state, position):
        for i, items in enumerate(cluster):
            start_time = time.time()
            minibatch_kmeans = MiniBatchKMeans(
                n_clusters=cluster[i],
                max_iter=num_Iterations[i],
                random_state=state[i],
            )
            minibatch_kmeans.fit(data)
            minibatch_kmeans_time = time.time() - start_time
            silhouette_ScoreMiniKmean = silhouette_score(
                data, minibatch_kmeans.labels_
            )  # Silhouette Score
            plt.subplot(len(self.num_Clutered), 2, i * 2 + position)
            plt.scatter(
                data[:, 0], data[:, 1], c=minibatch_kmeans.labels_, cmap="viridis"
            )
            plt.scatter(
                minibatch_kmeans.cluster_centers_[:, 0],
                minibatch_kmeans.cluster_centers_[:, 1],
                marker="x",
                s=200,
                linewidths=3,
                color="r",
            )
            plt.title(
                f"Mini Batch K-means: Clusters: {cluster[i]}, Iterations: {num_Iterations[i]},Time: {minibatch_kmeans_time:.2f} seconds\n Silhouette Score:{silhouette_ScoreMiniKmean:.2f},Inertia:{minibatch_kmeans.inertia_:.2f}"
            )

    def cal_GausianMixture(self, data, cluster, num_Iterations, state, position):
        for i, items in enumerate(cluster):
            start_time = time.time()
            gmm = GaussianMixture(
                n_components=cluster[i],
                random_state=state[i],
                max_iter=num_Iterations[i],
            )
            gmm.fit(data)
            labels = gmm.predict(data)
            means = gmm.means_
            gausian_MixtureTime = time.time() - start_time
            silhouette_ScoreMiniKmean = silhouette_score(
                data, labels
            )  # Silhouette Score
            plt.subplot(len(self.num_Clutered), 2, i * 2 + position)
            plt.scatter(data[:, 0], data[:, 1], c=labels, cmap="viridis")
            plt.scatter(
                means[:, 0],
                means[:, 1],
                marker="x",
                s=200,
                linewidths=3,
                color="r",
            )
            plt.title(
                f"Gaussian Mixture: Clusters: {cluster[i]}, Iterations: {num_Iterations[i]},Time: {gausian_MixtureTime:.2f} seconds\n Silhouette Score:{silhouette_ScoreMiniKmean:.2f}"
            )

    def char_Kmean(self, data, timer):
        time = timer[:4]
        kmean = timer[4:]
        plt.figure(figsize=(16, 12))
        for i in range(len(time)):
            plt.subplot(2, 2, i + 1)
            plt.scatter(data[:, 0], data[:, 1], c=kmean.labels_, cmap="viridis")
            plt.scatter(
                kmean.cluster_centers_[:, 0],
                kmean.cluster_centers_[:, 1],
                marker="x",
                s=200,
                linewidths=3,
                color="r",
            )
            plt.title("K-means Clustering")
            plt.xlabel("Time: {:.2f} seconds".format(time[i]))
        plt.tight_layout()
        plt.show()

    def char_MiniBatchKmean(self):
        print()

    def char_GausianMixture():
        return False
