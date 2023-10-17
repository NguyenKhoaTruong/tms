import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from HDFS.HDFS_ import HDFS_Connect_DB, HDFS_
from dotenv import load_dotenv
import pandas as pd
import schedule
import logging
import requests
import datetime
import time
import os


class data_Pipeline:
    def __init__(self):
        # HDFS_Connect_DB()
        load_dotenv()
        self.api_Point = os.getenv("API_POINT")
        self.api_Key = os.getenv("API_KEY")
        self.run_Data_Pipeline()
        # self.auto_Run_Data()

    def auto_Fill_Data(self, data_):
        for index, row in data_.iterrows():
            if pd.isna(row["Lat"]) or pd.isna(row["Lon"]):
                address = f"{row['Addr1']}, {row['Addr2']}, {row['Addr3']}"

                params = {"address": address, "key": self.api_Key}

                response = requests.get(self.api_Point, params=params)
                data = response.json()
                if data["status"] == "OK":
                    lat = data["results"][0]["geometry"]["location"]["lat"]
                    lon = data["results"][0]["geometry"]["location"]["lng"]

                    # Update the DataFrame with Lat and Lon values
                    data_.at[index, "Lat"] = lat
                    data_.at[index, "Lon"] = lon
        return data_

    def run_Data_Pipeline(self):
        # Bước 1: đọc file
        df = pd.read_excel("HDFS/data.xlsx")
        # Bước 2: Xử lý dữ liệu : # -Chuyển đổi những dữ liệu cần thiết.
        df["Truck"] = df["Truck"].str.replace("T", ".")
        df["Truck"] = df["Truck"].apply(
            lambda x: float(x[:-1]) if isinstance(x, str) else x
        )
        df["Order No"] = df["Order No"].str.replace("S", "", regex=False)

        df_unique = df.drop_duplicates(subset="Pick up")

        data = self.auto_Fill_Data(df_unique)[
            ["Pick up", "Order No", "Weight", "Volume", "Truck", "Lat", "Lon"]
        ]

        # Bước 3:Xử lý và tính toán dữ liệu: chuyển đến bước phân cụm dữ liệu
        df_Process_Last = data.values.tolist()

        logging.basicConfig(
            filename="HDFS/app.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logging.info("Clean Data")
        logging.info("{}".format(df_Process_Last))

        # Bước 4: Lưu trữ dữ liệu đã được xử lý
        self.save_Data_Process()
        # Bước 5:Trực quan hóa dữ liệu và báo cáo: hiển thị map,plt

        return df_Process_Last

    # Bước 6: Lập lich data chạy tự động: Lập lịch chạy data pipeline cứ mỗi 60 giây. Có thể điều chỉnh thời gian.
    def save_Data_Process(self):
        HDFS_()

    def save_Data(self):
        # tạo file:
        file_ = "HDFS/data_Order.xlsx"
        with open(file_, mode="w") as file:
            pass
        data = self.run_Data_Pipeline()
        # lưu dữ liệu vào file:
        data.to_excel(file_, index=False)

    def auto_Run_Data(self):
        schedule.every(5).seconds.do(self.run_Data_Pipeline)
        stop_Schedule = datetime.time(9, 55)
        while True:
            time_Now = datetime.datetime.now().time()
            if time_Now >= stop_Schedule:
                break
            schedule.run_pending()
            print("--runing--")
            time.sleep(1)
            self.save_Data()
