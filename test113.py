# from sklearn.metrics.pairwise import haversine_distances
# from math import radians
# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler

# data = pd.read_csv("data.csv")

# scaler = StandardScaler()
# data[["payload"]] = scaler.fit_transform(data[["payload"]])
# data["lat_rad"] = data["lat"].apply(lambda x: radians(x))
# data["lon_rad"] = data["lon"].apply(lambda x: radians(x))
# coords = data[["lat_rad", "lon_rad"]]
# data["haversine"] = haversine_distances(coords, coords) * 6371000
# kmeans = KMeans(n_clusters=3)
# data["cluster"] = kmeans.fit_predict(data[["haversine"]])
# big_payload_clusters = data[data["payload"] > 100]

# small_clusters = (
#     big_payload_clusters.groupby("cluster").size().reset_index(name="count")
# )

# small_clusters["subcluster"] = range(1, len(small_clusters) + 1)
# big_payload_clusters = big_payload_clusters.merge(
#     small_clusters[["cluster", "subcluster"]], on="cluster", how="left"
# )

# big_payload_clusters["cluster"] = big_payload_clusters["subcluster"]
# big_payload_clusters = big_payload_clusters.drop("subcluster", axis=1)

# print(data)
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
    QVBoxLayout,
    QCheckBox,
)
from PyQt5.QtCore import Qt, pyqtSlot


class MyCheckBoxItem(QCheckBox):
    def __init__(self, checked=False):
        super().__init__()
        self.setChecked(checked)
        self.stateChanged.connect(self.check_all)

    def check_all(self, state):
        if state == Qt.Checked:
            for checkbox in checkboxes:
                if checkbox != self:
                    checkbox.setChecked(True)


class CheckBoxTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Checkbox in QTableWidget Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2"])

        self.set_all_checked = False  # Biến để kiểm tra

        global checkboxes  # Sử dụng danh sách để lưu trữ tất cả các checkbox

        checkboxes = []

        for row in range(3):
            item = QTableWidgetItem()
            self.tableWidget.setItem(row, 0, item)

        for row in range(3):
            item = QTableWidgetItem()
            self.tableWidget.setItem(row, 1, item)

        for row in range(3):
            checkbox = MyCheckBoxItem(checked=True if self.set_all_checked else False)
            checkboxes.append(checkbox)  # Thêm checkbox vào danh sách
            self.tableWidget.setCellWidget(row, 0, checkbox)

        for row in range(3):
            checkbox = MyCheckBoxItem(checked=True if self.set_all_checked else False)
            checkboxes.append(checkbox)  # Thêm checkbox vào danh sách
            self.tableWidget.setCellWidget(row, 1, checkbox)

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckBoxTableWidget()
    window.show()
    sys.exit(app.exec_())
