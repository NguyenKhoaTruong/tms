from sklearn.metrics.pairwise import haversine_distances
from math import radians
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("data.csv")

scaler = StandardScaler()
data[["payload"]] = scaler.fit_transform(data[["payload"]])
data["lat_rad"] = data["lat"].apply(lambda x: radians(x))
data["lon_rad"] = data["lon"].apply(lambda x: radians(x))
coords = data[["lat_rad", "lon_rad"]]
data["haversine"] = haversine_distances(coords, coords) * 6371000
kmeans = KMeans(n_clusters=3)
data["cluster"] = kmeans.fit_predict(data[["haversine"]])
big_payload_clusters = data[data["payload"] > 100]

small_clusters = (
    big_payload_clusters.groupby("cluster").size().reset_index(name="count")
)

small_clusters["subcluster"] = range(1, len(small_clusters) + 1)
big_payload_clusters = big_payload_clusters.merge(
    small_clusters[["cluster", "subcluster"]], on="cluster", how="left"
)

big_payload_clusters["cluster"] = big_payload_clusters["subcluster"]
big_payload_clusters = big_payload_clusters.drop("subcluster", axis=1)

print(data)
