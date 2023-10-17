from dotenv import load_dotenv
import requests
import os


# Chuẩn hóa dữ liệu
class data_Proc:
    def __init__(self):
        load_dotenv()
        self.api_Key = os.getenv("API_KEY")
        self.api_Point = os.getenv("API_POINT")

    def get_Data(self, data):
        try:
            data_Unique = self.drop_Dulicate_Data(data)
            fill_Data = self.auto_Fill_Data(data_Unique)
            return fill_Data
        except ValueError as e:
            print("Log Error", e)

    def drop_Dulicate_Data(self, data):
        unique_data = []
        seen = set()

        for item in data:
            if item[0] not in seen:
                unique_data.append(item)
                seen.add(item[0])
        return unique_data

    def auto_Fill_Data(self, data):
        try:
            data_Check_Process = [list(item) for item in data]
            for index, value in enumerate(data_Check_Process):
                if value[5] == "" or value[6] == "":
                    address = f"{value[7]}, {value[8]}, {value[9]}"

                    params = {"address": address, "key": self.api_Key}
                    response = requests.get(self.api_Point, params=params)
                    data_ = response.json()
                    if data_["status"] == "OK":
                        lat = data_["results"][0]["geometry"]["location"]["lat"]
                        lon = data_["results"][0]["geometry"]["location"]["lng"]
                        data_Check_Process[index][5] = lat
                        data_Check_Process[index][6] = lon
            return data_Check_Process
        except ValueError as e:
            print("Log Error", e)
