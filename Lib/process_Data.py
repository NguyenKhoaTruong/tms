import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from DB.Migration import get_Data_DB


class process_Data:
    def __init__(self):
        self.data = get_Data_DB().showDataImportFileLib()
        self.data_Order = []

    def get_Data_Order(self):
        data_Unique = []
        for index, value in enumerate(self.data):
            data = get_Data_DB().data_Select_Lib(value[2])
            data_Unique.append(data)
        for value in data_Unique:
            if value and value is not self.data_Order:
                self.data_Order.append(value)
        return self.data_Order

    def drop_Dulicate_Data(self):
        data = self.get_Data_Order()
        unique_data = []
        seen = set()

        for item in data:
            if item[0] not in seen:
                unique_data.append(item)
                seen.add(item[0])
        return unique_data
