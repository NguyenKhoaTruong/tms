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
        fit_Data = []
        new_Data = []
        kmeans = KMeans(n_clusters=num_Cluster, random_state=0)
        threshold_distance_km = 2
        # for i in range(len(data)):
        kmeans.fit(data)
        labels = kmeans.labels_

        distances_km = [
            great_circle(data[j], kmeans.cluster_centers_[labels[j]]).kilometers
            for j in range(len(data))
        ]
        for j in range(len(data)):
            if distances_km[j] <= threshold_distance_km:
                fit_Data.append(data[j])
            else:
                new_Data.append(data[j])
        if len(fit_Data) < len(data):
            kmeans = KMeans(n_clusters=num_Cluster, random_state=0)
            data = fit_Data
        elif len(new_Data) > 0:
            kmeans = KMeans(n_clusters=num_Cluster, random_state=0)
            data = new_Data
        elif len(fit_Data) == len(data):
            print("Process Data")
        else:
            print("Processing....")
        # self.data_Center = kmeans.cluster_centers_.tolist()
        # for cluster_label in range(len(kmeans.cluster_centers_)):
        #     point = np.array(
        #         [data[i] for i in range(len(data)) if labels[i] == cluster_label]
        #     )
        #     self.data_Point.append(point)
        # print("check value data center", self.data_Center)
        # print("check value data point", self.data_Point)
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


num_Cluster = 10
data = [
    [10.79873893, 106.58475074],
    [10.76494905, 106.63425263],
    [10.80654415, 106.63419073],
    [10.76407979, 106.57976891],
    [10.7400531, 106.73387648],
    [10.79008932, 106.64003442],
    [10.82361435, 106.68602501],
    [10.76510526, 106.60136309],
    [10.754276, 106.65038487],
    [10.73252319, 106.70693794],
    [10.77968236, 106.63120246],
    [10.82526124, 106.70667993],
    [10.73769961, 106.72571768],
    [10.82866704, 106.67410763],
    [10.77849179, 106.66544417],
    [10.7410835, 106.70203763],
    [10.82395543, 106.69219394],
    [10.83674148, 106.68341207],
    [10.83382762, 106.67059324],
    [10.92673758, 106.55686148],
    [10.74950402, 106.65453533],
    [10.95901629, 106.50469228],
    [10.7547127, 106.633261],
    [10.69472676, 106.58839643],
    [10.86442298, 106.58982154],
    [10.76906319, 106.65309533],
    [10.73935071, 106.62920119],
    [10.76761123, 106.68591328],
    [10.76904968, 106.6657765],
    [10.75364472, 106.6133353],
    [10.82728301, 106.81193994],
    [10.76295414, 106.65702261],
    [10.75631753, 106.69231771],
    [10.80530015, 106.67858332],
    [10.75511243, 106.69004244],
    [10.6855854, 106.62249707],
    [10.79623274, 106.7405364],
    [10.74838756, 106.70536196],
    [10.82428508, 106.68272749],
    [10.83493002, 106.66219502],
    [10.82608672, 106.81733426],
    [10.86822489, 106.73579149],
    [10.73663306, 106.61394474],
    [10.76027751, 106.66189974],
    [10.74433337, 106.65502917],
    [10.85905418, 106.77776524],
    [10.80140875, 106.61857143],
    [10.82793967, 106.72155997],
    [10.8009655, 106.65353683],
    [10.7495301, 106.7084913],
    [10.75422204, 106.65166155],
    [10.7854681, 106.64193117],
    [10.8345276, 106.66475696],
    [10.83091125, 106.61499504],
    [10.66685789, 106.72514617],
    [10.75313396, 106.70073883],
    [10.81524199, 106.67207383],
    [10.63321175, 106.76237679],
    [10.77569148, 106.63053734],
    [10.78796334, 106.699553],
    [10.77059664, 106.66947987],
    [10.78661084, 106.64514608],
    [10.80091801, 106.65822372],
    [10.79501296, 106.72188185],
    [10.73380934, 106.70672371],
    [10.71850927, 106.74344459],
    [10.82839675, 106.62040336],
    [10.79911036, 106.68928578],
    [10.84141666, 106.74553243],
    [10.74285159, 106.61222465],
    [10.69713383, 106.59701609],
    [10.88967811, 106.59629605],
    [10.79777172, 106.65901639],
    [10.73362232, 106.67453329],
    [10.80604494, 106.66638702],
    [10.73155845, 106.6042846],
    [10.78684742, 106.67529388],
    [10.77469691, 106.67481141],
    [10.77034333, 106.6292236],
    [10.77184099, 106.67001309],
    [10.76848879, 106.6680193],
    [10.89545954, 106.62185635],
    [10.75422933, 106.66689835],
    [10.81400104, 106.61363473],
    [10.85086822, 106.66312291],
    [10.82270239, 106.62942746],
    [10.77499786, 106.6309953],
    [10.76841465, 106.61687605],
    [10.77446015, 106.65657468],
    [10.7933844, 106.64185857],
    [10.68408575, 106.55215376],
    [10.79737064, 106.62031109],
    [10.77849039, 106.66544494],
]

Kmean_().get_DataShowMap(data, num_Cluster)
