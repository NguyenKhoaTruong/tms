import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from decimal import Decimal, ROUND_DOWN
import UI.css_UI as css
import numpy as np


class ui_DataTableCompare(QWidget):
    def __init__(self,*arg):
        super().__init__()
        self.layout_ = QVBoxLayout()
        self.browser = QWebEngineView()
        self.matrix=arg[0]
        self.point=arg[1]
        self.required=arg[2]
        self.ui_()

    def ui_(self):
        self.setWindowTitle("Data Table Compare")
        self.showMaximized()
        self.layout_.addWidget(self.browser)
        self.setLayout(self.layout_)
        self.set_Data()
    def set_Data(self):
        data_=self.cal_DataKGM3(self.matrix,self.point)
        volume_Weight = np.array(data_, dtype=object)
        content_Html=self.get_DataWeightVolume(volume_Weight)
        self.load_UI(content_Html)
    def cal_DataKGM3(self,data,point):
        data_Kg = []
        arr_ = np.array(
            [
                [
                    item[2],
                    item[3],
                    float(item[5]),
                    float(item[6]),
                ]
                for item in data
            ]
        )
        for items in point:
            data = []
            for value in items:
                lat = value[0]
                lon = value[1]
                for data_ in arr_:
                    if lat == data_[2] and lon == data_[3]:
                        data.append(data_)
            data_Kg.append(data)
        return data_Kg
    def calculator_Drops(self, drops):
        data = []
        seen_Data = set()

        for item in drops:
            volume, weight, latitude, longitude = item
            coordinates = (latitude, longitude)

            if coordinates not in seen_Data:
                data.append(item)
                seen_Data.add(coordinates)
        return data
    def get_DataWeightVolume(self,arr_Point):
        list_Option = ""
        trip = "<tr><th></th>"
        order = "<tr><th>Order</th>"
        drops = "<tr><th>Drops</th>"
        weight_TB = "<tr><th>Weight</th>"
        volume_TB = "<tr><th>Volume</th>"
        capacity ="<tr><th>Weight/Equipment</th>"
        total="<tr><th>Total</th>"
        for index, value in enumerate(arr_Point):
            sum_kg = 0
            sum_m3 = 0
            for item in value:
                volume = item[0]
                weight = item[1]
                sum_kg += volume
                sum_m3 += weight
            capacity+=f"""<td>{round((float(sum_kg)/self.required)*100,3)}%</td>"""
            if sum_kg > self.required:
                total+="<td><i class=\"fa fa-times\" style=\"font-size:30px;color:red\"></i></td>"
            else:
                total+="<td><i class=\"fa fa-check\" style=\"font-size:30px;color:green\"></i></td>"
            trip += f"""<th> Trip {index + 1}</th>"""
            order += f"""<td>{len(value)} </td>"""
            drops += f"""<td>{len(self.calculator_Drops(value))}</td>"""
            weight_TB += f"""<td>{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)}</td>"""
            volume_TB += f"""<td>{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)}</td>"""
        trip += "</tr>"
        order += "</tr>"
        drops += "</tr>"
        weight_TB += "</tr>"
        volume_TB += "</tr>"
        capacity+="</tr>"
        total+="</tr>"
        list_Option += f"""{trip}{order}{drops}{weight_TB}{volume_TB}{capacity}{total}"""
        return list_Option
    def load_UI(self,content):
        html_content = f"""
        <html>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <head>
                <style>
                   {css.css_DataTable()}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="content">
                        <p>Iteration : 1</p>
                        <table id="customers">
                            {content}
                        </table>
                    </div>
                </div>
            </body>
        </html>
        """
        self.browser.setHtml(html_content)
        self.show()

