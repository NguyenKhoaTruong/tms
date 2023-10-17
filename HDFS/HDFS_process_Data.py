import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from azure.storage.filedatalake import DataLakeServiceClient
from DB.Migration import get_Data_DB
import pandas as pd

# Data LAKE user
# from azure.identity import DefaultAzureCredential


class proCData:
    def __init__(self):
        self.rawData = get_Data_DB().dataSource()
        self.readData = pd.read_csv("Pyqt5/HDFS/DataSoucrce.csv")
        self.show_Info_Data()
        self.clean_Data()
        self.static_Data()
        self.transform_Data()

    def show_Info_Data(self):
        self.data_Info = self.readData.info
        self.data = self.readData.head(20)

    def clean_Data(self):
        # sử dụng lọc đối với các biến là số hoặc chuỗi bằng nhau:
        # data_=data[['OrderId'][0]]>'1602004'
        dataFilter = self.data[["OrderId", "ItemNo", "Latitude", "Longitude"]]
        # xóa các phần tử NaN có trong dữ liệu:
        self.data_clean = dataFilter.dropna()
        self.data_clean.info

    def static_Data(self):
        # thống kê dữ liệu :
        print("Thống kê dữ liệu", self.data_clean.describe())

    def transform_Data(self):
        # biến đổi dữ liệu gộp hai cột lat và lon
        print("Biến đổi dữ liệu", self.data_clean)
        self.data_clean["OrderWhere"] = "{},{}".format(
            self.data_clean["Latitude"], self.data_clean["Longitude"]
        )
        print(self.data_clean["OrderWhere"])


class data_Lake:
    # SDK Data Azuze
    def __init__(self):
        print("")


if __name__ == "__main__":
    proCData()
