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
        content_Html=self.get_DataWeightVolume(data_)
        self.load_UI(content_Html)
    def cal_DataKGM3(self,data,point):
        data_Kg = []
        for items in point:
            b_=[]
            for item in items:
                _data = []
                for value in item:
                    q_=[]
                    lat = value[0]
                    lon = value[1]
                    for data_ in data:
                        if float(lat) == data_[2] and float(lon) == data_[3]:
                            _data.append(data_)
                    q_.append(_data)
                b_.append(q_)
            data_Kg.append(b_)
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
        _content=""
        for items in arr_Point:
            html_Trip="<div class=\"content\"><table id=\"customers\"><tr><th></th>"
            html_Capacity="""<tr><th>Weight/Equipment</th>"""
            html_Weight="""<tr><th>Weight</th>"""
            html_Volume="""<tr><th>Volume</th>"""
            html_Orders="""<tr><th>Order</th>"""
            html_Drops="""<tr><th>Drops</th>"""
            html_Total="""<tr><th>Total</th>"""
            _iterNum=""
            print('check valeu data items',items)
            for i,item in enumerate(items):
                print('check value data item',item)
                summ3=0
                sumkg=0
                html_Trip+=f"<td>Trip {i +1} </td>"
                html_Orders+=f"<td>{len(item[0])}</td>"
                html_Drops+=f"<td>{len(item[0])}</td>"
                for value in item:
                    print('check vlaue data value',value)
                    volume = value[0]
                    weight = value[1]
                    sumkg+=volume
                    summ3+=weight
                html_Volume+=f"""<td>{float(summ3)}</td>"""
                html_Weight+=f"""<td>{float(sumkg)}</td>"""
                html_Capacity +=f"""<td>{round((float(sumkg)/self.required)*100,3)}%</td>"""
                if sumkg > self.required:
                    html_Total += "<td><i class=\"fa fa-times\" style=\"font-size:30px;color:red\"></i></td>"
                else:
                    html_Total += "<td><i class=\"fa fa-check\" style=\"font-size:30px;color:green\"></i></td>"
                # _iterNum +=f"""<p>Iteration : {i_ +1 }</p>"""
            _content=f"""{html_Trip}</tr>{html_Orders}</tr>{html_Drops}</tr>{html_Weight}</tr>{html_Volume}</tr>{html_Capacity}</tr>{html_Total}</tr></table></div>"""
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
        print('check value data html content',html_content)
        self.browser.setHtml(html_content)
        self.show()

