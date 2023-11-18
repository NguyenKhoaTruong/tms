import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
    QLabel,
    QCheckBox,
    QLineEdit,
    QGridLayout,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Process_Data.PyQT5_TSP_Cluster import use_TSP_Cluster
from Cluster.Main_Cluster import Main_Clustering
from PyQt5.QtCore import QTime
from matplotlib.figure import Figure
from Process_Data.PyQT5_TSP import use_TSP
from Cluster.Compare_Accuracy import CompareAccuracy
from Map_.PyQT5_Map_Cluster import Show_Map_Cluster
from UI.PyQT5_Dialog_Location import InputDialog
from UI.PyQT5_LoadingData import LoadingGif
from UI.PyQT5_Dialog_Compare import DialogCompare
from UI.PYQT5_Capacity import Capacity_Mode
from PyQt5.QtCore import QFile, QTextStream
from Map_.PyQT5_Map import ShowMapCluster
from sklearn.cluster import KMeans
from PyQt5.QtWidgets import QWidget
from tkinter import messagebox as mb
from PyQt5.QtGui import QIcon
from dotenv import load_dotenv
from datetime import datetime
from PyQt5.QtCore import Qt
import numpy as np
import requests
import os
import UI.css_UI as css


class ui_Cluster(QWidget):
    def __init__(self, data, dataOrder, num_Cluster, type_Equipment):
        super().__init__()
        self.data = [
            ["YKK", 10.707197855355952, 106.93615121102836],
            ["NABATI", 10.662705470457466, 106.70724887936655],
        ]
        self.items_Mode = ["Volume", "Weight", "Trip Type"]
        self.api_Key = os.getenv("API_KEY")
        load_dotenv()
        self.array_Point = []
        self.on_Return = False
        self.off_Return = False
        self.start_Point = False
        self.data_Cluster = dataOrder
        self.num_clusters = num_Cluster
        self.equipment_Type = type_Equipment
        self.data_Map = ""
        self.selected_cluster = []
        self.data_Point = []
        self.data_Center = []
        self.data_Matrix = []
        self.data_Start_Points = []
        self.data_Weight = []
        self.labels = []
        self.centroid = []
        self.data_Iter=[]
        self.ui_()

    def ui_(self):
        self.setWindowTitle("Cluster Data")
        self.showMaximized()
        self.layOut_UI = QVBoxLayout()
        self.layout_InCluster = QHBoxLayout()
        self.content_Input = QHBoxLayout()
        self.layout_UB = QHBoxLayout()
        self.layout_Capacity = QHBoxLayout()
        self.layout_OpCluster = QHBoxLayout()

        label_StartPoint = QLabel("Start Point:")
        label_TSP = QLabel("Optimize Method:")
        self.label_Order = QLabel("Cluster Order:")
        self.add_Start_Point = QPushButton("Add Location", self)
        self.add_Start_Point.clicked.connect(self.show_Dialog_Location)

        # self.compare_TSP = QPushButton("Compare")

        self.btnStart = QPushButton("Start TSP")
        self.btnStart.clicked.connect(self.use_TSP)

        self.btnOnMode = QPushButton("On Return")
        self.btnOnMode.clicked.connect(self.get_On_Return)
        self.update_Status_Mode(self.btnOnMode, self.on_Return)

        self.btnOffMode = QPushButton("Off Return")
        self.btnOffMode.clicked.connect(self.get_Off_Return)
        self.update_Status_Mode(self.btnOffMode, self.off_Return)

        self.btn_CompareCluster = QPushButton("Compare Cluster")
        self.btn_CompareCluster.setFixedHeight(30)
        self.btn_CompareCluster.clicked.connect(self.compare_Accuracy_Algorithms)
        self.cbOrigin = QComboBox()

        self.cbStart = QComboBox()
        self.cbStart.setFixedWidth(200)
        # Sửa
        self.cbTSP = QComboBox()
        self.cbTSP.setFixedWidth(180)
        self.cbTSP.addItem("Nearest Neighbor")
        self.cbTSP.addItem("Randomized Tour")
        # self.cbTSP.addItem("Brute Force")
        # self.cbTSP.addItem("Branch And Bound")
        # self.cbTSP.addItem("2-OPT")
        # self.cbTSP.addItem("Line Kernighan Heuristic")
        # self.cbTSP.addItem("Greedy Algorithm")
        # self.cbTSP.addItem("Hill Climbing")

        self.cbTSP.addItem("Tabu Search")
        self.cbTSP.addItem("Ant Colony")
        self.cbTSP.addItem("Christofides")

        self.cbAlgorithmsCluster = QComboBox()
        self.cbAlgorithmsCluster.setFixedWidth(180)
        self.cbAlgorithmsCluster.addItem("K_Means")
        self.cbAlgorithmsCluster.addItem("Gausian Mixture")
        self.cbAlgorithmsCluster.addItem("Mean Shift")
        self.cbAlgorithmsCluster.addItem("Mini Batch K Mean")
        self.cbCluster = QComboBox()
        self.cbCluster.setFixedWidth(180)

        self.modeReturn = QCheckBox("Return Start")
        self.modeReturn.setChecked(False)
        self.modeReturn.stateChanged.connect(self.handleChangeMode)

        self.modeStartPoint = QCheckBox("Start Point")
        self.modeStartPoint.setChecked(True)
        self.modeStartPoint.stateChanged.connect(self.handleChangeModeStart)
        # set value
        self.set_ValueSR()
        # input data.
        label_StartTime = QLabel("Start Time:")
        label_WBTime = QLabel("Waiting Before Time:")
        label_ServiceTime = QLabel("Service Time:")
        label_WATime = QLabel("Waiting After Time:")
        label_CTime = QLabel("Congestion Time(0 -> 1 %):")
        label_Cluster = QLabel("Cluster:")

        self.btn_ShowCluster = QPushButton("View Map")
        self.btn_ShowCluster.clicked.connect(self.show_DataMapCluster)
        self.btn_ShowCluster.setFixedHeight(30)

        self.btn_Back = QPushButton("Back")
        self.btn_Back.setFixedHeight(30)
        self.btn_Back.setFixedWidth(100)
        self.btn_Back.hide()
        self.btn_Back.clicked.connect(self.fun_Back)

        self.btn_Compare = QPushButton("Compare")
        self.btn_Compare.setFixedHeight(30)
        self.btn_Compare.setFixedWidth(100)
        self.btn_Compare.hide()
        self.btn_Compare.clicked.connect(self.fun_Compare)

        self.input_STime = QComboBox()
        self.input_STime.setFixedWidth(200)
        self.input_STime.setStyleSheet("padding-left:10px")
        self.input_STime.currentIndexChanged.connect(self.handle_OnChangeTime)

        self.testip = QLineEdit()
        self.testip.setFixedWidth(100)

        self.input_WBTime = QLineEdit()
        self.input_WBTime.setFixedWidth(200)
        self.input_WBTime.setText(str(0))
        self.input_WBTime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_SETime = QLineEdit()
        self.input_SETime.setFixedWidth(200)
        self.input_SETime.setText(str(10))

        self.input_SETime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_WATime = QLineEdit()
        self.input_WATime.setFixedWidth(220)
        self.input_WATime.setText(str(0))

        self.input_WATime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_CTime = QLineEdit()
        self.input_CTime.setFixedWidth(200)
        self.input_CTime.setText(str(0.5))

        self.input_CTime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        boder_Capacity = QHBoxLayout()
        mode_Capacity = QGridLayout()
        label_Capacity = QLabel("Capacity View Mode")
        btn_Mode = QPushButton("Refresh")
        btn_Mode.clicked.connect(self.handle_Refresh)
        self.cb_Mode = QComboBox()
        figure = Figure()
        canvas = FigureCanvas(figure)
        mode_Capacity.addWidget(label_Capacity, 1, 0)
        mode_Capacity.addWidget(self.cb_Mode, 2, 0)
        mode_Capacity.addWidget(btn_Mode, 2, 1)
        mode_Capacity.setRowStretch(3, 1)
        mode_Capacity.setContentsMargins(10, 200, 0, 0)
        boder_Capacity.addLayout(mode_Capacity)
        boder_Capacity.addWidget(canvas)
        self.add_ItemMode(self.cb_Mode, self.items_Mode)
        self.chart(figure, canvas)
        self.custom_CSS(label_Capacity, btn_Mode, self.cb_Mode)

        self.layout_Capacity.addLayout(boder_Capacity)
        self.layout_InCluster.addWidget(label_StartPoint)
        self.layout_InCluster.addSpacing(65)
        self.layout_InCluster.addWidget(self.cbStart)
        self.layout_InCluster.addSpacing(170)
        self.layout_InCluster.addWidget(label_TSP)
        self.layout_InCluster.addSpacing(85)
        self.layout_InCluster.addWidget(self.cbTSP)
        self.layout_InCluster.addSpacing(130)
        self.layout_InCluster.addWidget(self.label_Order)
        self.layout_InCluster.addSpacing(10)
        self.layout_InCluster.addWidget(self.cbCluster)
        self.layout_InCluster.addStretch(1)
        self.layout_InCluster.addWidget(self.btnStart)
        self.layout_InCluster.addWidget(self.add_Start_Point)
        self.layout_InCluster.addWidget(self.cbOrigin)

        self.layout_OpCluster.addWidget(label_StartTime)
        self.layout_OpCluster.addSpacing(65)
        self.layout_OpCluster.addWidget(self.input_STime)
        self.layout_OpCluster.addSpacing(170)
        self.layout_OpCluster.addWidget(label_WBTime)
        self.layout_OpCluster.addSpacing(50)
        self.layout_OpCluster.addWidget(self.input_WBTime)
        self.layout_OpCluster.addSpacing(120)
        self.layout_OpCluster.addWidget(label_ServiceTime)
        self.layout_OpCluster.addWidget(self.input_SETime)
        self.layout_OpCluster.addStretch(1)
        self.layout_OpCluster.addWidget(self.btn_ShowCluster)
        self.layout_OpCluster.addWidget(self.modeReturn)
        self.layout_OpCluster.addWidget(self.modeStartPoint)

        self.content_Input.addWidget(label_WATime)
        self.content_Input.addWidget(self.input_WATime)
        self.content_Input.addSpacing(160)
        self.content_Input.addWidget(label_CTime)
        self.content_Input.addWidget(self.input_CTime)
        self.content_Input.addSpacing(120)
        self.content_Input.addWidget(label_Cluster)
        self.content_Input.addSpacing(50)
        self.content_Input.addWidget(self.cbAlgorithmsCluster)
        self.content_Input.addStretch(1)
        self.content_Input.addWidget(self.btn_CompareCluster)
        self.content_Input.addWidget(self.btn_Compare)
        self.content_Input.addWidget(self.btn_Back)
        self.add_MainLayout()
        self.set_Style()
        self.data_Start_Point()
        self.set_ValueStartTime()
        self.show_area()
        self.setLayout(self.layOut_UI)
        self.show_Input_Data_TSP()
        self.role_Menu()
        icon = QIcon("logo.ico")
        self.setWindowIcon(icon)

    def add_ItemMode(self, cb, item):
        for value in item:
            cb.addItem(value)
        return cb

    def chart(self, figure, canvas):
        ax = figure.add_subplot(111)
        categories = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        values = [25, 40, 30, 45, 50, 55, 65, 75, 75, 85]
        ax.bar(categories, values, color="skyblue")
        ax.set_title("K-Mean Cluster")
        ax.set_xlabel("Trip")
        ax.set_ylabel("Weight")
        canvas.draw()

    def custom_CSS(self, title, button, cb):
        title.setStyleSheet("font-size:15px")
        button.setFixedHeight(40)
        button.setFixedWidth(100)
        cb.setFixedHeight(40)
        cb.setFixedWidth(150)

    def add_MenuLayout(self):
        print()

    def add_MainLayout(self):
        self.layOut_UI.addLayout(self.layout_InCluster)
        self.layOut_UI.addLayout(self.layout_OpCluster)
        self.layOut_UI.addLayout(self.content_Input)
        self.layOut_UI.addLayout(self.layout_UB)
        # self.layOut_UI.addLayout(self.layout_Capacity)

    def role_Menu(self):
        if len(self.data_Cluster) > 10:
            self.set_UICluster()
            self.show_Data_Cluster()
            self.cal_Condisiton_Weight()
            self.show_Map_Cluster()
            # Capacity_Mode(self.layout_Capacity)
        else:
            self.showMaximized()
            self.set_UINoCluster()
            self.get_Off_Return()
            self.add_UINoCluster()
            ShowMapCluster(self.array_Point, self.layout_UB)

    def cal_Condisiton_Weight(self):
        total_Weight = []
        temp = 0
        for value in self.data_Weight:
            if value < self.equipment_Type:
                total_Weight.append(value)
            else:
                pass
        if (len(total_Weight) / len(self.data_Weight)) * 100 >= 60:
            # print("đủ điều kiện")
            pass
        else:
            while (len(total_Weight) / len(self.data_Weight)) * 100 < 60:
                temp += 1
                self.show_Data_Cluster()
                # print("chưa đủ điều kiện")
                if temp == 20:
                    break
        return total_Weight

    def set_UICluster(self):
        self.btnOffMode.hide()
        self.btnOnMode.hide()

    def set_UINoCluster(self):
        self.modeReturn.hide()
        self.label_Order.hide()
        self.btnOnMode.show()
        self.btnOffMode.show()
        self.btn_Compare.hide()
        self.btn_Back.hide()

    def add_UINoCluster(self):
        self.layout_InCluster.addWidget(self.btnStart)
        self.content_Input.addStretch(1)
        self.layout_OpCluster.addSpacing(10)
        self.layout_OpCluster.addWidget(self.btnOnMode)
        self.layout_OpCluster.addSpacing(10)
        self.layout_OpCluster.addWidget(self.btnOffMode)

    def handle_OnChangeTime(self, index):
        selected_time = self.input_STime.currentText()

    def set_ValueStartTime(self):
        for hour in range(24):
            for minute in range(0, 60, 15):  # Để hiển thị thời gian cách 15 phút
                time = QTime(hour, minute)
                self.input_STime.addItem(time.toString("hh:mm"))
        self.input_STime.setCurrentText("07:00")

    def handleChangeMode(self, state):
        if state == 2:
            self.on_Return = True
            self.off_Return = False
            print("Bật điều hướng.")
        else:
            self.off_Return = True
            self.on_Return = False
            print("Tắt điều hướng.")

    def handleChangeModeStart(self, state):
        if state == 2:
            self.start_Point = True
            self.cbStart.setDisabled(False)
            print("Bật Điểm Bắt Dầu")
        else:
            self.start_Point = False
            self.cbStart.setDisabled(True)
            print("Tắt Điểm Bắt Dầu")

    def set_Style(self):
        # self.compare_TSP.setFixedHeight(30)
        self.btnStart.setFixedHeight(30)
        self.add_Start_Point.setFixedHeight(30)
        css_Layout = css.css_Clsuter()
        self.setStyleSheet(css_Layout)

    def data_Start_Point(self):
        for item_data in self.data:
            item_text = item_data[0]
            self.cbStart.addItem(item_text, userData=item_data)
        self.set_DefaultValueSP()
        self.cbStart.currentIndexChanged.connect(self.onChange_Start_Point)

    def set_DefaultValueSP(self):
        data = self.cbStart.currentData()
        start_Point = [data[1], data[2]]
        self.data_Start_Points = start_Point

    def show_Dialog_Location(self):
        input_dialog = InputDialog(self)
        if input_dialog.exec_() == QDialog.Accepted:
            item_Address = input_dialog.input_Address.text()
            item_Code = input_dialog.input_Code.text()
            if item_Address:
                location_Data = self.get_Location_Text(item_Address, item_Code)
                self.cbStart.addItem(location_Data[0], userData=location_Data)

    def get_Location_Text(self, address, code):
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.api_Key}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            latitude = location["lat"]
            longitude = location["lng"]
            data_ = [code, latitude, longitude]
        else:
            print("Không thể tìm thấy vị trí.")
        return data_

    def onChange_Start_Point(self, index):
        item_data = self.cbStart.itemData(index)
        if item_data is not None:
            print("Start Point Location:", item_data)
        start_Points = [item_data[1], item_data[2]]
        self.data_Start_Points = start_Points

    def show_area(self):
        try:
            if len(self.data_Cluster) < 10:
                self.cbCluster.hide()
                # self.compare_TSP.hide()
        except ValueError as e:
            print("Log Error", e)

    def show_Data_Cluster(self):
        labels, centers = self.use_KmeanCluster()
        self.set_ValueDataMatrix(labels)
        self.set_ValueDataCenter(centers)
        self.set_ValueDataPoint(labels)
        self.cal_WeightTrip()
        self.cbCluster.addItems([f"Trip {i+1}" for i in range(len(self.data_Point))])
        self.set_ValueClusterData()
        self.cbCluster.currentIndexChanged.connect(self.show_Data_K_Mean_TSP)

    def use_KmeanCluster(self):
        self.data_array = np.array(self.data_Cluster)
        self.array_Matrix = np.array(
            [
                [
                    float(item[5]),
                    float(item[6]),
                ]
                for item in self.data_array
            ]
        )
        weight = np.array([float(item[2]) for item in self.data_array]).tolist()
        volume = np.array([float(item[3]) for item in self.data_array]).tolist()
        kmeans = KMeans(
            n_clusters=self.num_clusters,
            init="k-means++",
            n_init=30,
            max_iter=100,
            tol=1e-4,
        )
        kmeans.fit(self.array_Matrix, sample_weight=weight)
        iter = kmeans.n_iter_
        # text = self.cb_Mode.currentText()
        # if text == "Volume":
        #     kmeans.fit(self.array_Matrix, sample_weight=volume)
        # elif text == "Weight":
        #     kmeans.fit(self.array_Matrix, sample_weight=weight)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_
        self.labels.extend([labels])
        self.centroid.extend([centers])
        # print("iter", iter)
        return labels, centers

    def set_ValueClusterData(self):
        self.selected_cluster = self.data_Point[0]

    def remove_DataOld(self, index, data):
        print()

    def set_ValueDataMatrix(self, labels):
        for i in range(self.num_clusters):
            cluster_data = [
                self.data_Cluster[j]
                for j in range(len(self.data_Cluster))
                if labels[j] == i
            ]
            self.data_Matrix.append(cluster_data)
        return self.data_Matrix

    def set_ValueDataCenter(self, centers):
        for value in centers:
            self.data_Center.append([value[0], value[1]])
        return self.data_Center

    def set_ValueDataPoint(self, labels):
        iterPoint=[]
        for i in range(self.num_clusters):
            cluster_points = self.array_Matrix[labels == i]
            self.data_Point.append(cluster_points)
            iterPoint.append(cluster_points)
        self.data_Iter.append(iterPoint)
        return self.data_Point

    def cal_WeightTrip(self):
        weight = []
        data = np.array(self.data_Cluster).tolist()
        points_ = self.data_Point
        for item in points_:
            temp = []
            for value in item:
                lat = float(value[0])
                lon = float(value[1])
                for value_ in data:
                    if lat == float(value_[5]) and lon == float(value_[6]):
                        temp.append(float(value_[2]))
            weight.append(temp)
        weight_Trip = self.convent_DataWeight(weight)
        self.data_Weight = weight_Trip
        return self.data_Weight

    def convent_DataWeight(self, data):
        weight_Convent = []
        for items in data:
            tmp = 0
            for value in items:
                tmp += value
            weight_Convent.append(tmp)
        return weight_Convent

    def remove_data_duplicate(self, data):
        data_Clean = []
        seen_rows = set()
        for row in data:
            row_tuple = tuple(row)
            if row_tuple not in seen_rows:
                data_Clean.append(row)
                seen_rows.add(row_tuple)
        return data_Clean

    def show_Data_K_Mean_TSP(self, index):  # Dữ liệu phân cụm;
        self.selected_cluster = self.data_Point[-self.num_clusters:][index]
        self.selected_cluster = self.remove_data_duplicate(self.selected_cluster)
        self.cbOrigin.clear()
        for value in self.selected_cluster:
            self.cbOrigin.addItem("{},{}".format(value[0], value[1]))

    def show_Input_Data_TSP(self):  # dữ liệu hiển thị không cần phân cụm
        data_ = [[item[5], item[6]] for item in self.data_Cluster]
        converted_data = [[float(item) for item in sublist] for sublist in data_]
        self.array_Point = list(set(map(tuple, converted_data)))
        self.array_Point = [list(item) for item in self.array_Point]
        for value in self.array_Point:
            self.cbOrigin.addItem("{},{}".format(value[0], value[1]))
        self.cbOrigin.hide()

    def show_Map_Cluster(self):
        Show_Map_Cluster(
            self.data_Center[-self.num_clusters:],
            self.data_Point[-self.num_clusters:],
            self.layout_UB,
            self.layout_InCluster,
            # self.compare_TSP,
            self.cbTSP,
            self.on_Return,
            self.off_Return,
            self.data_array,
            self.cbCluster,
            self.cbStart,
            self.data_Map,
        )

    def fun_Compare(self):
        input_dialog = DialogCompare(self)
        input_dialog.exec_()

    def show_DataMapCluster(self):
        text_Selected = self.cbAlgorithmsCluster.currentText()
        data = np.array(
            [
                [
                    float(item[5]),
                    float(item[6]),
                ]
                for item in self.data_array
            ]
        )
        map_View = Main_Clustering().show_DataHTML(
            text_Selected, data, self.num_clusters
        )
        self.data_Map = map_View
        self.show_Map_Cluster()
        return self.data_Map

    def fun_Back(self):
        if self.layout_UB.count() >= 1:
            item = self.layout_UB.itemAt(0)
            self.layout_UB.removeItem(item)
        self.show_Map_Cluster()

    def get_On_Return(self):
        self.on_Return = not self.on_Return
        self.update_Status_Mode(self.btnOnMode, self.on_Return)
        if self.on_Return:
            self.off_Return = False
            self.update_Status_Mode(self.btnOffMode, self.off_Return)

    def get_Off_Return(self):
        self.off_Return = not self.off_Return
        self.update_Status_Mode(self.btnOffMode, self.off_Return)
        if self.off_Return:
            self.on_Return = False
            self.update_Status_Mode(self.btnOnMode, self.on_Return)

    def compare_Accuracy_Algorithms(self):
        data = np.array(
            [
                [
                    float(item[5]),
                    float(item[6]),
                ]
                for item in self.data_array
            ]
        )
        # CompareAccuracy().show_Accuracy(self, data, self.labels, self.centroid)
        # CompareAccuracy().show_TableAccuracy(self,self.data_array,self.data_Point[-self.num_clusters:],self.equipment_Type)
        CompareAccuracy().show_TableAccuracy(self,self.data_array,self.data_Iter,self.equipment_Type)

    def update_Status_Mode(self, button, is_active):
        color = "#4CAF50" if is_active else "white"
        button.setStyleSheet(
            f"background-color: {color}; color: black ;font-size:15px; width:10px ; height:10px"
        )

    def get_ParamTime(self):
        data_Time = []
        start_Time = self.input_STime.currentText()
        before_Time = self.input_WBTime.text()
        service_Time = self.input_SETime.text()
        after_Time = self.input_WATime.text()
        congestion_Time = self.input_CTime.text()
        time_format = "%H:%M"
        formatted_time = datetime.strptime(start_Time, time_format)
        timer = formatted_time.time()

        data_Time.append(
            [
                timer,
                int(before_Time),
                int(service_Time),
                int(after_Time),
                congestion_Time,
            ]
        )
        return data_Time

    # valid parameter
    def valid_Congestion_Time(self, data, param_UI):
        if len(data) < 0 and len(data > 1):
            param_UI.clear()
            mb.showwarning(title="Notification !!!", message="Congestion Time is 0->1")

    def set_ValueSR(self):
        self.start_Point = True
        self.on_Return = False
        self.off_Return = True

    def use_TSP(self):
        data_TShipTo = self.get_ParamTime()
        print('check vlaue data selected cluster',self.selected_cluster)
        if len(self.data_Cluster) > 10:
            use_TSP_Cluster(
                self.selected_cluster,
                self,
                self.cbOrigin,
                self.layout_UB,
                self.data_Center,
                self.data_array,
                self.data_Start_Points,
                self.on_Return,
                self.off_Return,
                data_TShipTo[0],
                self.start_Point,
            )
        else:
            data_Origin = self.cbOrigin.currentText().split(",")
            data_Origin = [float(x) for x in data_Origin]
            use_TSP(
                self.array_Point,
                self,
                data_Origin,
                self.layout_UB,
                np.array(self.data_Cluster),
                self.on_Return,
                self.off_Return,
                self.data_Start_Points,
            )

    def handle_Refresh(self):
        self.show_Data_Cluster()
        self.show_Map_Cluster()
