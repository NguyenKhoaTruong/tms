import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from DB.Migration import get_Data_DB
from hdfs import InsecureClient
from dotenv import load_dotenv
from decimal import Decimal
import pandas as pd
import openpyxl
import os
import stat


# Lấy dữ liệu từ data base -> lưu file -> Xử lý ở data pipeline : hadoop namenode -format -clusterID CID-4c1f6d58-a1b7-44e2-9b45-a3e946f69b06
class HDFS_Connect_DB:
    def __init__(self):
        self.headers = [
            "Pick up",
            "Order No",
            "Weight",
            "Volume",
            "Truck",
            "Addr1",
            "Addr2",
            "Addr3",
            "Lat",
            "Lon",
        ]
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.file_ = "HDFS/data.xlsx"
        self.sheet.append(self.headers)
        self.data = []
        self.create_file()
        self.get_Data()

    def create_file(self):
        with open(self.file_, mode="w") as file:
            pass

    def get_Data(self):
        data_ = get_Data_DB().data_lake()
        for value_ in data_:
            row_data = [
                str(item) if isinstance(item, Decimal) else item for item in value_
            ]
            self.sheet.append(row_data)
        self.workbook.save(self.file_)
        print("Đã lưu dữ liệu vào File Data.xlsx")


# Xử lý dữ liệu lưu trên hadoop
class HDFS_:
    def __init__(self):
        # HDFS_Connect_DB()
        load_dotenv()
        self.url = os.getenv("URL_HDFS")
        self.userName = os.getenv("USER_NAME_DT")
        self.file_path = os.getenv("FILE_PATH")
        self.hdfs_path = os.getenv("HDFS_PATH")
        self.hdfs_path_ = os.getenv("HDFS_PATH")
        self.local_file_path = os.getenv("FILE_PATH")
        self.file_log_app = os.getenv("FILE_LOG_APP")
        self.file_data_order = os.getenv("FILE_DATA_ORDER")
        self.hdfs_file_path = os.getenv("HDFS_FILE_PATH")

        # các quyền truy cập:
        self.owner_permission = (
            stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
        )  # Quyền đọc, ghi và thực thi cho người sở hữu
        self.group_permission = (
            stat.S_IRGRP | stat.S_IXGRP
        )  # Quyền đọc và thực thi cho nhóm người dùng
        self.others_permission = stat.S_IROTH | stat.S_IXOTH

        self.connect_hdfs()
        self.create_Forder_HDFS()
        self.save_File_HDFS()
        self.show_Info_File()
        # self.download_File()
        self.accsess_Permissions_File()
        self.show_Info_Permissions()

    def connect_hdfs(self):
        self.client = InsecureClient(self.url, user=self.userName)

    def create_Forder_HDFS(self):
        self.client.makedirs(self.hdfs_path)

    def save_File_HDFS(self):
        self.client.upload(self.hdfs_path_, self.file_log_app, overwrite=True)
        self.client.upload(self.hdfs_path_, self.file_data_order, overwrite=True)

    def show_Info_File(self):
        file_info = self.client.status(self.hdfs_file_path)
        print(f"File size: {file_info['length']} bytes")

    def download_File(self):
        downloaded_local_file_path = "D:/PythonGUI-ManageEmployee/Pyqt5{}".format(
            self.file_path
        )  # Tải file từ HDFS về máy tính local
        self.client.download(
            self.hdfs_file_path, downloaded_local_file_path, overwrite=True
        )
        readData = pd.read_csv(downloaded_local_file_path)
        print("check value read data", readData)
        print("check data", readData.info)

    def accsess_Permissions_File(self):
        permissions = (
            self.owner_permission | self.group_permission | self.others_permission
        )
        file_path_permissions = self.file_data_order
        os.chmod(file_path_permissions, permissions)

        file_path_permissions = "{}/{}".format(self.hdfs_path, self.file_data_order[5:])
        permissions = "755"
        self.client.set_permission(file_path_permissions, permissions)
        print("Đã Phân Quyền File")

    def show_Info_Permissions(self):
        # Đường dẫn đến tệp cần kiểm tra quyền
        file_path = self.file_data_order

        # Lấy thông tin về quyền của tệp
        file_permissions = os.stat(file_path).st_mode

        # Đổi định dạng của quyền từ số nguyên sang chuỗi bít
        permission_string = oct(file_permissions)[-4:]

        print(f"Quyền của tệp {file_path}: {permission_string}")
