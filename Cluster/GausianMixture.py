import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt


class Gausian:
    def __init__(self):
        print("Gausian Mixture")

    def convent_Point(self, data, labels, cluster):
        point = []
        for i in range(cluster):
            cluster_points = data[labels == i]
            point.append(cluster_points)
        return point

    def get_DataShowMap(self, data, cluster):
        gmm = GaussianMixture(n_components=cluster, random_state=0)
        gmm.fit(data)
        labels = gmm.predict(data)
        means = gmm.means_
        data_Point = self.convent_Point(data, labels, cluster)
        data_Center = [[items[0], items[1]] for items in means]

        return data_Center, data_Point

    def show_Char(self, data, labels, means):
        plt.scatter(data[:, 1], data[:, 0], c=labels, cmap="viridis")
        plt.scatter(
            means[:, 1], means[:, 0], marker="x", s=100, c="red", label="Centroids"
        )
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Phân cụm dữ liệu với Gaussian Mixture Model")
        plt.legend()
        plt.show()
