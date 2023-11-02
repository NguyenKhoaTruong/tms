from sklearn.cluster import KMeans, MiniBatchKMeans
import matplotlib.pyplot as plt
import numpy as np
import time


class CompareAccuracy:
    def __init__(self):
        print("Compare Accuracy")

    def show_Accuracy(self, data, num_Cluter):
        num_Clutered = [10, 20, 30, 40, 50]
        n_Iterations = [200, 400, 600, 800, 1000]
        random_State = n_Iterations.copy()
        # Timer
        kmeans, miniKmean = self.compare_Accuracy(
            data, num_Clutered, n_Iterations, random_State
        )
        # Show char
        self.char_Kmean(data, kmeans)
        self.char_MiniBatchKmean()

    def compare_Accuracy(self, data, cluster, num_Iterations, state):
        timer_Kmean = []
        time_MiniKmean = []

        def cal_Time():
            for index, items in enumerate(cluster):
                start_time = time.time()
                tKmean, path_Kmeans = self.cal_Kmean(
                    cluster[index],
                    num_Iterations[index],
                    state[index],
                    data,
                    start_time,
                )
                timer_Kmean.insert(0, path_Kmeans)
                timer_Kmean.append(tKmean)
                # Mini Batch K-mean
                tMiniKmean, path_MiniKmean = self.cal_MiniBatchKmean(
                    cluster[index],
                    num_Iterations[index],
                    state[index],
                    data,
                    start_time,
                )
                time_MiniKmean.insert(0, path_MiniKmean)
                time_MiniKmean.append(tMiniKmean)
            return timer_Kmean, time_MiniKmean

        cal_Time()
        return timer_Kmean, time_MiniKmean

    def cal_Kmean(self, cluster, iter, state, data, start_time):
        kmeans = KMeans(
            n_clusters=cluster,
            max_iter=iter,
            random_state=state,
        )
        kmeans.fit(data)
        kmeans_time = time.time() - start_time
        return kmeans_time, kmeans

    def cal_MiniBatchKmean(self, cluster, iter, state, data, start_time):
        minibatch_kmeans = MiniBatchKMeans(
            n_clusters=cluster,
            max_iter=iter,
            random_state=state,
        )
        minibatch_kmeans.fit(data)
        minibatch_kmeans_time = time.time() - start_time
        return minibatch_kmeans_time, minibatch_kmeans

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

    def char_MiniBatchKmean(self):
        print()

    def char_GausianMixture():
        return False
