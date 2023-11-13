# def ham_goi_lai():
#     print("Hàm gọi lại")


# def goi_lai_de_quy(dieu_kien):
#     if not dieu_kien():
#         ham_goi_lai()
#         goi_lai_de_quy(dieu_kien)


# # Điều kiện kiểm tra
# def ham_can_kiem_tra(x):
#     return x > 10


# # Sử dụng
# goi_lai_de_quy(lambda: not ham_can_kiem_tra(5))
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

data = 5000.0
data1 = [
    [1.0, 10.79873892744089, 106.58475073864138],
    [938.72, 10.764949051934444, 106.63425262680195],
    [1897.28, 10.806544151486372, 106.63419073199863],
    [244.91, 10.764079789979318, 106.57976890751715],
    [1897.28, 10.7400530995737, 106.7338764787851],
    [1299.5, 10.790089319833042, 106.64003441699646],
    [1785.24, 10.823614351505748, 106.68602501436756],
    [510.32, 10.765105259503555, 106.6013630947109],
    [305.84, 10.754275999507401, 106.65038486747628],
    [1272.02, 10.732523192626422, 106.7069379362698],
    [1897.28, 10.779682363758237, 106.63120245625056],
    [1897.28, 10.825261241106542, 106.70667993346213],
    [898.53, 10.737699613991722, 106.72571767515892],
    [1279.91, 10.828667037403232, 106.67410762602444],
    [412.29, 10.778491793268698, 106.66544417327842],
    [936.23, 10.741083499365942, 106.70203763215794],
    [1870.61, 10.823955431371676, 106.69219393905452],
    [0.0, 10.836741476104356, 106.68341207235753],
    [1952.54, 10.833827624045112, 106.67059323605213],
    [1459.53, 10.926737581225254, 106.55686147657384],
    [971.34, 10.749504024802121, 106.65453533199823],
    [555.85, 10.959016288745774, 106.50469227862662],
    [127.82, 10.754712703279315, 106.63326099624115],
    [423.05, 10.694726756700211, 106.58839643199786],
    [207.8, 10.864422978832003, 106.58982153727769],
    [495.15, 10.769063188224223, 106.6530953335917],
    [699.5, 10.739350713879652, 106.62920119338125],
    [1666.56, 10.767611232403523, 106.68591328391079],
    [1852.01, 10.769049682361974, 106.66577650080094],
    [318.42, 10.753644717579572, 106.6133352973548],
    [1076.59, 10.827283008576414, 106.81193993662411],
    [715.75, 10.762954140781089, 106.65702261420729],
    [211.94, 10.756317534699074, 106.69231770751723],
    [592.54, 10.8053001493701, 106.67858331832046],
    [187.04, 10.755112433441516, 106.690042442933],
    [528.98, 10.685585396099569, 106.62249706823035],
    [1766.69, 10.796232738243804, 106.74053639547414],
    [725.13, 10.74838755597344, 106.70536196146102],
    [298.39, 10.824285079737, 106.68272749434792],
    [345.04, 10.834930016798408, 106.66219501977464],
    [203.5, 10.826086717333506, 106.8173342644842],
    [190.15, 10.868224893898695, 106.73579148784809],
    [1233.5, 10.736633059860063, 106.61394473840016],
    [486.95, 10.760277509184522, 106.66189973845366],
    [595.75, 10.744333365337354, 106.6550291679002],
    [521.67, 10.859054175855906, 106.77776523805082],
    [276.56, 10.801408751565196, 106.61857143060715],
    [784.52, 10.827939670249133, 106.72155997085434],
    [1215.65, 10.800965497496932, 106.65353682632195],
    [936.23, 10.749530100247858, 106.70849129687295],
    [1838.54, 10.754222040359897, 106.6516615480369],
    [1557.3, 10.785468096971915, 106.64193116565633],
    [298.39, 10.834527603648134, 106.66475695577076],
    [1471.09, 10.830911251743272, 106.61499504415322],
    [1411.83, 10.666857886706726, 106.72514616742377],
    [471.19, 10.75313395509537, 106.7007388263215],
    [203.5, 10.815241990112296, 106.67207382944194],
    [1076.59, 10.633211745181494, 106.76237678601967],
    [1459.53, 10.775691481392982, 106.63053733789408],
    [971.34, 10.787963341854569, 106.69955300059291],
    [555.85, 10.77059663982937, 106.66947987384219],
    [1233.5, 10.786610837486364, 106.64514608153063],
    [211.94, 10.800918007998886, 106.65822371666304],
    [423.05, 10.795012960576202, 106.72188184969707],
    [207.8, 10.733809335017282, 106.70672371042879],
    [486.95, 10.718509266117739, 106.74344459289748],
    [347.72, 10.82839675280384, 106.62040335765374],
    [962.42, 10.799110364054618, 106.68928577973072],
    [254.95, 10.841416660990014, 106.74553242680346],
    [820.09, 10.742851589208437, 106.61222465012885],
    [865.84, 10.697133834421798, 106.59701609367342],
    [1543.29, 10.889678105562988, 106.59629605320778],
    [371.41, 10.797771718316245, 106.65901639259019],
    [511.83, 10.733622324592591, 106.67453328509292],
    [328.09, 10.806044944318701, 106.6663870161133],
    [1172.93, 10.73155844576023, 106.60428459860847],
    [316.24, 10.786847420293347, 106.67529388446025],
    [204.96, 10.774696907976047, 106.6748114060552],
    [346.06, 10.770343333676342, 106.62922359949961],
    [685.35, 10.771840987231569, 106.67001309064219],
    [488.17, 10.76848878704559, 106.66801929683373],
    [325.36, 10.895459536628419, 106.62185634562174],
    [539.16, 10.754229328356239, 106.66689834765585],
    [345.04, 10.814001042568387, 106.6136347262402],
    [1870.61, 10.850868224726465, 106.66312291227648],
    [0.0, 10.822702385984531, 106.629427464492],
    [1952.54, 10.774997863354868, 106.63099530416778],
    [790.59, 10.768414647994026, 106.61687605079598],
    [190.15, 10.774460153621625, 106.65657468434846],
    [715.75, 10.793384404013407, 106.64185856693454],
    [127.82, 10.684085751188704, 106.55215376089205],
    [592.54, 10.797370644447689, 106.6203110869487],
    [495.15, 10.778490394254115, 106.66544494233557],
]
data2 = np.array(data1)[:, 1:3]
weight = np.array(data1)[:, 0].tolist()
data_Point = []
total_weight = []
arr_iter = []
arr_weight_iter = []
arr_history = []


def kmeans_with_repeats(data, weight, iter_):
    n_clusters = 10
    kmeans = KMeans(n_clusters=n_clusters, max_iter=100)
    kmeans.fit(data, sample_weight=weight)
    labels = kmeans.labels_
    set_ValueDataPoint(data, labels, n_clusters)
    weight_ = cal_WeightTrip(data2, data_Point)
    with open(f"text.txt", "a") as fout:
        fout.write("\nNumber Of Iterations:{}\n".format(str(iter_)))
        fout.write("Number Cluster:{}\n".format(str(n_clusters)))
        for i in range(kmeans.n_iter_):
            fout.write(f"\nIteration {i + 1}: \n{kmeans.cluster_centers_}\n")
        for i, value in enumerate(weight_):
            fout.write(f"\nTrip {i + 1}:{value}\n")
    arr_iter.extend([iter_])
    arr_weight_iter.extend([kmeans.cluster_centers_.copy()])
    arr_history.extend([kmeans.cluster_centers_.copy()])

    return weight_


# def show_Result():
#     plt.figure(figsize=(19, 12))
#     for i, items in enumerate(cluster):
#         start_time = time.time()
#         kmeans = KMeans(
#             n_clusters=cluster[i],
#             max_iter=num_Iterations[i],
#             random_state=state[i],
#         )
#         kmeans.fit(data)
#         kmeans_time = time.time() - start_time
#         silhouette_ScoreKmean = silhouette_score(
#             data, kmeans.labels_
#         )  # Silhouette Score
#         # Paint Chart
#         plt.subplot(len(self.num_Clutered), 2, i * 2 + 1)
#         plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap="viridis")
#         plt.scatter(
#             kmeans.cluster_centers_[:, 0],
#             kmeans.cluster_centers_[:, 1],
#             marker="x",
#             s=200,
#             linewidths=3,
#             color="r",
#         )
#         plt.title(
#             f"K-means: Clusters: {cluster[i]}, Iterations: {num_Iterations[i]},Time: {kmeans_time:.2f} seconds\nSilhouette Score:{silhouette_ScoreKmean:.2f},Inertia:{kmeans.inertia_:.2f}"
#         )
#     plt.tight_layout()
#     plt.show()


def set_ValueDataPoint(data, label, num):
    data_Point.clear()
    for i in range(num):
        cluster_points = data[label == i]
        data_Point.append(cluster_points)
    return data_Point


def cal_WeightTrip(data, point):
    data = np.array(data1).tolist()
    weight_kmean = []
    if len(weight_kmean) > 10:
        weight_kmean.clear()
    for items in point:
        temp = 0
        for value in items:
            lat = value[0]
            lon = value[1]
            for value_ in data:
                if lat == value_[1] and lon == value_[2]:
                    temp += value_[0]
        weight_kmean.append(temp)
    return weight_kmean


def reload_function(weight_kmean, data, data2, weight):
    data_Weight = []
    temp = 0
    weight_kmean_ = weight_kmean
    for value in weight_kmean_:
        if value < data:
            data_Weight.append(value)
        else:
            pass
    if (len(data_Weight) / len(weight_kmean)) * 100 >= 70:
        print("đủ điều kiện")
        pass
    else:
        while (len(data_Weight) / len(weight_kmean)) * 100 < 70:
            temp += 1
            kmeans_with_repeats(data2, weight, temp)
            print("chưa đủ điều kiện")
            if temp == 100:
                break
    return data_Weight


temp = 0
data_weight_test = kmeans_with_repeats(data2, weight, temp)
data_reload = reload_function(data_weight_test, data, data2, weight)
# show_Result()
# print("check value data history", arr_history, len(arr_history))
print("check vlaue data arr_history", arr_history, len(arr_history))
# print("check len(arr_History)", arr_history, len(arr_history))
# new_duplicate = []
# for items in arr_history:
#     for value in items:
#         lat = value[0]
#         lon = value[1]
#         if [lat, lon] not in new_duplicate:
#             new_duplicate.append([lat, lon])
# # if len(new_duplicate) > 5:
#     print("check value", value)
print("check len", len(new_duplicate))
print("chắc calue in kye", arr_history[0])
