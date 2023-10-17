
from sklearn.cluster import KMeans
import numpy as np
# Chuyển đổi sau:
class K_Means_Cluster:
    def __init__(self,data_Cluster,cbCluster):
        self.data_Point=[]
        self.data_Center=[]
        self.data_Matrix=[]
        self.cluster(data_Cluster,cbCluster)
    def convert_Data(self,data_Cluster):
        # Chuyển đổi dữ liệu thành mảng NumPy
        data_array = np.array(data_Cluster)     
        # ma trận giữa các điểm dữ liệu
        array_Matrix = np.array([[item[2], item[3], float(item[5]), float(item[6])] for item in data_array]) 
        return data_array,array_Matrix 
    def divide_Data(self,data_Cluster):
        data_Select,matrix_Select=self.convert_Data(data_Cluster)
        
        if len(data_Select)>10 and len(data_Select)<=15:
            num_clusters = 3
        elif len(data_Select)>15 and len(data_Select)<=25:
            num_clusters= 5
        return num_clusters
    def cluster(self,data_Cluster,cbCluster):
        num_clusters=self.divide_Data(data_Cluster)
        data,matrix_data=self.convert_Data(data_Cluster)
        
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(matrix_data)
    
        label_Data=kmeans.labels_
        point_Center=kmeans.cluster_centers_
        
        for i in range(num_clusters):
            cluster_data = [data_Cluster[j] for j in range(len(data_Cluster)) if label_Data[j] == i]
            self.data_Matrix.append(cluster_data)
            
        for value in point_Center:
            self.data_Center.append([value[2],value[3]])
            
        for i in range(num_clusters):
            cluster_points = matrix_data[label_Data == i]
            self.data_Point.append(cluster_points)

        cbCluster.addItems([f"Trip {i+1}" for i in range(len(self.data_Point))])
        cbCluster.setCurrentIndex(0)
        cbCluster.currentIndexChanged.connect(self.show_Data_K_Mean_TSP)
        
# Xem chi tiết các cụm:
# for i in range(self.num_clusters):
#     cluster_points = self.array_Matrix[label_Data == i]
#     self.data_Point.append(cluster_points)
#     print(f"Cluster {i+1}:")
#     print(cluster_points)  
        