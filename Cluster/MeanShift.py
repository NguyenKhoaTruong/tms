import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt


class Mean_Shift_:
    def __init__(self):
        print("Mean Shift")

    def convent_Point(self, data, labels):
        point = []
        for i in range(int(10)):
            cluster_points = data[labels == i]
            point.append(cluster_points)
        return point

    def get_DataShowMap(self, data):
        bandwidth = estimate_bandwidth(data, quantile=0.2)
        ms = MeanShift()
        ms.fit(data)
        data_Center = ms.cluster_centers_.tolist()
        labels = ms.labels_
        data_Point = self.convent_Point(data, labels)
        return data_Center, data_Point

    def show_Char(self, data, ms, cluster_centers):
        plt.scatter(data[:, 1], data[:, 0], c=ms.labels_)
        plt.scatter(
            cluster_centers[:, 1], cluster_centers[:, 0], c="red", marker="x", s=100
        )
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Mean-Shift Clustering")
        plt.show()
