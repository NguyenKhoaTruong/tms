import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from UI.PYQT5_Compare_Kmeans import ui_Test
from UI.PYQT5_CompareDataTable import ui_DataTableCompare
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import time


class CompareAccuracy:
    def __init__(self):
        self.n_Iterations = 100
        self.random_State = 10
    def show_TableAccuracy(self,main_UI,data,point,type):
        main_UI.show_UI=ui_DataTableCompare(data,point,type)
        main_UI.show_UI.show()
    def show_Accuracy(self, main_UI, data, label, centroid):
        timer_Kmean = []
        time_MiniKmean = []

        def show_ImgCompare(name_Compare):
            if name_Compare == "K_Means":
                self.cal_Kmean(data, label,centroid)
                main_UI.show_UI = ui_Test()
                main_UI.show_UI.show()
        show_ImgCompare("K_Means")
        return timer_Kmean, time_MiniKmean

    def cal_Kmean(self, data, label,cluster):
        for i, items in enumerate(cluster):
            plt.figure(figsize=(10, 10))
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

