import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Lib.process_Data import process_Data
from Lib.caculator_Distacne import distance_Matrix
from sklearn.cluster import KMeans
import numpy as np


class use_Kmean:
    def __init__(self):
        self.data_Center = []
        self.data_Numeric = []
        self.data_Matrix = []
        self.data_Point = []
        self.num_clusters = 0
        self.data_Numeric_ = []

    def data_Kmean(self, data):
        data_array = np.array(data)
        for item in data_array:
            for row in item:
                self.data_Numeric.append(
                    np.array([row[2], row[3], float(row[5]), float(row[6])])
                )
        for value in self.data_Numeric:
            data_ = value.tolist()
            self.data_Numeric_.append(data_)

        kmeans = KMeans(n_clusters=self.cal_Cluster(self.data_Numeric_))
        kmeans.fit(self.data_Numeric_)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_

        for i in range(self.cal_Cluster(self.data_Numeric_)):
            cluster_data = [data[j] for j in range(len(data)) if labels[j] == i]
            self.data_Matrix.append(cluster_data)

        for value in centers:
            self.data_Center.append([value[2], value[3]])

        data_ = self.convent_Data_Point(self.data_Matrix)
        return data_

    def cal_Cluster(self, data):
        if len(data) > 10 and len(data) <= 15:
            self.num_clusters = 3
        elif len(data) > 15 and len(data) <= 25:
            self.num_clusters = 5
        elif len(data) > 25:
            self.num_clusters = 8
        return self.num_clusters

    def show_Num_Trip(self, num_Trip):
        for item in range(num_Trip):
            print(f"Trip {item+1} ")
        return num_Trip

    def convent_Data_Point(self, data):
        point = []
        for value in data:
            sub_Data = []
            if len(value) == 0:
                print("...")
            else:
                for item in value:
                    for items in item:
                        lat = items[5]
                        lon = items[6]
                        sub_Data.append((float(lat), float(lon)))
                point.append(sub_Data)
        print("check value point", point)
        return point
