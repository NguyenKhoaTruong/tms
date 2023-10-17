import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWidgets import (
    QWidget,
    QTextEdit,
    QHeaderView,
    QPushButton,
    QTableWidget,
    QComboBox,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QDateEdit,
    QApplication,
    QLabel,
    QLineEdit,
    QGridLayout,
    QCheckBox,
)
from DB.Migration import get_Data_DB
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from datetime import date
from tkinter import messagebox as mb
import folium
from PyQt5 import QtWebEngineWidgets


class datePickerCompleteDate(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            "font-size: 25px ; padding-left: 20px ; padding-right:20px; padding-top:5px"
        )
        self.date = QtWidgets.QDateEdit(calendarPopup=True)
        self.menuBar().setCornerWidget(self.date, QtCore.Qt.TopLeftCorner)
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date.dateChanged.connect(self.onDateChanged)

    def onDateChanged(self, qDate):
        print("check date {0}/{1}/{2}".format(qDate.day(), qDate.month(), qDate.year()))


class CheckBoxHeader(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 39)
        self.dataExpressOrder = []
        self.dataOrderSelect = []
        self.setHorizontalHeaderLabels(
            ["Action"]
            + [
                "OrderNo",
                "Delivery Date",
                "Trip No",
                "Ship To Name",
                "Weight",
                "Volume",
                "Qty",
                "Arrival Time",
                "Item Note",
                "Pick Up",
                "PickUp Tel",
                "Trip Type",
                "Ship To Address",
                "Other Ref No2",
                "Other Ref No1",
                "POD Return Date",
                "POD Submit Date",
                "Submit ID",
                "Equipment Type",
                "Equipment Code",
                "Staff Name",
                "Mobile",
                "OwnerShip",
                "COD Amount",
                "Wave Priority",
                "Ship To Tel",
                "Request Group",
                "Request Truck Type",
                "Created Date",
                "Created User",
                "Trip Status",
                "Delivery Result",
                "Fail Reason",
                "Remark",
                "Vendor",
                "Equipment Desc",
                "Driver Desc",
                "District",
                "Province",
            ]
        )

        dataTableExpressOrder = get_Data_DB().dataExpressOrder()

        for row in range(
            len(dataTableExpressOrder)
        ):  # thêm check box vào ô đầu tiên cùa tabel
            checkbox_widget = QWidget()
            checkbox_layout = QVBoxLayout(checkbox_widget)
            checkbox_layout.addWidget(CheckBoxHeader())
            checkbox_layout.setAlignment(Qt.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_widget.setLayout(checkbox_layout)
            self.setCellWidget(row, 0, checkbox_widget)

            for value in dataTableExpressOrder:  # thêm dữ liệu vào table
                self.dataExpressOrder.append(value)
                self.setRowCount(len(dataTableExpressOrder))
                for i, rows in enumerate(dataTableExpressOrder):
                    for j, val in enumerate(rows):
                        self.setItem(i, j + 1, QTableWidgetItem(str(val)))
            self.verticalHeader().setDefaultSectionSize(50)
            self.horizontalHeader().setDefaultSectionSize(250)
            self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def get_selected_data(self):
        selected_rows = []
        for row in range(self.rowCount()):
            if self.cellWidget(row, 0).findChild(QCheckBox).isChecked():
                selected_rows.append(row)

        selected_data = []
        for row in selected_rows:
            row_data = [
                self.item(row, col).text() for col in range(1, self.columnCount())
            ]
            selected_data.append(row_data)
        return selected_data


class ui_Cluster(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data_Cluster = data
        self.setGeometry(0, 0, 800, 600)
       
        self.setWindowTitle("Cluster Data")
        layOut_UI = QVBoxLayout()

        self.text_show_data = QTextEdit()
        self.text_show_data.setStyleSheet("height:100px;color:green;font-weight:bold")

        showInput = """
        Data Input:
        {}
        """.format(
            str(data)
        )
        self.text_show_data.setText(showInput)

        # show Map
        map = folium.Map(
            location=[10.810468342398334, 106.66488939695603], zoom_start=13
        )
        self.dataMap = QtWebEngineWidgets.QWebEngineView()
        self.dataMap.setHtml(map.get_root().render())
        self.dataMap.resize(640, 600)
        self.dataMap.show()

        # add Layout:
        layOut_UI.addWidget(self.text_show_data)
        layOut_UI.addWidget(self.dataMap)

        self.setLayout(layOut_UI)
        self.show_Data_Cluster()

    def show_Data_Cluster(self):
        print("check value data clusster", self.data_Cluster)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)
        self.dataContact = []

        today = date.today()
        mainLayout = QVBoxLayout()
        tableFunLayout = QHBoxLayout()
        generalLayout = QGridLayout()
        labelOrderNO = QLabel("Order No")
        self.inputOrderNo = QLineEdit()
        self.inputOrderNo.setStyleSheet("height:40px")
        self.inputOrderNo.returnPressed.connect(self.searchDataOnPress)
        labelDeliveryDay = QLabel("Delivery Date")
        self.date_edit_now = QDateEdit()
        self.date_edit_now.editingFinished.connect(self.update)
        self.date_edit_now.setDate(today)
        self.date_edit_before = QDateEdit()
        self.date_edit_before.editingFinished.connect(self.update)
        self.date_edit_before.setDate(today)
        labelTripNo = QLabel("Trip No")
        inputTripNo = QLineEdit()
        inputTripNo.setStyleSheet("height:40px")
        labelContact = QLabel("Contact")
        datePickerCompleteDay = datePickerCompleteDate()
        datePickerCompleteDay.setStyleSheet("")
        self.cbContact = QComboBox(self)
        self.cbContact.setStyleSheet("font-size: 15px;height:40px")
        # call data add fill Combobox:
        for value in get_Data_DB().showDataContact():
            self.dataContact.append(value[0])
        self.cbContact.addItems(self.dataContact)

        self.btnSearch = QPushButton("Search")
        self.btnSearch.setStyleSheet("font-size:15px; width:10px; height:40px")
        self.btnSearch.clicked.connect(self.searchData)

        labelOrderStatus = QLabel("Order Status")
        self.cbOrderStatus = QComboBox(self)
        self.cbOrderStatus.setStyleSheet("font-size:15px; height:40px")
        self.cbOrderStatus.addItems(["New", "Processing", "Completed"])

        labelItemNote = QLabel("Item Note")
        self.inputItemNote = QLineEdit()
        self.inputItemNote.setStyleSheet("height:40px")
        self.btnBack = QPushButton("Back")
        self.btnBack.setStyleSheet("font-size:15px;width:10px;height:40px")
        # self.btnBack.clicked.connect(self.backMenu)

        self.btnGoData = QPushButton("Go")
        self.btnGoData.setStyleSheet("font-size:15px;width:10px;height:40px")
        self.btnGoData.clicked.connect(self.get_Data)

        generalLayout.addWidget(labelOrderNO, 0, 0)
        generalLayout.addWidget(self.inputOrderNo, 0, 1)
        generalLayout.addWidget(labelDeliveryDay, 0, 2)
        generalLayout.addWidget(self.date_edit_now, 0, 3)
        generalLayout.addWidget(self.date_edit_before, 0, 4)
        generalLayout.addWidget(self.btnGoData, 0, 5)
        generalLayout.addWidget(labelTripNo, 1, 0)
        generalLayout.addWidget(inputTripNo, 1, 1)
        generalLayout.addWidget(labelContact, 1, 2)
        generalLayout.addWidget(self.cbContact, 1, 3)
        generalLayout.addWidget(self.btnSearch, 1, 4)
        generalLayout.addWidget(labelOrderStatus, 2, 0)
        generalLayout.addWidget(self.cbOrderStatus, 2, 1)
        generalLayout.addWidget(labelItemNote, 2, 2)
        generalLayout.addWidget(self.inputItemNote, 2, 3)
        generalLayout.addWidget(self.btnBack, 2, 4)
        # Table
        self.table = TableWidget()

        tableFunLayout.addWidget(self.table)
        mainLayout.addLayout(generalLayout)
        mainLayout.addLayout(tableFunLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Express Order")

    def get_Data(self):
        selected_data = self.table.get_selected_data()
        if selected_data:
            self.show_UI = ui_Cluster(selected_data)
            self.show_UI.show()  # thiếu show UI center
        else:
            mb.showwarning(title="Notification", message="No Data Choose")

    # def backMenu(self):
    #     self.backOption=ViewOptionMenu()
    #     self.backOption.show()
    #     self.close()

    def searchData(self):
        valueContact = self.cbContact.currentText()
        valueTimeLeft = self.date_edit_now.date().toPyDate()
        valueTimeRight = self.date_edit_before.date().toPyDate()
        status = self.cbOrderStatus.currentText()
        textNote = self.inputItemNote.text()
        otherNo = self.inputOrderNo.text()
        data = []
        if status == "New" or status == "Processing":
            valueContact = self.cbContact.currentText()
            dataSearch = get_Data_DB.searchStatusOrder(valueContact, "PLAN")
            if len(dataSearch) == 0:
                mb.showwarning(title="Notification!!!", message="No Data")
            for value in dataSearch:
                data.append(value)
                self.table.setRowCount(len(dataSearch))
                for i, row in enumerate(data):
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))
        if status == "Completed":
            valueContact = self.cbContact.currentText()
            dataSearch = get_Data_DB.searchStatusOrder(valueContact, "COMPLETED")
            if len(dataSearch) == 0:
                mb.showwarning(title="Notification!!!", message="No Data")
            for value in dataSearch:
                data.append(value)
                self.table.setRowCount(len(dataSearch))
                for i, row in enumerate(data):
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))

    def searchDataOnPress(self):
        valueOrderNo = self.inputOrderNo.text()
        data = []
        row = 0
        if valueOrderNo:
            dataOrderSearch = get_Data_DB.showInfoOrderNo(valueOrderNo)
            for value in dataOrderSearch:
                data.append(value)
                self.table.setRowCount(1)
                for i, row in enumerate(data):  # mapping data list in table view get:
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            dataOrderSearch = get_Data_DB.dataExpressOrder()
            for value in dataOrderSearch:
                data.append(value)
                self.table.setRowCount(len(dataOrderSearch))
                for i, row in enumerate(data):
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))


optionMenu = QApplication(sys.argv)
optionMenu.setStyleSheet("QPushButton{font-size: 20px; width: 200px; height: 50px}")
viewOptionMenu = AppDemo()
viewOptionMenu.show()
sys.exit(optionMenu.exec_())
