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
from PyQt5.QtCore import QTime

from Process_Data.PyQT5_TSP import use_TSP
from Process_Data.PyQT5_TSP_Cluster import use_TSP_Cluster
from Map_.PyQT5_Map_Cluster import Show_Map_Cluster
from UI.PyQT5_Dialog_Location import InputDialog
from UI.PyQT5_LoadingData import LoadingGif
from UI.PyQT5_Dialog_Compare import DialogCompare
import UI.css_UI as css
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


class ui_Cluster(QWidget):
    def __init__(self, data, dataOrder, num_Cluster):
        super().__init__()
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
        self.array_Point = []
        self.on_Return = False
        self.off_Return = False
        self.start_Point = False
        self.data_Cluster = dataOrder
        self.num_clusters = num_Cluster
        self.selected_cluster = []
        self.data_Point = []
        self.data_Center = []
        self.data_Matrix = []
        self.data_Start_Points = []
        self.data = [
            ["YKK", 10.707197855355952, 106.93615121102836],
            ["NABATI", 10.662705470457466, 106.70724887936655],
        ]
        self.ui_()

    def ui_(self):
        self.setWindowTitle("Cluster Data")
        self.showMaximized()
        self.layOut_UI = QVBoxLayout()
        self.layout_InCluster = QHBoxLayout()
        self.content_Input = QHBoxLayout()
        self.layout_UB = QHBoxLayout()
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

        self.cbOrigin = QComboBox()

        self.cbStart = QComboBox()
        self.cbStart.setFixedWidth(200)
        # Sửa
        self.cbTSP = QComboBox()
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

        self.layout_InCluster.addWidget(label_StartPoint)
        self.layout_InCluster.addSpacing(65)
        self.layout_InCluster.addWidget(self.cbStart)
        self.layout_InCluster.addSpacing(170)
        self.layout_InCluster.addWidget(label_TSP)
        self.layout_InCluster.addSpacing(85)
        self.layout_InCluster.addWidget(self.cbTSP)
        self.layout_InCluster.addSpacing(170)
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
        self.layout_OpCluster.addSpacing(150)
        self.layout_OpCluster.addWidget(label_ServiceTime)
        self.layout_OpCluster.addWidget(self.input_SETime)
        self.layout_OpCluster.addStretch(1)
        self.layout_OpCluster.addWidget(self.modeReturn)
        self.layout_OpCluster.addWidget(self.modeStartPoint)

        self.content_Input.addWidget(label_WATime)
        self.content_Input.addWidget(self.input_WATime)
        self.content_Input.addSpacing(160)
        self.content_Input.addWidget(label_CTime)
        self.content_Input.addWidget(self.input_CTime)
        self.content_Input.addSpacing(170)
        self.content_Input.addStretch(1)
        self.content_Input.addWidget(self.btn_Compare)
        self.content_Input.addWidget(self.btn_Back)

        self.layOut_UI.addLayout(self.layout_InCluster)
        self.layOut_UI.addLayout(self.layout_OpCluster)
        self.layOut_UI.addLayout(self.content_Input)
        self.layOut_UI.addLayout(self.layout_UB)

        self.set_Style()
        self.data_Start_Point()
        self.set_ValueStartTime()
        self.show_area()
        self.setLayout(self.layOut_UI)
        self.show_Input_Data_TSP()
        self.role_Menu()
        icon = QIcon("logo.ico")  # Thay đổi đường dẫn tới biểu tượng của bạn
        self.setWindowIcon(icon)

    def role_Menu(self):
        if len(self.data_Cluster) > 10:
            self.set_UICluster()
            self.show_Data_Cluster()
        else:
            self.showMaximized()
            self.set_UINoCluster()
            self.get_Off_Return()
            self.add_UINoCluster()
            ShowMapCluster(self.array_Point, self.layout_UB)

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
        kmeans = KMeans(
            n_clusters=self.num_clusters,
            init="k-means++",
            n_init=30,
            max_iter=100,
            tol=1e-4,
            random_state=0,
        )

        kmeans.fit(self.array_Matrix)
        print('checl value data matrix',self.array_Matrix)
        self.labels = kmeans.labels_
        self.centers = kmeans.cluster_centers_

        self.set_ValueDataMatrix(self.labels)
        self.set_ValueDataCenter(self.centers)
        self.set_ValueDataPoint(self.labels)
        # thực hiện tách cụm khi cụm có nhiều data
        # self.divided_Cluster()

        self.cbCluster.addItems([f"Trip {i+1}" for i in range(len(self.data_Point))])
        self.set_ValueClusterData()
        self.cbCluster.currentIndexChanged.connect(self.show_Data_K_Mean_TSP)
        self.show_Map_Cluster()

    def set_ValueClusterData(self):
        self.selected_cluster = self.data_Point[0]

    # chia nhỏ cụm
    def divided_Cluster(self):
        def convent_DataCenter(data, center_Data):
            for value in data:
                center_Data.append([value[2], value[3]])
            # print("check value data centreDataa", len(center_Data))
            return center_Data

        data = []
        temp = []
        dataPoint = self.data_Point
        data_Center = self.data_Center
        for index, value in enumerate(dataPoint):
            if len(value) > 25:
                temp.append(index)
                num = len(value) // 3
                kmean_Sub = KMeans(n_clusters=num)
                kmean_Sub.fit(value)
                labels_Sub = kmean_Sub.labels_
                center_Sub = kmean_Sub.cluster_centers_
                data_new = []
                for j in range(num):
                    sub_Data = np.array(value)[labels_Sub == j]
                    data_new.append(sub_Data)
                data.extend(data_new)

            else:
                data.append(value)
        # print("check vlaue data", data, len(data))
        # Xóa dữ liệu trong biến data Point và center
        # print("check value data point", dataPoint, len(dataPoint))
        new_Point = np.delete(dataPoint, temp[0])
        # print("check value len new point strat", len(new_Point))
        data_Center.pop(temp[0])
        # thêm dữ liệu mới phân cụm vào data:
        new_Point = np.append(new_Point, data)
        # print("check value data new point", new_Point, len(new_Point))
        new_Center = convent_DataCenter(data_Center, center_Sub)
        # print("check len point", len(new_Point))
        # print("check value data cemter", data_Center, len(data_Center))
        # data_Center.append
        # Cập nhật lại hai biến point và data center.
        # self.dataPoint,self.dataCemter

        # Trả ra kết quả cho hàm

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
        for i in range(self.num_clusters):
            cluster_points = self.array_Matrix[labels == i]
            self.data_Point.append(cluster_points)
        return self.data_Point

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
        self.selected_cluster = self.data_Point[index]
        self.selected_cluster = self.remove_data_duplicate(self.selected_cluster)
        self.cbOrigin.clear()
        for value in self.selected_cluster:
            self.cbOrigin.addItem("{},{}".format(value[0], value[1]))

    def show_Input_Data_TSP(self):  # dữ liệu hiển thị không cần phân cụm
        data_ = [[item[5], item[6]] for item in self.data_Cluster]
        converted_data = [[float(item) for item in sublist] for sublist in data_]
        self.array_Point = list(
            set(map(tuple, converted_data))
        )  # loại bỏ các phần tử trùng trong mảng:
        self.array_Point = [list(item) for item in self.array_Point]
        for value in self.array_Point:
            self.cbOrigin.addItem("{},{}".format(value[0], value[1]))
        self.cbOrigin.hide()

    def show_Map_Cluster(self):
        Show_Map_Cluster(
            self.data_Center,
            self.data_Point,
            self.layout_UB,
            self.layout_InCluster,
            # self.compare_TSP,
            self.cbTSP,
            self.on_Return,
            self.off_Return,
            self.data_array,
            self.cbCluster,
            self.cbStart,
        )

    def fun_Compare(self):
        input_dialog = DialogCompare(self)
        input_dialog.exec_()

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
