import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from UI.PYQT5_Compare_Kmeans import ui_Test
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import time


class CompareAccuracy:
    def __init__(self):
        print("Compare Accuracy")
        self.n_Iterations = 100
        self.random_State = 10

    def show_Accuracy(self, main_UI, data, label, centroid):
        timer_Kmean = []
        time_MiniKmean = []

        def show_ImgCompare(name_Compare):
            if name_Compare == "K_Means":
                self.cal_Kmean(data, label,centroid)
                main_UI.show_UI = ui_Test()
                main_UI.show_UI.show()
                # hiển thị giao diện web view ở đây
            #     self.cal_MiniBatchKmean(
            #         data, cluster, num_Iterations, state, position[1]
            #     )
            # elif name_Compare == "Kmean_GaussianMixture":
            #     self.cal_Kmean(data, cluster, num_Iterations, state)
            #     self.cal_GausianMixture(
            #         data, cluster, num_Iterations, state, position[1]
            #     )
            # elif name_Compare == "GaussianMixture_MiniKmean":
            #     self.cal_MiniBatchKmean(
            #         data, cluster, num_Iterations, state, position[0]
            #     )
            #     self.cal_GausianMixture(
            #         data, cluster, num_Iterations, state, position[1]
            #     )

        show_ImgCompare("K_Means")
        return timer_Kmean, time_MiniKmean

    def cal_Kmean(self, data, label,cluster):
        for i, items in enumerate(cluster):
            plt.figure(figsize=(10, 10))
            # plt.subplot(len(cluster), 2, i + 1)
            plt.scatter(data[:, 0], data[:, 1], c=label[i], cmap="viridis")
            plt.scatter(
                cluster[i][:, 0],
                cluster[i][:, 1],
                marker="x",
                s=200,
                linewidths=3,
                color="r",
            )
            plt.title(f"K-means: Iterations: {i+1},\n")
            plt.savefig(f"Assets\Img_Compare\K_Means_{i+1}", bbox_inches="tight")

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

    def char_GausianMixture():
        return False
