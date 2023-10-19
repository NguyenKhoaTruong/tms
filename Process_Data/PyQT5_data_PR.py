from dotenv import load_dotenv
import os
import json


class data_Parameter:
    def __init__(self):
        load_dotenv()
        self.file_Path = os.getenv("DATA_JSON")

    def save_Data_JSON(self, point, distance, start_Point):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                points = data.get("points", [])
                start_Points = data.get("start_Points", [])
                distances = data.get("distances", [])
        except FileNotFoundError:
            points = []
            start_Points = []
            distances = []

        for index, value in enumerate(point):
            points.append(point[index])
            distances.append(distance[index])

        new_data = {
            "data": [
                {
                    "points": points,
                    "distances": distances,
                    "start_Points": start_Points.append(start_Point),
                }
            ]
        }
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)

    def get_Param(self):
        if os.path.exists(self.file_Path):
            with open(self.file_Path, "r") as file:
                config_data = json.load(file)
            data_list = config_data["data"]
            first_data_item = data_list[0]
            points = first_data_item["points"]
        else:
            print(f"File {self.file_Path} không tồn tại")

    def remove_File(self):
        if os.path.exists(self.file_Path):
            os.remove(self.file_Path)
            print(f"File '{self.file_Path}' đã được xoá.")
        else:
            print(f"Tệp '{self.file_Path}' không tồn tại.")
