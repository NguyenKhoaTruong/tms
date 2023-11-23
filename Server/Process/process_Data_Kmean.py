import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Server.Process.map_Cluster import MapCluster
from sklearn.cluster import KMeans
import numpy as np
class Process_Data:
    def __init__(self):
        self.point=[]
        self.center=[]
        self.label=[]
    def _process(self,data):
        #filter data duplicate
        _order=self.dropDuplicateData(data['order'])
        _name_Cluster=data['name']
        _num_Cluster=data['num']
        _html=self._Kmean(_order,_name_Cluster,_num_Cluster)
        return _html
        
    def dropDuplicateData(self,*arg):
        _data=arg[0]
        temp=[]
        if _data:
            for items in _data:
                if items not in temp:
                    temp.append(items)
        else:
            return None
        return temp
    def conventDataPoint(self,_point):
        data=[]
        for items in _point:
            _q=[]
            for item in items:
                _q.append([item[0],item[1],])
            data.append(_q)
        return data
    def _Kmean(self,order,name,cluster):
        _data= np.array(order)
        _matrix = np.array([[float(item[0]),float(item[1]),]for item in _data])
        _weight = np.array([float(item[2]) for item in _data]).tolist()
        _volume = np.array([float(item[3]) for item in _data]).tolist()
        if name == "K-Means":
            _means = KMeans(
                n_clusters=cluster,
                init="k-means++",
                n_init=30,
                max_iter=100,
                tol=1e-4,
            )
            _means.fit(_matrix,sample_weight=_weight)
            label = _means.labels_
            center = _means.cluster_centers_.tolist()
            point=self.set_ValueDataPoint(_matrix,label,cluster)
            _newPoint=self.conventDataPoint(point)
            radius=self.show_radius_Cluster(_newPoint,center)
            
        else:
            print('No Algorithms Cluster Running')
        _html=MapCluster().showMap(_newPoint,center,radius)
        return _html

    def set_ValueDataPoint(self,data,labels,_num):
        _point=[]
        for i in range(_num):
            cluster_points = data[labels == i]
            _point.append(cluster_points)
        return _point
    def show_radius_Cluster(self, data_point, data_center):
        radius = []
        for i, group in enumerate(data_point):
            max_distance = 0
            for point in group:
                distance = self.haversine_distance(point, data_center[i])
                if distance > max_distance:
                    max_distance = distance
            radius.append(max_distance)
        radius = np.array(radius) * 1000
        return radius
    def haversine_distance(self, coord1, coord2):
        R = 6371  # Bán kính của Trái Đất trong kilômét
        lat1, lon1 = np.radians(list(coord1))
        lat2, lon2 = np.radians(list(coord2))

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

        distance = R * c
        return distance