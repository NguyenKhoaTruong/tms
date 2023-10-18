# # from decimal import Decimal
# # route=[[10.85040297, 106.7286891], [10.81879354, 106.6277875], [10.81879354, 106.6277875], [10.740346775668945, 106.66111865328268], [10.85040297, 106.7286891]]
# # data_Order=[[('MC210126000014', 'S1230700059', Decimal('1.00000'), Decimal('1.00000'), None, '10.79869129', '106.5848717', '229/35 LIEN KHU 4-5,P.BINH HUNG HOA\r\n B', 'BINH TAN', 'HCM')],
# #             [('YKKVN003594002', 'S1230700058', Decimal('1.00000'), Decimal('1.00000'), None, '10.83544663', '106.6344321', '21/6C PHAN HUY ICH, PHUONG 14, ', 'GO VAP', 'HO CHI MINH')],
# #             [('YKKVN003474000', 'S1230700028', Decimal('1.00000'), Decimal('1.00000'), None, '10.8179385', '106.6147104', 'LO III-3A, DUONG CN1, NHOM CN III, KCN TAN BINH, P.TAY THANH, ', 'TAN PHU', 'HO CHI MINH'),
# #              ('YKKVN003474000', 'S1230700057', Decimal('1.00000'), Decimal('1.00000'), None, '10.8179385', '106.6147104', 'LO III-3A, DUONG CN1, NHOM CN III, KCN TAN BINH, P.TAY THANH, ', 'TAN PHU', 'HO CHI MINH')],
# #             [('YKKVN002440036', 'S1230700056', Decimal('1.00000'), Decimal('1.00000'), None, '10.83970674', '106.6493478', '1B QUANG TRUNG,PHUONG 8,QUAN', 'GO VAP', 'HO CHI MINH')],
# #             [('YKKVN001676000', 'S1230700055', Decimal('1.00000'), Decimal('1.00000'), None, '10.86084919', '106.6889711', '1365/1 QUOC LO 1A, PHUONG AN PHU DONG, ', 'QUAN 12', 'HO CHI MINH')],
# #             [('YKKVN001566016', 'S1230700054', Decimal('1.00000'), Decimal('1.00000'), None, '10.85040297', '106.7286891', 'PHONG KINH DOANH-CTCP MAY SAI GON 3 40/32 QUOC LO 13, HIEP BINH PHUOC ', 'THU DUC', 'HO CHI MINH')],
# #             [('YKKVN001537000', 'S1230700027', Decimal('1.00000'), Decimal('1.00000'), None, '10.81879354', '106.6277875', '36 DUONG TAY THANH, PHUONG TAY THANH', 'TAN PHU', 'HO CHI MINH'),('YKKVN001537000', 'S1230700053', Decimal('1.00000'), Decimal('1.00000'), None, '10.81879354', '106.6277875', '36 DUONG TAY THANH, PHUONG TAY THANH', 'TAN PHU', 'HO CHI MINH')],
# #             [('MC191216000002', 'S1230700052', Decimal('1.00000'), Decimal('1.00000'), None, '10.7536879', '106.7406081', 'LO SO BF 21-23-25-27-29,DUONG TAN THUAN,KCX TAN THUAN,P.TAN THUAN DONG', 'QUAN 7', 'HO CHI MINH')],
# #             [('YKKVN004383002', 'S1230700051', Decimal('1.00000'), Decimal('1.00000'), None, '10.75591833', '106.7307766', 'DUONG LY THAI TO, TO 12, PHUONG YEN DO,', 'PLEIKU', 'GIA LAI')],
# #             [('YKKVN003965002', 'S1230700050', Decimal('1.00000'), Decimal('1.00000'), None, '10.74700592', '106.6253679', '241 DUONG 26,PHUONG BINH TRI DONG B  , ', 'BINH TAN', 'HO CHI MINH')],
# #             [('YKKVN003915000', 'S1230700049', Decimal('1.00000'), Decimal('1.00000'), None, '10.73665121', '106.6969019', 'LO NX-E1-E2, DUONG D1, KHU CONG NGHIEP LONG HAU, XA LONG HAU', 'CAN GIUOC', 'LONG AN')]]
# # # Lấy tọa độ lat và lon từ "route"
# # route_lat_lon = [point[:2] for point in route]
# # print('check value route lat lon',route_lat_lon)

# # # Lấy tọa độ lat và lon từ phần tử thứ nhất của "data_Order"
# # data_Order_lat_lon = [[float(order[0][5]), float(order[0][6])] for order in data_Order]
# # # Tạo một mảng mới chứa các giá trị order từ phần tử thứ nhất của "data_Order" dựa trên sự so sánh với "route"
# # new_array = []

# # for lat_lon in data_Order_lat_lon:
# #     if lat_lon in route_lat_lon:
# #         index = route_lat_lon.index(lat_lon)
# #         new_array.append(data_Order[index][0][1])

# # # In ra mảng mới
# # print('check new aray',new_array,len(new_array))

# # # data=[(10.85040297, 106.7286891), (10.81879354, 106.6277875), (10.81879354, 106.6277875), (10.740346775668945, 106.66111865328268)]
# # # data_=[]
# # # for value in data:
# # #     if value not in data_:
# # #         data_.append(value)
# # #         print('check value da',data_)
# # # print('check value data_',data_)
# # # for i in range(3):
# # #     print(i)

# # import googlemaps
# # from datetime import datetime

# # route_Point = [
# #     [10.662705470457466, 106.70724887936655],
# #     [10.74700592, 106.6253679],
# #     [10.74705863, 106.6254001],
# #     [10.75799883, 106.6517412],
# #     [10.74358153, 106.6604386],
# #     [10.74353937, 106.6604922],
# #     [10.73665121, 106.6969019],
# #     [10.662705470457466, 106.70724887936655],
# # ]
# # # time = [[datetime.time(0, 0), 10, 10, 10, 10]]

# # gmaps = googlemaps.Client(key="AIzaSyAXiMLkRaq16MeTMVOFnYWqxDd0TCV3prU")
# # origin = (route_Point[0][0], route_Point[0][1])
# # destination = (route_Point[-1][0], route_Point[-1][1])
# # for i in range(1, len(route_Point)):
# #     waypoint = (route_Point[i][0], route_Point[i][1])
# #     directions_result = gmaps.directions(
# #         origin,
# #         destination,
# #         waypoints=[waypoint],
# #         mode="driving",
# #         departure_time=datetime.now(),
# #     )
# #     if directions_result:
# #         start_location = directions_result[0]["legs"][0]["start_location"]
# #         end_location = directions_result[0]["legs"][0]["end_location"]
# #         duration = directions_result[0]["legs"][0]["duration"]["text"]
# #         origin = (end_location["lat"], end_location["lng"])
# #         print("check value data time", duration)
# #     else:
# #         print(f"Không tìm thấy thông tin từ điểm {i} đến điểm {i+1}.")

# # import geopy.distance
# # from datetime import datetime, timedelta


# # def calculate_eta_etd_with_fixed_times(
# #     points, time_Way_point, fixed_wait_time, fixed_send_time
# # ):
# #     eta_etd_list = []
# #     for i in range(1, len(points)):
# #         if i == 1:
# #             eta = datetime.now()
# #         else:
# #             print("check value data eta etd", eta_etd_list)
# #             eta = eta_etd_list[-1][1]
# #             print("xxxxx", eta)
# #         eta += timedelta(minutes=time_Way_point[i - 1])
# #         etd = (
# #             eta
# #             + timedelta(minutes=fixed_wait_time)
# #             + timedelta(minutes=fixed_send_time)
# #         )

# #         eta_etd_list.append((eta, etd))

# #     return eta_etd_list


# # point = [
# #     [10.662705470457466, 106.70724887936655],
# #     [10.75591833, 106.7307766],
# #     [10.7536879, 106.7406081],
# #     [10.81631072, 106.7760074],
# #     [10.82877023, 106.7304006],
# #     [10.85040297, 106.7286891],
# # ]

# # # time_Ship = [datetime.time(1, 0), 10, 10, 10, 10]
# # time_Way_point = [33, 5, 32, 21, 9]
# # fixed_wait_time = 10
# # fixed_send_time = 10

# # eta_etd_data = calculate_eta_etd_with_fixed_times(
# #     point, time_Way_point, fixed_wait_time, fixed_send_time
# # )
# # for i, value in enumerate(eta_etd_data):
# #     print(
# #         f"Segment {i + 1}: ETA - {value[0].strftime('%H:%M')}, ETD - {value[1].strftime('%H:%M')}"
# #     )
# # import sys
# # from PyQt5.QtWidgets import (
# #     QApplication,
# #     QWidget,
# #     QGridLayout,
# #     QVBoxLayout,
# #     QPushButton,
# #     QHBoxLayout,
# #     QTableWidget,
# # )

# # app = QApplication(sys.argv)
# # window = QWidget()
# # window.setWindowTitle("Example")
# # x = QHBoxLayout()
# # button11 = QPushButton("Button 11")
# # button11.setFixedWidth(5)
# # button11.setFixedHeight(5)
# # main_layout = QGridLayout()
# # vbox_container = QWidget()
# # # Tạo QVBoxLayout và thiết lập nó cho QWidget
# # vbox_layout = QVBoxLayout(vbox_container)
# # table_widget = QTableWidget(3, 3)
# # table_widget.setGeometry(100, 100, 500, 500)
# # # Thêm các phần tử vào QVBoxLayout
# # button1 = QPushButton("Button 1")
# # button11 = QPushButton("Button 11")
# # button2 = QPushButton("Button 2")
# # button12 = QPushButton("Button 12")
# # button3 = QPushButton("Button 3")
# # button13 = QPushButton("Button 13")

# # buttontest = QPushButton("Button test")

# # # vbox_layout.addWidget(table_widget)
# # vbox_layout.addWidget(button1)
# # vbox_layout.addWidget(button2)
# # vbox_layout.addWidget(button3)


# # main_layout.addWidget(table_widget, 0, 0)
# # main_layout.addWidget(vbox_container, 1, 0)
# # main_layout.addWidget(button11, 2, 0)
# # main_layout.addWidget(button12, 2, 1)

# # # Đặt layout chính cho cửa sổ
# # x.addWidget(button1)
# # x.addLayout(main_layout)
# # window.setLayout(x)

# # window.show()
# # sys.exit(app.exec_())
# # import sys
# # import numpy as np
# # from PyQt5.QtCore import Qt, QThread, pyqtSignal
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
# # from sklearn.cluster import KMeans


# # class KMeansThread(QThread):
# #     result_signal = pyqtSignal(np.ndarray)

# #     def __init__(self, data, num_clusters):
# #         super().__init__()
# #         self.data = data
# #         self.num_clusters = num_clusters

# #     def run(self):
# #         kmeans = KMeans(n_clusters=self.num_clusters)
# #         labels = kmeans.fit_predict(self.data)
# #         print("check type labels", type(labels))
# #         self.result_signal.emit(labels)


# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("K-Means Clustering")
# #         self.setGeometry(100, 100, 400, 200)

# #         layout = QVBoxLayout()

# #         self.cluster_button = QPushButton("Run K-Means")
# #         self.cluster_button.clicked.connect(self.start_kmeans)
# #         layout.addWidget(self.cluster_button)

# #         central_widget = QWidget()
# #         central_widget.setLayout(layout)
# #         self.setCentralWidget(central_widget)

# #     def start_kmeans(self):
# #         self.cluster_button.setEnabled(False)

# #         # Tạo dữ liệu ngẫu nhiên để minh họa
# #         data = np.random.rand(10000, 2)  # 100 điểm dữ liệu 2 chiều

# #         self.kmeans_thread = KMeansThread(data, num_clusters=3)
# #         self.kmeans_thread.result_signal.connect(self.update_result)
# #         self.kmeans_thread.start()

# #     def update_result(self, labels):
# #         # Cập nhật giao diện sau khi K-Means hoàn thành
# #         self.cluster_button.setEnabled(True)
# #         print("K-Means hoàn thành. Nhãn của các điểm dữ liệu:", labels)


# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())
# # Import các thư viện cần thiết
# # import sys
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox


# # class CheckBoxHeader(QCheckBox):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)


# # # Tạo lớp MainWindow
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Set Check True for All Checkboxes")
# #         self.setGeometry(100, 100, 400, 300)

# #         layout = QVBoxLayout()
# #         self.checkbox_list = []

# #         # Tạo danh sách các QCheckBox và thêm chúng vào danh sách checkbox_list
# #         for i in range(100):
# #             checkbox = QCheckBox(f"Checkbox {i + 1}")
# #             layout.addWidget(checkbox)
# #             self.checkbox_list.append(checkbox)

# #         # Tạo một nút để đặt tất cả các ô chọn thành True
# #         set_all_checked_button = QCheckBox("Set All Checked")
# #         set_all_checked_button.clicked.connect(self.set_all_checkboxes_checked)
# #         layout.addWidget(set_all_checked_button)

# #         central_widget = QWidget()
# #         central_widget.setLayout(layout)
# #         self.setCentralWidget(central_widget)

# #     def set_all_checkboxes_checked(self):
# #         # Đặt trạng thái "được chọn" cho tất cả các ô chọn trong danh sách
# #         for checkbox in self.checkbox_list:
# #             checkbox.setChecked(True)


# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())
# # from decimal import Decimal
# # import numpy as np
# # from sklearn.cluster import KMeans

# # data = [
# #     [Decimal("0.00000"), Decimal("0.00000"), 10.771135858264335, 106.69507196790613],
# #     [Decimal("1.00000"), Decimal("1.00000"), 11.03297581, 106.3542277],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.89934761, 106.413231],
# #     [Decimal("1.00000"), Decimal("1.00000"), 11.02517305, 106.3870693],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.95523884, 106.6061324],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.89015757, 106.6345503],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.8965339, 106.6406705],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.92449731, 106.5581646],
# #     [Decimal("1.00000"), Decimal("1.00000"), 11.00698019, 106.3945347],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.75799883, 106.6517412],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.6478613, 106.5443319],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.828227407730115, 106.7733690828174],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.827237159791236, 106.679470496312],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.811710745264808, 106.63303318975827],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.817867359243692, 106.61473196280781],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.952184023450435, 106.89048764418078],
# #     [Decimal("1.00000"), Decimal("1.00000"), 11.08452259156998, 107.17174401903856],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.972936342924847, 106.90877480185128],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.412331038586013, 107.19334947422125],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.7411685976066, 106.9311067916584],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.911455351812652, 106.8608174650592],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.910847184835376, 106.69956076807442],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.907563319424014, 106.71699805894866],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.911086195059935, 106.70034263189507],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.971847491113245, 106.7337902322077],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.896296714153396, 106.72605694602625],
# #     [Decimal("1.00000"), Decimal("1.00000"), 11.130025001767287, 106.60041292421302],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.919692700754005, 106.73034889412152],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.99520075891292, 106.70779289631317],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.946243697773696, 106.74889584074957],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.743486664230028, 106.660556613498],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.755351564939886, 106.72962652564206],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.751027390235278, 106.61127699631155],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.828195794307579, 106.7733690828174],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.62991908399019, 106.71692132514566],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.751035676989272, 106.61127196263875],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.755872771815007, 106.74292579631158],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.875662663730843, 106.73057725822333],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.860849185863177, 106.68894959631228],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.83968566264628, 106.64933706747692],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.835404478048432, 106.63442136747699],
# #     [Decimal("1.00000"), Decimal("1.00000"), 10.79873892744089, 106.58475073864138],
# # ]

# # k_initial = len(data) // 10
# # # Khởi tạo và fit mô hình K-means ban đầu
# # kmeans_initial = KMeans(n_clusters=k_initial)
# # kmeans_initial.fit(data)

# # # Nhãn của từng điểm dữ liệu
# # labels_initial = kmeans_initial.labels_
# # center_initial = kmeans_initial.cluster_centers_

# # initial_clusters = []
# # for i in range(k_initial):
# #     cluster_data = np.array(data)[labels_initial == i]
# #     initial_clusters.append(cluster_data)


# # updated_clusters = []
# # for cluster_data in initial_clusters:
# #     if len(cluster_data) > 25:
# #         # Tách cụm lớn thành các cụm nhỏ hơn
# #         k_subclusters = len(cluster_data) // 10
# #         kmeans_subcluster = KMeans(n_clusters=k_subclusters)
# #         kmeans_subcluster.fit(cluster_data)
# #         labels_subcluster = kmeans_subcluster.labels_

# #         # Tạo danh sách các cụm con
# #         subclusters = []
# #         for j in range(k_subclusters):
# #             subcluster_data = np.array(cluster_data)[labels_subcluster == j]
# #             subclusters.append(subcluster_data)

# #         updated_clusters.extend(subclusters)
# #     else:
# #         updated_clusters.append(cluster_data)
# # for value in subclusters:
# #     print("check value data value", value, len(value))
# # import numpy as np
# # from sklearn.cluster import KMeans
# # from scipy.spatial.distance import mahalanobis
# # from decimal import Decimal

# # # Tạo dữ liệu mẫu
# # data1 =SyntaxError('invalid syntax. Perhaps you forgot a comma?', ('<string>', 1, 17, "[array([Decimal('0.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), array([Decimal('1.00...pe=object), ...]", 1, 57))
# # data =  [[10.771135858264335, 106.69507196790613],
# #         [11.03297581, 106.3542277],
# #         [10.89934761, 106.413231],
# #         [11.02517305, 106.3870693],
# #         [10.95523884, 106.6061324],
# #         [10.89015757, 106.6345503],
# #         [10.8965339, 106.6406705],
# #         [10.92449731, 106.5581646],
# #         [11.00698019, 106.3945347],
# #         [10.75799883, 106.6517412],
# #         [10.6478613, 106.5443319],
# #         [10.828227407730115, 106.7733690828174],
# #         [10.827237159791236, 106.679470496312],
# #         [10.811710745264808, 106.63303318975827],
# #         [10.817867359243692, 106.61473196280781],
# #         [10.952184023450435, 106.89048764418078],
# #         [11.08452259156998, 107.17174401903856],
# #         [10.972936342924847, 106.90877480185128],
# #         [10.412331038586013, 107.19334947422125],
# #         [10.7411685976066, 106.9311067916584],
# #         [10.911455351812652, 106.8608174650592],
# #         [10.910847184835376, 106.69956076807442],
# #         [10.907563319424014, 106.71699805894866],
# #         [10.911086195059935, 106.70034263189507],
# #         [10.971847491113245, 106.7337902322077],
# #         [10.896296714153396, 106.72605694602625],
# #         [11.130025001767287, 106.60041292421302],
# #         [10.919692700754005, 106.73034889412152],
# #         [10.99520075891292, 106.70779289631317],
# #         [10.946243697773696, 106.74889584074957],
# #         [10.743486664230028, 106.660556613498],
# #         [10.755351564939886, 106.72962652564206],
# #         [10.751027390235278, 106.61127699631155],
# #         [10.828195794307579, 106.7733690828174],
# #         [10.62991908399019, 106.71692132514566],
# #         [10.751035676989272, 106.61127196263875],
# #         [10.755872771815007, 106.74292579631158],
# #         [10.875662663730843, 106.73057725822333],
# #         [10.860849185863177, 106.68894959631228],
# #         [10.83968566264628, 106.64933706747692],
# #         [10.835404478048432, 106.63442136747699],
# #         [10.79873892744089, 106.58475073864138]]
# # print(data)
# # NameError("name 'array' is not defined")
# # data = [[2, 3], [3, 2], [3, 1]]

# # # Tính độ dài của danh sách ban đầu

# # split_index1 = len(data) // 3
# # split_index2 = 2 * split_index1

# # part1 = data[:split_index1]
# # part2 = data[split_index1:split_index2]
# # part3 = data[split_index2:]

# # # In kết quả
# # print("Phần 1:", part1)
# # print("Phần 2:", part2)
# # print("Phần 3:", part3)

# # data = []

# # data1 = [[1], [2]]
# # data = data1

# # print("check value data", data)


# # Danh sách các điểm với tọa độ latitude (lat) và longitude (lon)

# # import networkx as nx

# # from scipy.spatial import distance
# # import itertools

# # Danh sách các điểm dữ liệu với tọa độ lat-lon

# # import networkx as nx
# # from scipy.spatial import distance
# # import itertools

# # # Danh sách các điểm dữ liệu với tọa độ lat-lon
# # start_Point = [10.212211080689428, 105.88644918781283]
# # points = [
# #     [10.771135858264335, 106.69507196790613],
# #     [11.03297581, 106.3542277],
# #     [10.89934761, 106.413231],
# #     [11.02517305, 106.3870693],
# #     [10.95523884, 106.6061324],
# #     [10.89015757, 106.6345503],
# #     [10.8965339, 106.6406705],
# #     [10.92449731, 106.5581646],
# #     [11.00698019, 106.3945347],
# #     [10.75799883, 106.6517412],
# #     [10.6478613, 106.5443319],
# #     [10.828227407730115, 106.7733690828174],
# #     [10.827237159791236, 106.679470496312],
# #     [10.811710745264808, 106.63303318975827],
# #     [10.817867359243692, 106.61473196280781],
# #     [10.952184023450435, 106.89048764418078],
# #     [11.08452259156998, 107.17174401903856],
# #     [10.972936342924847, 106.90877480185128],
# #     [10.412331038586013, 107.19334947422125],
# #     [10.7411685976066, 106.9311067916584],
# #     [10.911455351812652, 106.8608174650592],
# #     [10.910847184835376, 106.69956076807442],
# #     [10.907563319424014, 106.71699805894866],
# #     [10.911086195059935, 106.70034263189507],
# #     [10.971847491113245, 106.7337902322077],
# #     [10.896296714153396, 106.72605694602625],
# #     [11.130025001767287, 106.60041292421302],
# #     [10.919692700754005, 106.73034889412152],
# #     [10.99520075891292, 106.70779289631317],
# #     [10.946243697773696, 106.74889584074957],
# #     [10.743486664230028, 106.660556613498],
# #     [10.755351564939886, 106.72962652564206],
# #     [10.751027390235278, 106.61127699631155],
# #     [10.828195794307579, 106.7733690828174],
# #     [10.62991908399019, 106.71692132514566],
# #     [10.751035676989272, 106.61127196263875],
# #     [10.755872771815007, 106.74292579631158],
# #     [10.875662663730843, 106.73057725822333],
# #     [10.860849185863177, 106.68894959631228],
# #     [10.83968566264628, 106.64933706747692],
# #     [10.835404478048432, 106.63442136747699],
# #     [10.79873892744089, 106.58475073864138],
# # ]
# # points.insert(0, start_Point)
# # # Số lượng điểm dữ liệu
# # n = len(points)

# # # Tạo một đồ thị hoàn chỉnh với n điểm
# # G = nx.complete_graph(n)

# # # Tính toán khoảng cách giữa các điểm và lưu vào ma trận khoảng cách
# # dist_matrix = distance.cdist(points, points, "euclidean")

# # # Áp dụng thuật toán Christofides để giải bài toán người đi du lịch
# # tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True)

# # # Tính toán chi phí của lời giải
# # total_distance = sum(dist_matrix[i][j] for i, j in zip(tsp_tour, tsp_tour[1:]))

# # print(f"Lời giải TSP: {tsp_tour}")
# # print(f"Chi phí TSP: {total_distance}")
# # import pulp
# # from geopy.distance import great_circle

# # # Danh sách các điểm dữ liệu với tọa độ lat-lon
# # points = [
# #     [10.771135858264335, 106.69507196790613],
# #     [11.03297581, 106.3542277],
# #     [10.89934761, 106.413231],
# #     [11.02517305, 106.3870693],
# #     [10.95523884, 106.6061324],
# #     [10.89015757, 106.6345503],
# #     [10.8965339, 106.6406705],
# #     [10.92449731, 106.5581646],
# #     [11.00698019, 106.3945347],
# #     [10.75799883, 106.6517412],
# #     [10.6478613, 106.5443319],
# #     [10.828227407730115, 106.7733690828174],
# #     [10.827237159791236, 106.679470496312],
# #     [10.811710745264808, 106.63303318975827],
# #     [10.817867359243692, 106.61473196280781],
# #     [10.952184023450435, 106.89048764418078],
# #     [11.08452259156998, 107.17174401903856],
# #     [10.972936342924847, 106.90877480185128],
# #     [10.412331038586013, 107.19334947422125],
# #     [10.7411685976066, 106.9311067916584],
# #     [10.911455351812652, 106.8608174650592],
# #     [10.910847184835376, 106.69956076807442],
# #     [10.907563319424014, 106.71699805894866],
# #     [10.911086195059935, 106.70034263189507],
# #     [10.971847491113245, 106.7337902322077],
# #     [10.896296714153396, 106.72605694602625],
# #     [11.130025001767287, 106.60041292421302],
# #     [10.919692700754005, 106.73034889412152],
# #     [10.99520075891292, 106.70779289631317],
# #     [10.946243697773696, 106.74889584074957],
# #     [10.743486664230028, 106.660556613498],
# #     [10.755351564939886, 106.72962652564206],
# #     [10.751027390235278, 106.61127699631155],
# #     [10.828195794307579, 106.7733690828174],
# #     [10.62991908399019, 106.71692132514566],
# #     [10.751035676989272, 106.61127196263875],
# #     [10.755872771815007, 106.74292579631158],
# #     [10.875662663730843, 106.73057725822333],
# #     [10.860849185863177, 106.68894959631228],
# #     [10.83968566264628, 106.64933706747692],
# #     [10.835404478048432, 106.63442136747699],
# #     [10.79873892744089, 106.58475073864138],
# # ]


# # # Danh sách các điểm với tọa độ latitude (lat) và longitude (lon)

# # # Số lượng điểm
# # num_points = len(points)

# # # Tạo mô hình ILP
# # tsp_model = pulp.LpProblem("TSP", pulp.LpMinimize)

# # # Tạo các biến nguyên 0-1 để biểu diễn các cạnh
# # x = {}
# # for i in range(num_points):
# #     for j in range(num_points):
# #         if i != j:
# #             x[i, j] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# # # Hàm mục tiêu: Tối thiểu hóa tổng khoảng cách
# # tsp_model += pulp.lpSum(x[i, j] * great_circle(points[i], points[j]).kilometers
# #                         for i in range(num_points) for j in range(num_points) if i != j)

# # # Ràng buộc:
# # # Mỗi thành phố phải được thăm đúng một lần
# # for i in range(num_points):
# #     tsp_model += pulp.lpSum(x[i, j] for j in range(num_points) if i != j) == 1

# # # Mỗi thành phố chỉ có thể rời khỏi một lần
# # for j in range(num_points):
# #     tsp_model += pulp.lpSum(x[i, j] for i in range(num_points) if i != j) == 1

# # # Giải quyết bài toán
# # tsp_model.solve()

# # # Lấy hành trình tối ưu
# # optimal_path = [i for i in range(num_points) if x[i, (i + 1) % num_points].varValue == 1]

# # # Tạo hành trình đầy đủ bằng cách thêm điểm chưa được sử dụng
# # full_path = []
# # current_point = optimal_path[0]
# # while len(full_path) < num_points:
# #     full_path.append(current_point)
# #     for i in range(num_points):
# #         if i != current_point and x[current_point, i].varValue == 1:
# #             current_point = i
# #             break

# # # In ra hành trình đầy đủ và tổng khoảng cách
# # print("Hành trình đầy đủ:")
# # for i in range(len(full_path)):
# #     print(f"{points[full_path[i]]} ->", end=" ")
# # print(points[full_path[0]])  # Quay lại điểm xuất phát
# # total_distance = sum(great_circle(points[full_path[i]], points[full_path[(i + 1) % num_points]]).kilometers
# #                     for i in range(num_points))
# # print("Tổng khoảng cách đầy đủ:", total_distance, "kilometers")
# # import googlemaps

# # # Khởi tạo Google Maps API Client với API key của bạn
# # gmaps = googlemaps.Client(key="AIzaSyAXiMLkRaq16MeTMVOFnYWqxDd0TCV3prU")

# # # Danh sách 50 điểm dữ liệu của bạn (ví dụ: tọa độ lat/lng)
# # data_points = [
# #     [10.771135858264335, 106.69507196790613],
# #     [11.03297581, 106.3542277],
# #     [10.89934761, 106.413231],
# #     [11.02517305, 106.3870693],
# #     [10.95523884, 106.6061324],
# #     [10.89015757, 106.6345503],
# #     [10.8965339, 106.6406705],
# #     [10.92449731, 106.5581646],
# #     [11.00698019, 106.3945347],
# #     [10.75799883, 106.6517412],
# #     [10.6478613, 106.5443319],
# #     [10.828227407730115, 106.7733690828174],
# #     [10.827237159791236, 106.679470496312],
# #     [10.811710745264808, 106.63303318975827],
# #     [10.817867359243692, 106.61473196280781],
# #     [10.952184023450435, 106.89048764418078],
# #     [11.08452259156998, 107.17174401903856],
# #     [10.972936342924847, 106.90877480185128],
# #     [10.412331038586013, 107.19334947422125],
# #     [10.7411685976066, 106.9311067916584],
# #     [10.911455351812652, 106.8608174650592],
# #     [10.910847184835376, 106.69956076807442],
# #     [10.907563319424014, 106.71699805894866],
# #     [10.911086195059935, 106.70034263189507],
# #     [10.971847491113245, 106.7337902322077],
# #     [10.896296714153396, 106.72605694602625],
# #     [11.130025001767287, 106.60041292421302],
# #     [10.919692700754005, 106.73034889412152],
# #     [10.99520075891292, 106.70779289631317],
# #     [10.946243697773696, 106.74889584074957],
# #     [10.743486664230028, 106.660556613498],
# #     [10.755351564939886, 106.72962652564206],
# #     [10.751027390235278, 106.61127699631155],
# #     [10.828195794307579, 106.7733690828174],
# #     [10.62991908399019, 106.71692132514566],
# #     [10.751035676989272, 106.61127196263875],
# #     [10.755872771815007, 106.74292579631158],
# #     [10.875662663730843, 106.73057725822333],
# #     [10.860849185863177, 106.68894959631228],
# #     [10.83968566264628, 106.64933706747692],
# #     [10.835404478048432, 106.63442136747699],
# #     [10.79873892744089, 106.58475073864138],
# # ]

# # grouped_data = [data_points[i : i + 25] for i in range(0, len(data_points), 25)]

# # # Tạo một biến để lưu tổng khoảng cách và thời gian
# # total_distance = 0
# # total_duration = 0

# # # Lặp qua từng nhóm và thực hiện lượt gọi API Directions
# # for group in grouped_data:
# #     # Tạo danh sách các điểm xuất phát và đích
# #     origins = group
# #     destinations = group

# #     # Gọi API Directions
# #     try:
# #         directions_result = gmaps.distance_matrix(origins, destinations, mode="driving")

# #         # Trích xuất thông tin khoảng cách và thời gian từ kết quả
# #         for row in directions_result["rows"]:
# #             for element in row["elements"]:
# #                 total_distance += element["distance"]["value"]
# #                 total_duration += element["duration"]["value"]
# #     except googlemaps.exceptions.ApiError as e:
# #         print("Lỗi khi gọi API Directions:", e)

# # # Chuyển đổi khoảng cách và thời gian sang đơn vị phù hợp (ví dụ: mét và giây)
# # total_distance_km = total_distance / 1000
# # total_duration_hours = total_duration / 3600

# # print("Tổng khoảng cách:", total_distance_km, "km")
# # print("Tổng thời gian:", total_duration_hours, "giờ")
# # import requests

# # # Khai báo API Key của bạn
# # api_key = "AIzaSyAXiMLkRaq16MeTMVOFnYWqxDd0TCV3prU"

# # # Tạo danh sách chứa 50 điểm
# # points = [
# #     {"lat": 10.662705470457466, "lng": 106.70724887936655},
# #     {"lat": 11.03297581, "lng": 106.3542277},
# #     {"lat": 10.919692700754005, "lng": 106.73034889412152},
# #     {"lat": 10.83968566264628, "lng": 106.64933706747692},
# #     {"lat": 10.78085784198798, "lng": 106.63160549815758},
# #     {"lat": 13.987031486263923, "lng": 107.99237541447324},
# #     {"lat": 20.423718223531758, "lng": 106.15880282612936},
# #     {"lat": 15.858457723278487, "lng": 108.38838887981179},
# #     {"lat": 20.851344033982606, "lng": 104.70464633175901},
# #     {"lat": 10.911455351812652, "lng": 106.8608174650592},
# #     {"lat": 10.95523884, "lng": 106.6061324},
# #     {"lat": 11.02517305, "lng": 106.3870693},
# #     {"lat": 10.6478613, "lng": 106.5443319},
# #     {"lat": 10.860849185863177, "lng": 106.68894959631228},
# #     {"lat": 10.755872771815007, "lng": 106.74292579631158},
# #     {"lat": 10.99520075891292, "lng": 106.70779289631317},
# #     {"lat": 10.971847491113245, "lng": 106.7337902322077},
# #     {"lat": 10.751035676989272, "lng": 106.61127196263875},
# #     {"lat": 10.896296714153396, "lng": 106.72605694602625},
# #     {"lat": 20.4471621, "lng": 106.3271365},
# #     {"lat": 10.835404478048432, "lng": 106.63442136747699},
# #     {"lat": 10.8965339, "lng": 106.6406705},
# #     {"lat": 10.828227407730115, "lng": 106.7733690828174},
# #     {"lat": 10.77113588566068, "lng": 106.69506125398182},
# #     {"lat": 10.910847184835376, "lng": 106.69956076807442},
# #     {"lat": 20.916538519892267, "lng": 106.10661156142478},
# #     {"lat": 11.08452259156998, "lng": 107.17174401903856},
# #     {"lat": 11.00698019, "lng": 106.3945347},
# #     {"lat": 10.89015757, "lng": 106.6345503},
# #     {"lat": 10.743486664230028, "lng": 106.660556613498},
# #     {"lat": 20.4414449, "lng": 106.1574427},
# #     {"lat": 10.946243697773696, "lng": 106.74889584074957},
# #     {"lat": 10.92449731, "lng": 106.5581646},
# #     {"lat": 10.827237159791236, "lng": 106.679470496312},
# #     {"lat": 10.412331038586013, "lng": 107.19334947422125},
# #     {"lat": 10.907563319424014, "lng": 106.71699805894866},
# #     {"lat": 10.817867359243692, "lng": 106.61473196280781},
# #     {"lat": 10.771135858264335, "lng": 106.69507196790613},
# #     {"lat": 10.75799883, "lng": 106.6517412},
# #     {"lat": 10.911086195059935, "lng": 106.70034263189507},
# #     {"lat": 10.755351564939886, "lng": 106.72962652564206},
# #     {"lat": 10.89934761, "lng": 106.413231},
# #     {"lat": 10.62991908399019, "lng": 106.71692132514566},
# #     {"lat": 11.130025001767287, "lng": 106.60041292421302},
# #     {"lat": 10.811710745264808, "lng": 106.63303318975827},
# #     {"lat": 10.875662663730843, "lng": 106.73057725822333},
# #     {"lat": 10.972936342924847, "lng": 106.90877480185128},
# #     {"lat": 10.952184023450435, "lng": 106.89048764418078},
# #     {"lat": 10.79873892744089, "lng": 106.58475073864138},
# #     {"lat": 10.751027390235278, "lng": 106.61127699631155},
# #     {"lat": 10.745645409601028, "lng": 106.73286228068469},
# #     {"lat": 10.7411685976066, "lng": 106.9311067916584},
# #     {"lat": 10.828195794307579, "lng": 106.7733690828174},
# #     {"lat": 10.819410113629296, "lng": 106.70194892514708},
# # ]


# # total_distance = 0
# # total_duration = 0

# # # Lặp qua từng cặp điểm
# # for i in range(len(points) - 1):
# #     start_point = f"{points[i]['lat']},{points[i]['lng']}"
# #     end_point = f"{points[i + 1]['lat']},{points[i + 1]['lng']}"

# #     # Gọi Google Maps Directions API để tính toán khoảng cách và thời gian với chế độ 'driving'
# #     url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_point}&destination={end_point}&mode=driving&key={api_key}"
# #     response = requests.get(url)
# #     data = response.json()

# #     if data["status"] == "OK":
# #         route = data["routes"][0]
# #         distance = route["legs"][0]["distance"]["value"]  # Khoảng cách (mét)
# #         duration = route["legs"][0]["duration"]["value"]  # Thời gian (giây)
# #         total_distance += distance
# #         total_duration += duration

# #         test_distance = distance = route["legs"][0]["distance"]["text"]
# #         test_duration = route["legs"][0]["duration"]["text"]
# #         print(f"Khoảng cách từ Điểm {i + 1} đến Điểm {i + 2}: {test_distance}")
# #         print(f"Thời gian từ Điểm {i + 1} đến Điểm {i + 2}: {test_duration}")

# # # Chuyển đổi tổng khoảng cách và tổng thời gian thành đơn vị đo lường phù hợp
# # total_distance_km = total_distance / 1000  # Khoảng cách tính bằng kilômét
# # total_duration_hours = total_duration / 3600  # Thời gian tính bằng giờ

# # print(f"Tổng khoảng cách: {total_distance_km} km", round(total_distance_km, 3))
# # print(f"Tổng thời gian: {total_duration_hours} giờ", round(total_duration_hours, 3))
# # import sys
# # from PyQt5 import QtCore, QtGui, QtWidgets
# # from PyQt5.QtGui import QMovie
# # from PyQt5.QtCore import Qt


# # class LoadingGif(object):
# #     def mainUI(self, FrontWindow):
# #         FrontWindow.setObjectName("FTwindow")
# #         FrontWindow.resize(250, 250)
# #         self.centralwidget = QtWidgets.QWidget(FrontWindow)
# #         self.centralwidget.setObjectName("main-widget")

# #         # Label Create
# #         self.label = QtWidgets.QLabel(self.centralwidget)
# #         self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
# #         self.label.setMinimumSize(QtCore.QSize(200, 200))
# #         self.label.setMaximumSize(QtCore.QSize(200, 200))
# #         self.label.setObjectName("lb1")
# #         FrontWindow.setCentralWidget(self.centralwidget)
# #         # Loading the GIF
# #         self.movie = QMovie("loader.gif")
# #         self.label.setMovie(self.movie)
# #         self.startAnimation()

# #     # Start Animation

# #     def startAnimation(self):
# #         self.movie.start()

# #     # Stop Animation(According to need)
# #     def stopAnimation(self):
# #         self.movie.stop()


# # app = QtWidgets.QApplication(sys.argv)
# # window = QtWidgets.QMainWindow()
# # demo = LoadingGif()
# # demo.mainUI(window)
# # window.show()
# # sys.exit(app.exec_())
# # import sys
# # from PyQt5.QtWidgets import (
# #     QApplication,
# #     QWidget,
# #     QHBoxLayout,
# #     QPushButton,
# #     QSpacerItem,
# #     QSizePolicy,
# # )

# # app = QApplication(sys.argv)
# # window = QWidget()
# # window.setWindowTitle("Khoảng cách giữa các phần tử trong QHBoxLayout")

# # layout = QHBoxLayout()

# # button1 = QPushButton("Button 1")
# # layout.addWidget(button1)

# # # Thêm một QSpacerItem với khoảng cách ngang
# # spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
# # layout.addItem(spacer)

# # button2 = QPushButton("Button 2")
# # layout.addWidget(button2)

# # window.setLayout(layout)
# # window.show()

# # sys.exit(app.exec_())
# from decimal import Decimal

# data = [
#     [10.707197855355952, 106.93615121102836],
#     [10.737672991050914, 106.72544499631141],
#     [10.70215679449556, 106.60922571997646],
#     [10.801358803201547, 106.6535789953199],
#     [10.772474411206565, 106.69799557054573],
#     [10.737100592321609, 106.72539996435638],
#     [10.825914779055791, 106.68012890426232],
#     [10.769570719747994, 106.69274918987253],
# ]
# matrix = [
#     [
#         "",
#         "",
#         "",
#         "",
#         "",
#         10.707197855355952,
#         106.93615121102836,
#         "None",
#         "Nhơn Trạch District",
#         "Dong Nai",
#     ],
#     [
#         "MC220509000004",
#         "S1230700002",
#         Decimal("0.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.771135858264335,
#         106.69507196790613,
#         "Tổ 7,KV5,Phường An Phú ,Bình Định",
#         "",
#         "",
#     ],
#     [
#         "MC2204030071",
#         "S1230700003",
#         Decimal("0.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         20.4471621,
#         106.3271365,
#         "Khu A, Khu Công nghiệp Nguyễn Đức Cảnh, phường Tiền Phong, thành phố Thái Bình, ",
#         "",
#         "",
#     ],
#     [
#         "MC220426000001",
#         "S1230700004",
#         Decimal("0.00000"),
#         Decimal("0.00000"),
#         "1T",
#         20.851344033982606,
#         104.70464633175901,
#         "Tiểu khu cấp 3, thị trấn Nông trường Mộc Châu",
#         "Mộc Châu",
#         "Sơn La",
#     ],
#     [
#         "MC2204030078",
#         "S1230700006",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         "1T5",
#         20.423718223531758,
#         106.15880282612936,
#         "Số 443, đường Giải Phóng, thành phố Nam Định, tỉnh Nam Định",
#         None,
#         None,
#     ],
#     [
#         "MC2204030077",
#         "S1230700007",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         "1T",
#         20.916538519892267,
#         106.10661156142478,
#         "Xã Bạch Sam, huyện Mỹ Hào, tỉnh Hưng Yên",
#         None,
#         None,
#     ],
#     [
#         "MC220510000001",
#         "S1230700008",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         "1T3",
#         15.858457723278487,
#         108.38838887981179,
#         "THÔN THUẬN AN,XÃ DUY XUYÊN",
#         "QUẢNG NAM",
#         "",
#     ],
#     [
#         "YKKVN002244006",
#         "S1230700015",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         11.03297581,
#         106.3542277,
#         "ROAD 4-LINH TRUNG EPZ&IP III",
#         "TRANG BANG",
#         "TAY NINH",
#     ],
#     [
#         "YKKVN003146000",
#         "S1230700016",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.89934761,
#         106.413231,
#         "AP CHANH, DUC HOA HA",
#         "DUC HOA",
#         "LONG AN",
#     ],
#     [
#         "YKKVN003431000",
#         "S1230700017",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         11.02517305,
#         106.3870693,
#         "DUONG 13,KCN TRANG BANG,XA AN TINH, ",
#         "TRANG BANG",
#         "TAY NINH",
#     ],
#     [
#         "YKKVN003801000",
#         "S1230700018",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.95523884,
#         106.6061324,
#         "AP 12, XA TAN THANH DONG, ",
#         "CU CHI",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN004109000",
#         "S1230700019",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.89015757,
#         106.6345503,
#         "LO C CUM CONG NGHIEP G TRUNG, KHU PHO 5, P.HIEP THANH",
#         "QUAN 12",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN004389000",
#         "S1230700020",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.8965339,
#         106.6406705,
#         "221/63 DUONG DT 4, AP 5, XA DONG THANH",
#         "HOC MON",
#         "HO CHI MINH",
#     ],
#     [
#         "MC210329000002",
#         "S1230700021",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.92449731,
#         106.5581646,
#         "CTY MAY MAC VIGAWELL - 11 QUOC LO\r\n 22,AP TRAM BOM,TAN PHU TRUNG,",
#         "CU CHI\r\n",
#         "HCM",
#     ],
#     [
#         "YKKVN02789A003",
#         "S1230700022",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         11.00698019,
#         106.3945347,
#         "LOT 28,RD NO.7,TRANG BANG IP, AN TINH VILLAGE",
#         "TRANG BANG",
#         "TAY NINH",
#     ],
#     [
#         "YKKVN001536000",
#         "S1230700023",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.75799883,
#         106.6517412,
#         "100/11-12 DUONG AN DUONG VUONG, P.9 ",
#         "QUAN 5",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN004395002",
#         "S1230700024",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.6478613,
#         106.5443319,
#         "58A,QUOC LO 1A,XA MY YEN",
#         "BEN LUC",
#         "LONG AN",
#     ],
#     [
#         "MC220425000020",
#         "S1230700025",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.828227407730115,
#         106.7733690828174,
#         "18 TANG NHON PHU, P.PHUOC LONG B,",
#         "QUAN 9, TP.HO CHI MINH",
#         "",
#     ],
#     [
#         "YKKVN001513000",
#         "S1230700026",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.827237159791236,
#         106.679470496312,
#         "03 NGUYEN OANH, PHUONG 10, ",
#         "GO VAP",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001537000",
#         "S1230700027",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.811710745264808,
#         106.63303318975827,
#         "36 DUONG TAY THANH, PHUONG TAY THANH",
#         "TAN PHU",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN003474000",
#         "S1230700028",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.817867359243692,
#         106.61473196280781,
#         "LO III-3A, DUONG CN1, NHOM CN III, KCN TAN BINH, P.TAY THANH, ",
#         "TAN PHU",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001741000",
#         "S1230700029",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.952184023450435,
#         106.89048764418078,
#         "LO 247, DUONG SO 12, KCN AMATA, PHUONG LONG BINH",
#         "BIEN HOA",
#         "DONG NAI",
#     ],
#     [
#         "YKKVN001741003",
#         "S1230700030",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         11.08452259156998,
#         107.17174401903856,
#         "LO SO B1,CUM CONG NGHIEP PHU CUONG, AP PHU DONG,XA PHU CUONG,",
#         "DINH QUAN",
#         "DONG NAI",
#     ],
#     [
#         "YKKVN001741007",
#         "S1230700031",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.972936342924847,
#         106.90877480185128,
#         "KHU PHO 4, THI TRAN",
#         "TRANG BOM",
#         "DONG NAI",
#     ],
#     [
#         "YKKVN003309002",
#         "S1230700032",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.412331038586013,
#         107.19334947422125,
#         "DNTN KHANH VAN - B10 TO 3 PHUOC BINH, PHUOC TINH,",
#         "LONG DIEN",
#         "BA RIA-VUNG TAU",
#     ],
#     [
#         "MC190920000001",
#         "S1230700033",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.7411685976066,
#         106.9311067916584,
#         "DUONG SO 10, KCN NHONTRACH 1",
#         "NHONTRACH",
#         "DONG NAI",
#     ],
#     [
#         "MC220419000006",
#         "S1230700034",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.911455351812652,
#         106.8608174650592,
#         "SO 7,DUONG 19A,KCN BIEN HOA 2",
#         "PHUONG AN BINH",
#         "THANH PHO BIEN HOA",
#     ],
#     [
#         "YKKVN001913000",
#         "S1230700035",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.910847184835376,
#         106.69956076807442,
#         "SO 7/128, KHU PHO BINH DUC 1, PHUONG BINH HOA, ",
#         "THUAN AN",
#         "BINH DUONG",
#     ],
#     [
#         "YKKVN001913003",
#         "S1230700036",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.907563319424014,
#         106.71699805894866,
#         "THUAN AN DISTRICT",
#         "THUAN AN",
#         "BINH DUONG",
#     ],
#     [
#         "YKKVN001913006",
#         "S1230700037",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.911086195059935,
#         106.70034263189507,
#         "SO 7/128, KHU PHO BINH DUC 1, PHUONG BINH HOA, ",
#         "THUAN AN",
#         "BINH DUONG",
#     ],
#     [
#         "YKKVN004060000",
#         "S1230700038",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.971847491113245,
#         106.7337902322077,
#         "KHU PHO BINH PHU, PHUONG BINH CHUAN ",
#         "THUAN AN",
#         "BINH DUONG",
#     ],
#     [
#         "MC200602000007",
#         "S1230700039",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.896296714153396,
#         106.72605694602625,
#         "LO C,DUONG SO 3,KCN DONG AN P.BINH HOA",
#         "TP.THUAN AN",
#         "BINH DUONG",
#     ],
#     [
#         "YKKVN004535000",
#         "S1230700040",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         11.130025001767287,
#         106.60041292421302,
#         "LO F-3-CN, DUONG D1, KCN MY PHUOC, PHUONG MY PHUOC, ",
#         "BEN CAT",
#         "BINH DUONG",
#     ],
#     [
#         "YKKVN004599002",
#         "S1230700041",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.919692700754005,
#         106.73034889412152,
#         "2/434 KHU PHO BINH DANG,PHUONG BINH HOA",
#         "THUAN AN",
#         "BINH DUONG",
#     ],
#     [
#         "MC190813000002",
#         "S1230700042",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.99520075891292,
#         106.70779289631317,
#         "SO 9/3, KHU PHO BINH HOA 1, PHUONG TAN PHUOC KHANH",
#         "TAN UYEN",
#         "BINH DUONG",
#     ],
#     [
#         "MC200508000001",
#         "S1230700043",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.946243697773696,
#         106.74889584074957,
#         "THUA DAT SO 1434,TO BAN DO SO 11, TAN PHUOC,PHUONG TAN BINH",
#         "THANH PHO DI AN",
#         "BINH DUONG",
#     ],
#     [
#         "YKKVN001790002",
#         "S1230700045",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.743486664230028,
#         106.660556613498,
#         "636-638 NGUYEN DUY, PHUONG 12, ",
#         "QUAN 10",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001832000",
#         "S1230700046",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.755351564939886,
#         106.72962652564206,
#         "04 DUONG BEN NGHE,PHUONG TAN THUAN DONG,",
#         "QUAN 7",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN002019006",
#         "S1230700047",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.751027390235278,
#         106.61127699631155,
#         "241 DUONG 26,PHUONG BINH TRI DONG B",
#         "BINH TAN",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN002793007",
#         "S1230700048",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.828195794307579,
#         106.7733690828174,
#         "18 TANG NHON PHU, P.PHUOC LONG B, ",
#         "QUAN 9",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN003915000",
#         "S1230700049",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.62991908399019,
#         106.71692132514566,
#         "LO NX-E1-E2, DUONG D1, KHU CONG NGHIEP LONG HAU, XA LONG HAU",
#         "CAN GIUOC",
#         "LONG AN",
#     ],
#     [
#         "YKKVN003965002",
#         "S1230700050",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.751035676989272,
#         106.61127196263875,
#         "241 DUONG 26,PHUONG BINH TRI DONG B  , ",
#         "BINH TAN",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN004383002",
#         "S1230700051",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         13.987031486263923,
#         107.99237541447324,
#         "DUONG LY THAI TO, TO 12, PHUONG YEN DO,",
#         "PLEIKU",
#         "GIA LAI",
#     ],
#     [
#         "MC191216000002",
#         "S1230700052",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.755872771815007,
#         106.74292579631158,
#         "LO SO BF 21-23-25-27-29,DUONG TAN THUAN,KCX TAN THUAN,P.TAN THUAN DONG",
#         "QUAN 7",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001566016",
#         "S1230700054",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.875662663730843,
#         106.73057725822333,
#         "PHONG KINH DOANH-CTCP MAY SAI GON 3 40/32 QUOC LO 13, HIEP BINH PHUOC ",
#         "THU DUC",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001676000",
#         "S1230700055",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.860849185863177,
#         106.68894959631228,
#         "1365/1 QUOC LO 1A, PHUONG AN PHU DONG, ",
#         "QUAN 12",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN002440036",
#         "S1230700056",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.83968566264628,
#         106.64933706747692,
#         "1B QUANG TRUNG,PHUONG 8,QUAN",
#         "GO VAP",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN003594002",
#         "S1230700058",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.835404478048432,
#         106.63442136747699,
#         "21/6C PHAN HUY ICH, PHUONG 14, ",
#         "GO VAP",
#         "HO CHI MINH",
#     ],
#     [
#         "MC210126000014",
#         "S1230700059",
#         Decimal("1.00000"),
#         Decimal("1.00000"),
#         None,
#         10.79873892744089,
#         106.58475073864138,
#         "229/35 LIEN KHU 4-5,P.BINH HUNG HOA\r\n B",
#         "BINH TAN",
#         "HCM",
#     ],
#     [
#         "MC190703000012",
#         "S1230700060",
#         Decimal("49188.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.806285415324725,
#         106.66638909716877,
#         "Số 10, đường Phổ Quang, phường 2",
#         "Tân Bình",
#         "TPHCM",
#     ],
#     [
#         "MC190703000013",
#         "S2852218553",
#         Decimal("49188.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.8241411863737,
#         106.69220602600463,
#         "366 Phan Văn Trị, Phường 5",
#         "Gò Vấp",
#         "Thành phố Hồ Chí Minh",
#     ],
#     [
#         "MC19070300   00014",
#         "3",
#         Decimal("122.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         10.737672991050914,
#         106.72544499631141,
#         "99 đường Nguyễn Thi Thập, Phường Tân Phú",
#         "Quận 7",
#         "TPHCM",
#     ],
#     [
#         "MC190703000015",
#         "4",
#         Decimal("1861.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.833772441629703,
#         106.6706595548403,
#         "SỐ 18, ĐƯỜNG PHAN VĂN TRỊ, PHƯỜNG 10   0",
#         "GÒ VẤP",
#         "HỒ CHÍ MINH",
#     ],
#     [
#         "MC190703000016",
#         "5",
#         Decimal("1700.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.754417697361298,
#         106.65163803949733,
#         "11 VÕ TRƯỜNG TOẢN, PHƯỜNG 15",
#         "QUẬN 5",
#         "TPHCM",
#     ],
#     [
#         "MC19070300    00017",
#         "6",
#         Decimal("182.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         10.737100592321609,
#         106.72539996435638,
#         "Lô A, khu dân cư Cityland, số 99 đường Nguyễn Thi Thập, Phường Tân Phú",
#         "Quận 7",
#         "HCM",
#     ],
#     [
#         "MC190703000018      8",
#         "7",
#         Decimal("12.00000"),
#         Decimal("0.00000"),
#         "5T",
#         10.819410113629296,
#         106.70194892514708,
#         "420 Nơ Trang Long, Phường 13",
#         "Bình Thạnh",
#         "Hồ Chí Minh",
#     ],
#     [
#         "MC190703000019",
#         "8",
#         Decimal("21.00000"),
#         Decimal("0.00000"),
#         "5T",
#         10.78085784198798,
#         106.63160549815758,
#         "53 Đường Nguyễn Sơn, P. Phú Thạnh",
#         "Tân Phú",
#         "Hồ      Chí Minh",
#     ],
#     [
#         "MC190703000020",
#         "9",
#         Decimal("1700.00000"),
#         Decimal("0.00000"),
#         "5T",
#         10.780667160763866,
#         106.63178008296076,
#         "53 Đường Nguyễn Sơn, P. Phú Thạnh",
#         "Tân Phú",
#         "Hồ Chí Minh",
#     ],
#     [
#         "MC190703000021",
#         "10    0",
#         Decimal("156.00000"),
#         Decimal("0.00000"),
#         "10T",
#         10.825914779055791,
#         106.68012890426232,
#         "792 Nguyễn Kiêệm, P. 3",
#         "Gò Vấp",
#         "Tp. HCM ",
#     ],
#     [
#         "MC190703000022",
#         "11",
#         Decimal("61.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.70215679449556,
#         106.60922571997646,
#         "LÔ IIIB2, Trung Tâm Thương Mại Bình Điền,Đường  Nguyễn Van Linh    h, Khu Phố 6",
#         "Quan 8",
#         "HCM",
#     ],
#     [
#         "MC190703000023",
#         "12",
#         Decimal("468.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         110.702832333373399,
#         106.71408888182572,
#         "B30-B33 Nguyễn Hữu Thọ",
#         "QUẬN 7",
#         "TP HCM",
#     ],
#     [
#         "MC190703000024",
#         "13",
#         Decimal("900.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.824670299803746,
#         106.69164403949799,
#         "168 Phan Văn Trị, Phường 5",
#         "Gò Vấp",
#         "Hồ Chí Minh",
#     ],
#     [
#         "MC190703000025",
#         "14",
#         Decimal("1156.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         10.754229161503945,
#         106.65166243562358,
#         "11 VÕ TRƯỜNG TOẢN",
#         "Quận 5",
#         "Hồ Chí Minh",
#     ],
#     [
#         "MC190703000026",
#         "15",
#         Decimal("240.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.791082134547583,
#         106.70519867481649,
#         "2/3A Nguyễn Thị Minh Khai, P. Dakao",
#         "Quan 1",
#         "Thành phố Hồ Chí Minh",
#     ],
#     [
#         "MC190703000027",
#         "16",
#         Decimal("10.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.745645409601028,
#         106.73286228068469,
#         "Vincom+ KĐT Nam Long, Số 71, Trần Trọng Cung, Phường Tân Thuận Đông",
#         "Quận 7",
#         "Tp.HCM",
#     ],
#     [
#         "MC190703000028",
#         "17",
#         Decimal("69.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.801358803201547,
#         106.6535789953199,
#         "SỐ 20, ĐƯỜNG CỘNG HÒA,   , PHƯỜNG 12",
#         "TÂN  BÌNH",
#         "Hồ Chí Minh",
#     ],
#     [
#         "MC190703000029",
#         "18",
#         Decimal("497.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.786668431857239,
#         106.6450357701823,
#         "Lô M, Chung cư Bàu Cát 2, Vườn Lan",
#         "Tân Bình",
#         "Hồ C   Chí Minh",
#     ],
#     [
#         "MC190703000030",
#         "19",
#         Decimal("1341.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         13.089938138379788,
#         109.31141598182182,
#         "kp Chu Van An, thua dat so 15, P.5, Tuy Hoa, Phu Yen",
#         "",
#         "",
#     ],
#     [
#         "YKKVN001790001",
#         "20",
#         Decimal("111.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         10.769570719747994,
#         106.69274918987253,
#         "4TH FLOOR, 76 LE LAI, BEN THANH WARD, ",
#         "QUAN 1",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001536005",
#         "21",
#         Decimal("1849.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         10.816882077107154,
#         106.6113164264207,
#         "CUM 6-2, DUONG M14, KCN",
#         "TAN BINH",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001536004",
#         "22",
#         Decimal("1900.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         10.79735553387646,
#         106.61826074360721,
#         "LO III,25B,DUONG 19/5A,KCN ",
#         "TAN BINH",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001536003",
#         "23",
#         Decimal("1900.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.853501549270407,
#         106.60256738962947,
#         "2/7G NGUYEN THI SOC -BA DIEM",
#         "HOC MON",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001536002",
#         "24",
#         Decimal("1850.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.705233747475107,
#         106.59819259204659,
#         "C14/25 AP 3, XA TAN KIEN",
#         "BINH CHANH",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001536001",
#         "25",
#         Decimal("64.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         10.772474411206565,
#         106.69799557054573,
#         "4TH FLOOR, 76 LE LAI, BEN THANH WARD, ",
#         "QUAN 1",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN002793009",
#         "26",
#         Decimal("848.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.546319708380269,
#         106.38636460554008,
#         "NO 27,NGUYEN THI BAY STREET,WARD 6",
#         "TAN AN",
#         "LONG AN",
#     ],
#     [
#         "YKKVN002793008",
#         "27",
#         Decimal("1639.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.98667209324086,
#         106.71588106722169,
#         "DUONG LIEN , BINH CHUAN ",
#         "THUAN AN",
#         "BINH DUONG",
#     ],
#     [
#         "YKKVN001537002",
#         "28",
#         Decimal("486.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.818932642800332,
#         106.62771111165259,
#         "36 TAY THANH, PHUONG TAY THANH",
#         "TAN PHU",
#         "HO CHI MINH",
#     ],
#     [
#         "YKKVN001537001",
#         "29",
#         Decimal("53.00000"),
#         Decimal("0.00000"),
#         "1T",
#         10.77113588566068,
#         106.69506125398182,
#         "4TH FLOOR, 76 LE LAI, BEN THANH WARD, ",
#         "QUAN 1",
#         "HO CHI MINH",
#     ],
#     [
#         "MC220510000003",
#         "30",
#         Decimal("20.00000"),
#         Decimal("0.00000"),
#         "1T3",
#         20.4414449,
#         106.1574427,
#         "3-34 Đường Trần Anh Tông, Lộc Vượng",
#         "Nam Định",
#         "Liên hệ nhận hàng : 0912863123",
#     ],
#     [
#         "MC220510000002",
#         "31",
#         Decimal("311.00000"),
#         Decimal("0.00000"),
#         "1T5",
#         21.586099856870742,
#         105.84283181998013,
#         "Số 80, tổ 29 đường Hoàng Ngân, phường Phan Đình Phùng",
#         "Thái Nguyên",
#         "Mr Liêm - 0944952266",
#     ],
#     [
#         "ACE1109-001",
#         "S2309260111",
#         Decimal("938.72000"),
#         Decimal("3.97000"),
#         "1T85",
#         10.765192789956403,
#         106.634210380971,
#         "Số 13 Nguyễn Trọng Quyền Tân Thới Hòa ",
#         "TAN PHU",
#         "HO CHI MINH",
#     ],
#     [
#         "ACEGV08-001",
#         "S2309260109",
#         Decimal("1785.24000"),
#         Decimal("8.15000"),
#         "1T85",
#         10.823137911135815,
#         106.68556492330116,
#         "192A Nguyễn Thái Sơn Phường 4 ",
#         "GO VAP",
#         "HO CHI MINH",
#     ],
#     [
#         "ACEBL1960-009",
#         "S2309260111",
#         Decimal("305.84000"),
#         Decimal("1.89000"),
#         "1T85",
#         10.754275999507401,
#         106.65038486747628,
#         "109-111 Đường Nguyễn Thị Nhỏ ",
#         "QUAN 11",
#         "HO CHI MINH",
#     ],
# ]
# print(len(matrix))
# data1 = []
# for item in data:
#     lat = item[0]
#     lon = item[1]
#     for value in matrix:
#         if lat == value[5] and lon == value[6]:
#             add_one = value[7]
#             add_two = value[8]
#             add_three = value[9]
#             data1.append([add_one, add_two, add_three])
# for value in data1:
#     print(value)
# data = 15.3
# data1 = [10, 23, 44, 22, 55]


# # Tạo một hàm tùy chỉnh để tính toán khoảng cách tuyệt đối giữa số và data
# def absolute_difference(x):
#     return abs(x - data)


# closest_value = min(data1, key=absolute_difference)
# print("Số gần nhất với giá trị data là:", closest_value)

# Điều kiện bạn muốn kiểm tra
data = 1
data1 = [1, 2, 3, 4, 5]
s1 = f"""{"quần đùi"if data in data1 else "quần què"} """
print("check valeu data s1", s1)

daata = "84.25 km"
print("check value data", daata[:-2])

# btn_Compare.clicked.connect(fun_Compare)

# def fun_Compare():
#     print("check value data cluster", selected_cluster)
#     input_dialog = DialogCompare(self)
#     input_dialog.exec_()
