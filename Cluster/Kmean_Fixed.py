import numpy as np
from sklearn.cluster import KMeans
from geopy.distance import great_circle
import matplotlib.pyplot as plt


class Kmean_:
    def __init__(self):
        print("K_mean Fixed")
        self.data_Point = []
        self.data_Center = []

    def get_DataShowMap(self, data, num_Cluster):
        kmeans = KMeans(n_clusters=num_Cluster, random_state=0)
        threshold_distance_km = 2
        for i in range(len(data)):
            kmeans.fit(data)
            labels = kmeans.labels_

            distances_km = [
                great_circle(data[j], kmeans.cluster_centers_[labels[j]]).kilometers
                for j in range(len(data))
            ]
            new_data = []

            for j in range(len(data)):
                if distances_km[j] <= threshold_distance_km:
                    new_data.append(data[j])
            if len(new_data) < len(data):
                kmeans = KMeans(n_clusters=10, random_state=0)
                data = new_data
            elif len(new_data) == len(data):
                print("Đang xử lý")
            else:
                print("Đang xử lý")

        self.data_Center = kmeans.cluster_centers_.tolist()
        for cluster_label in range(len(kmeans.cluster_centers_)):
            point = np.array(
                [data[i] for i in range(len(data)) if labels[i] == cluster_label]
            )
            self.data_Point.append(point)
        return self.data_Center, self.data_Point

    def show_Char(self, kmeans):
        data = np.array(data)
        plt.scatter(data[:, 1], data[:, 0], c=kmeans.labels_, cmap="viridis")
        plt.scatter(
            kmeans.cluster_centers_[:, 1],
            kmeans.cluster_centers_[:, 0],
            s=200,
            c="red",
            label="Centroids",
        )
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("K-means Clustering Result")
        plt.legend()
        plt.show()
