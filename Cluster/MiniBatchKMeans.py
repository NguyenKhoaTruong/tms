from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt


class Mini_Bath_KMean:
    def __init__(self):
        print("Mini Bath K Mean")

    def get_DataMap(self, data, cluster):
        kmeans = MiniBatchKMeans(n_clusters=cluster, batch_size=1024, random_state=0)
        kmeans.fit(data)
        data_Centers = kmeans.cluster_centers_.tolist()
        labels = kmeans.labels_
        data_Point = self.convent_Point(data, labels, cluster)
        return data_Centers, data_Point

    def convent_Point(self, data, labels, cluster):
        point = []
        for i in range(cluster):
            cluster_points = data[labels == i]
            point.append(cluster_points)
        return point

    def show_Char(self, data, kmeans, cluster_centers):
        plt.scatter(data[:, 1], data[:, 0], c=kmeans.labels_, cmap="rainbow")
        plt.scatter(
            cluster_centers[:, 1], cluster_centers[:, 0], marker="x", s=200, c="black"
        )
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Mini-Batch K-Means Clustering")
        plt.show()
