import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from tkinter import messagebox as mb
from DB.Migration import get_Data_DB
from UI.PyQT5_UI_Cluster import ui_Cluster
from Process_Data.PyQT5_Data import data_Proc


class ClusterData:  # Sửa lại phân cụm dữ liệu
    def __init__(self, dataSelect, mainWindow, num_Cluster, type_Equipment):
        self.dataOrder = []
        self.dataSelect_ = []
        self.dataCondition = []
        try:
            print("Phân Cụm Dữ Liệu Lớn")
            data = get_Data_DB().checkDataCluster()
            for value in data:
                self.dataOrder.append([value[0], value[1], value[6], value[7]])
            data_clear = [
                item
                for item in self.dataOrder
                if all(element != "" for element in item)
            ]
            self.valid_Data_Select(
                dataSelect, mainWindow, data_clear, num_Cluster, type_Equipment
            )
        except ValueError as e:
            print("Log Error", e)

    def valid_Data_Select(self, data, data_UI, data_clear, num_Cluster, type_Equipment):
        try:
            if len(data) == 0:
                mb.showinfo(
                    title="Notification!!!",
                    message="Chưa có dữ liệu nào được chọn!!",
                )
            else:
                for value_ in data:
                    self.dataSelect_.append(value_[2])

                data_Select = get_Data_DB().data_Select(self.dataSelect_)
                data_ = data_Proc().get_Data(data_Select)
                data_UI.show_UI = ui_Cluster(
                    data_clear, data_, num_Cluster, type_Equipment
                )
                data_UI.show_UI.show()
        except ValueError as e:
            print("Log Error", e)
