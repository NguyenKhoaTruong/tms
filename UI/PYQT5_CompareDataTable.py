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
        # print('check data_',data_[0],len(data_)[0])
        # volume_Weight = np.array(data_, dtype=object)
        # content_Html=self.get_DataWeightVolume(volume_Weight)
        # self.load_UI(content_Html)
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
        ).tolist()
        print(data)
        print(point)
        for items in point:
            for item in items:
                data = []
                for value in item:
                    lat = value[0]
                    lon = value[1]
                    for data_ in arr_:
                        if lat == data_[2] and lon == data_[3]:
                            print(data)
                            print(data_)
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
        # print(arr_Point)
        _content=""
        for i,items in enumerate(arr_Point):
            html_Trip="<div class=\"content\"><table id=\"customers\"><tr><th></th>"
            html_Capacity="""<tr><th>Weight/Equipment</th>"""
            html_Weight="""<tr><th>Weight</th>"""
            html_Volume="""<tr><th>Volume</th>"""
            html_Orders="""<tr><th>Order</th>"""
            html_Drops="""<tr><th>Drops</th>"""
            html_Total="""<tr><th>Total</th>"""
            orders=len(items)
            _iterNum=""
            sum_kg=0
            sum_m3=0
            for index, value in enumerate(items):
                volume = value[0]
                weight = value[1]
                sum_kg += volume
                sum_m3 += weight
                if sum_kg > self.required:
                    html_Total += "<td><i class=\"fa fa-times\" style=\"font-size:30px;color:red\"></i></td>"
                else:
                    html_Total += "<td><i class=\"fa fa-check\" style=\"font-size:30px;color:green\"></i></td>"
                html_Trip += f"""<th> Trip {index + 1}</th>"""
                html_Orders += f"""<td>{orders}</td>"""
                html_Drops += f"""<td>{orders}</td>"""
                html_Weight += f"""<td>{float(sum_kg)}</td>"""
                html_Volume += f"""<td>{float(sum_m3)}</td>"""
                html_Capacity +=f"""<td>{round((float(sum_kg)/self.required)*100,3)}%</td>"""
            _content+=f"""{html_Trip}</tr>{html_Orders}</tr>{html_Drops}</tr>{html_Weight}</tr>
            {html_Volume}</tr>{html_Capacity}</tr>{html_Total}</tr></table></div>"""
            _iterNum +=f"""<p>Iteration : {index +1 }</p>"""
        return _content
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
                    {content}
                </div>
            </body>
        </html>
        """
        self.browser.setHtml(html_content)
        self.show()

