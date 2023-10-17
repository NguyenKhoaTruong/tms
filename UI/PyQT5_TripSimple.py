import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQT5_OptionMenu import ViewOptionMenu
from PyQt5.QtWidgets import (
    QWidget,
    QHeaderView,
    QPushButton,
    QTableWidget,
    QComboBox,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QDateEdit,
    QLabel,
    QLineEdit,
    QGridLayout,
)
from ..DB.Migration import (
    showDataContact,
    searchTripSimple,
    findDataTripOrder,
    showDataTripOrder,
    findDataTripOrder,
)
from PyQt5 import QtCore, QtWidgets
from tkinter import messagebox as mb
from datetime import date


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


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 23)
        self.setHorizontalHeaderLabels(
            [
                "Trip No",
                "Batch Group No",
                "Batch Group",
                "Equipment Type",
                "ETP",
                "Ownership",
                "Porter",
                "Driver",
                "Equipment Code",
                "Equipment Desc",
                "Order No",
                "Qty",
                "Weight",
                "Volume",
                "Trip Memo",
                "Pick Up Date",
                "Start Date",
                "End Date",
                "Delivery Result",
                "Fail Reason",
                "Other Note",
                "Created Date",
                "Create User",
                "Updated Date",
                "Update User",
                "ETD",
                "ETA",
                "Pass Code",
                "Trip Status",
                "Driver Mobile No",
                "Staging",
                "Vendor",
                "Link Up Trip No",
                "Loading End",
                "Loading Start",
            ]
        )
        self.verticalHeader().setDefaultSectionSize(50)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)


class ViewTripSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.row = 0
        self.dataContact = []
        today = date.today()
        mainLayout = QVBoxLayout()
        tableFunLayout = QHBoxLayout()
        generalLayout = QGridLayout()

        self.date_edit_now = QDateEdit()
        self.date_edit_now.editingFinished.connect(self.update)
        self.date_edit_now.setDate(today)
        self.date_edit_before = QDateEdit()
        self.date_edit_before.editingFinished.connect(self.update)
        self.date_edit_before.setDate(today)

        labelTripNo = QLabel("Trip No")
        self.inputTripNo = QLineEdit()
        self.inputTripNo.setStyleSheet("height:40px")
        self.inputTripNo.returnPressed.connect(self.showDataOnPressValueSearch)

        label_ETP = QLabel("ETP")
        labelOrderNo = QLabel("Order No")
        self.inputOrderNo = QLineEdit()
        self.inputOrderNo.setStyleSheet("height:40px")
        self.inputOrderNo.returnPressed.connect(self.showDataOnPressValueSearch)

        labelContacts = QLabel("Contacts")

        self.cbContact = QComboBox(self)
        self.cbContact.setStyleSheet("font-size: 15px; height:40px")

        for value in showDataContact():  # call data add fill Combobox:
            self.dataContact.append(value[0])
        self.cbContact.addItems(self.dataContact)

        self.btnSearch = QPushButton("Search")
        self.btnSearch.setStyleSheet("font-size:15px;width:10px;height:40px")
        self.btnSearch.clicked.connect(self.searchData)

        self.btnBackOption = QPushButton("Back Menu")
        self.btnBackOption.setStyleSheet("font-size:15px; width:10px;height:40px")
        self.btnBackOption.clicked.connect(self.backHomeMenu)

        generalLayout.addWidget(labelTripNo, 0, 0)
        generalLayout.addWidget(self.inputTripNo, 0, 1)
        generalLayout.addWidget(label_ETP, 0, 2)
        generalLayout.addWidget(self.date_edit_now, 0, 3)
        generalLayout.addWidget(self.date_edit_before, 0, 4)
        generalLayout.addWidget(labelOrderNo, 1, 0)
        generalLayout.addWidget(self.inputOrderNo, 1, 1)
        generalLayout.addWidget(labelContacts, 2, 0)
        generalLayout.addWidget(self.cbContact, 2, 1)
        generalLayout.addWidget(self.btnBackOption, 2, 4)
        generalLayout.addWidget(self.btnSearch, 2, 3)

        self.table = TableWidget()  # Table
        tableFunLayout.addWidget(self.table)
        mainLayout.addLayout(generalLayout)
        mainLayout.addLayout(tableFunLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Trip Simple")
        self.resize(1600, 600)

    def backHomeMenu(self):
        self.viewOption = ViewOptionMenu()
        self.viewOption.show()
        self.close()

    def searchData(self):
        valueContact = self.cbContact.currentText()
        valueTimeLeft = self.date_edit_now.date().toPyDate()
        valueTimeRight = self.date_edit_before.date().toPyDate()
        data = []
        if valueContact and valueTimeLeft and valueTimeRight:
            dataSearch = searchTripSimple(valueContact, valueTimeLeft, valueTimeRight)
            if not dataSearch:
                mb.showwarning(title="Notification!!!", message="No Data")
            for value in dataSearch:
                data.append(value)
                self.table.setRowCount(len(dataSearch))
                for i, row in enumerate(data):
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))

    def showDataOnPressValueSearch(self):
        valueTripNo = self.inputTripNo.text()
        data = []
        row = 0
        # set Data
        if valueTripNo:
            dataTripSearch = findDataTripOrder(valueTripNo)
            for value in dataTripSearch:
                data.append(value)
                self.table.setRowCount(1)
                # mapping data list in table view get:
                for i, row in enumerate(data):
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            dataTripSearch = showDataTripOrder()
            for value in dataTripSearch:
                data.append(value)
                self.table.setRowCount(len(dataTripSearch))
                for i, row in enumerate(data):
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))

    def showDataOnPressValueOrderNo(self):
        valueOrderNo = self.inputOrderNo.text()
        data = []
        row = 0
        if valueOrderNo:
            dataOrderSearch = findDataTripOrder(valueOrderNo)
            for value in dataOrderSearch:
                data.append(value)
                self.table.setRowCount(1)
                for i, row in enumerate(data):
                    for j, val in enumerate(row):
                        self.table.setItem(i, j, QTableWidgetItem(str(val)))
