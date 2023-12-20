import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
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
    QFileDialog,
    QFrame,
    QLabel,
    QCheckBox,
    QApplication,
    QDialog,
    QGroupBox,
)
from Process_Data.PyQT5_ClusterData import ClusterData
from PyQt5.QtCore import Qt, QFile, QTextStream
from UI.PyQT5_Dialog_Cluster import InputDialog
from Process_Data.PyQT5_Data import data_Proc
from PyQt5.QtGui import QColor, QIcon
from DB.Migration import get_Data_DB
from PyQt5 import QtCore, QtWidgets
from tkinter import messagebox as mb
from kneed import KneeLocator
from sklearn.cluster import KMeans
from datetime import date
import numpy as np
import pandas as pd
import ctypes
import datetime
import random
import os
import xlsxwriter

app = "MP.TMS_PLAN.TMS.1.0"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app)


class datePickerCompleteDate(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            "font-size: 25px ; padding-left: 20px ; padding-right:20px; padding-top:5px"
        )
        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.menuBar().setCornerWidget(self.dateedit, QtCore.Qt.TopLeftCorner)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateedit.dateChanged.connect(self.onDateChanged)

    def onDateChanged(self, qDate):
        print("check date {0}/{1}/{2}".format(qDate.day(), qDate.month(), qDate.year()))


class CheckBoxHeader(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    #     self.stateChanged.connect(self.check_all)

    # def set_checked(self, checked):
    #     self.setChecked(checked)

    # def check_all(self, state):
    #     if state == Qt.Checked:
    #         for checkbox in checkboxes:
    #             if checkbox != self:
    #                 checkbox.set_checked(True)


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 15)
        self.dataTriptype = []
        self.requestTruckType = []
        self.setHorizontalHeaderLabels(
            [
                "OrderNo",
                "PickUp",
                "Ship To Code",
                "Ship To Address",
                # "Trip Type",
                "Weight",
                "Volume",
                "Item Note",
                "Qty",
                "COD Amount",
                "Wave Priority",
                "Complete Date",
                "Request Group",
                "Request Truck Type",
                "Other Ref No1",
            ]
        )
        # Call query SQL Data
        for value in get_Data_DB().showDataTripType():
            self.dataTriptype.append(value[0])
        for value in get_Data_DB().showDataEquipType():
            self.requestTruckType.append(value[0])

        self.verticalHeader().setDefaultSectionSize(50)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.showDataTimePick()
        self.showCellTripType()
        self.showRequestType()

    def showCellTripType(self):
        self.cbTripType = QComboBox(self)
        self.cbTripType.setStyleSheet("font-size: 15px")
        self.cbTripType.addItems(self.dataTriptype)
        self.setCellWidget(0, 4, self.cbTripType)

    def showRequestType(self):
        self.cbRequestTypeNo = QComboBox(self)
        self.cbRequestTypeNo.setStyleSheet("font-size: 15px")
        self.cbRequestTypeNo.addItems(self.requestTruckType)
        self.setCellWidget(0, 13, self.cbRequestTypeNo)

    def showDataTimePick(self):
        self.datePickerCompleteDay = datePickerCompleteDate(self)
        self.setCellWidget(0, 11, self.datePickerCompleteDay)

    def showDataETP(self):
        self.dateETP = QDateEdit(calendarPopup=True)
        self.dateETP.setStyleSheet("font-size: 15px")
        self.dateETP.setDateTime(QtCore.QDateTime.currentDateTime())
        self.setCellWidget(0, 17, self.dateETP)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        self.showCellTripType()
        self.showRequestType()
        self.showDataTimePick()

    def _importFile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Excel File",
            "",
            "Excel Files (*.xlsx);;All Files (*)",
            options=options,
        )
        if file_path:
            try:
                self.setRowCount(0)
                rowCount = self.rowCount()
                self.insertRow(rowCount)
                df = pd.read_excel(file_path)
                self.displayDataInTable(df)
            except Exception as e:
                print(f"Error: {e}")

    def displayDataInTable(self, df):
        self.setRowCount(df.shape[0])
        self.setColumnCount(df.shape[1])
        self.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[row, col]))
                self.setItem(row, col, item)

    def getAndSaveDataFileTable(self):
        data = []
        for row in range(0, self.rowCount()):
            row_data = []
            for col in range(self.columnCount()):
                item = self.item(row, col)
                if item is not None:
                    row_data.append(item.text())
            data.append(row_data)
        print(data, len(data))
        self.setRowCount(0)

    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount() - 1)

    def _showDataOrder(self):
        self.setRowCount(0)
        self.setRowCount(1)
        self.setColumnCount(22)
        self.setHorizontalHeaderLabels(
            ["Action"]
            + [
                "Order ID",
                "OrderNo",
                "PickUp",
                "Ship To Code",
                "Ship To Address",
                # "Trip Type",
                "Weight",
                "Volume",
                "Item Note",
                "Qty",
                "COD Amount",
                "Wave Priority",
                "Complete Date",
                "Request Group",
                "Request Truck Type",
                "Other Ref No1",
                "Driver ID",
                "ETP",
                "ETA",
                "ATP",
                "ATD",
                "ATP",
            ]
        )
        data = []
        try:
            dataSearch = get_Data_DB().showDataImportFile()

            if dataSearch == None or dataSearch == "":
                mb.showwarning(title="Notification!!!", message="No Data")
            else:
                for row in range(len(dataSearch) + 1):
                    checkbox_widget = QWidget()
                    checkbox_layout = QVBoxLayout(checkbox_widget)
                    checkbox_layout.addWidget(CheckBoxHeader())
                    checkbox_layout.setAlignment(Qt.AlignCenter)
                    checkbox_layout.setContentsMargins(0, 0, 0, 0)
                    checkbox_widget.setLayout(checkbox_layout)
                    self.setCellWidget(row, 0, checkbox_widget)

                    for value in dataSearch:
                        data.append(value)
                        self.setRowCount(len(dataSearch) + 1)

                for i, rows in enumerate(data):
                    for j, val in enumerate(rows):
                        self.setItem(i + 1, j + 1, QTableWidgetItem(str(val)))
            self.verticalHeader().setDefaultSectionSize(50)
            self.horizontalHeader().setDefaultSectionSize(250)
            self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        except ValueError as error:
            print("Log-Error", error)

    def get_UI_Select(self, d):
        print("")

    def get_selected_data(self):
        selected_rows = []
        for row in range(self.rowCount()):
            if self.cellWidget(row, 0).findChild(QCheckBox).isChecked():
                selected_rows.append(row)
        selected_data = []
        if selected_rows == [0]:
            # CheckBoxHeader(QCheckBox).setChecked(True)
            for row in range(1, self.rowCount()):
                row_data = []
                for col in range(self.columnCount()):
                    item = self.item(row, col)
                    if item:
                        row_data.append(item.text())
                selected_data.append(row_data)
            return selected_data
        else:
            for row in selected_rows:
                row_data = [
                    self.item(row, col).text() for col in range(1, self.columnCount())
                ]
                selected_data.append(row_data)
            return selected_data

    def _copyRow(self):
        self.insertRow(self.rowCount())
        rowCount = self.rowCount()
        columnCount = self.columnCount()

        for j in range(columnCount):
            if not self.item(rowCount - 2, j) is None:
                self.setItem(
                    rowCount - 1, j, QTableWidgetItem(self.item(rowCount - 2, j).text())
                )

    def clearData(self):
        for item in self.selectedItems():
            item.setText("")

    def _saveRowData(self):
        mb.showinfo(title="Notification", message="Add Data")


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.dataContact = []
        today = date.today()
        mainLayout = QVBoxLayout()
        group_Menu = QGroupBox("Menu")
        tableFunLayout = QHBoxLayout()
        content_Menu = QHBoxLayout()

        labelOrderNO = QLabel("Order No:")
        labelOrderNO.setStyleSheet("font-size:15px")
        labelContact = QLabel("Contact:")
        labelContact.setStyleSheet("font-size:15px")

        labelDeliveryDay = QLabel("Delivery Date:")
        labelDeliveryDay.setStyleSheet("font-size:15px")

        self.checkAutoGennerated = QCheckBox("Auto Generated")
        self.checkAutoGennerated.setStyleSheet("font-size:15px")
        self.checkAutoGennerated.stateChanged.connect(self.handleOnChangeAuto)

        self.checkGenerated = QCheckBox("Generated Trip and Complete")
        self.checkGenerated.setStyleSheet("font-size:15px")
        self.checkGenerated.stateChanged.connect(self.handleOnChangeGenerated)

        # datePickerCompleteDay = datePickerCompleteDate()

        cbContact = QComboBox(self)
        cbContact.setFixedWidth(200)
        cbContact.setFixedHeight(30)

        for value in get_Data_DB().showDataContact():
            self.dataContact.append(value[0])

        date_edit_now = QDateEdit()
        date_edit_now.setFixedHeight(30)
        date_edit_now.setFixedWidth(100)
        date_edit_now.editingFinished.connect(self.update)

        self.btnBack = QPushButton("Back")
        self.btnGoData = QPushButton("Show Map")
        self.btnGoData.clicked.connect(self.get_Data)

        date_edit_now.setDate(today)
        cbContact.addItems(self.dataContact)

        content_Menu.addWidget(labelContact)
        content_Menu.addWidget(cbContact)
        content_Menu.addSpacing(100)
        content_Menu.addWidget(labelDeliveryDay)
        content_Menu.addWidget(date_edit_now)
        content_Menu.addSpacing(100)
        content_Menu.addWidget(self.checkAutoGennerated)
        content_Menu.addSpacing(100)
        content_Menu.addWidget(self.checkGenerated)
        # content_Menu.addWidget(self.btnBack)
        content_Menu.addStretch(1)
        content_Menu.addWidget(self.btnGoData)

        group_Menu.setLayout(content_Menu)
        group_Menu.setFixedHeight(100)

        self.table = TableWidget()
        tableFunLayout.addWidget(self.table)
        buttonLayout = QVBoxLayout()
        button_new = QPushButton("New")
        button_new.clicked.connect(self.table._addRow)
        buttonLayout.addWidget(button_new)

        button_copy = QPushButton("Copy")
        button_copy.clicked.connect(self.table._copyRow)
        button_copy.setDisabled(True)
        buttonLayout.addWidget(button_copy)

        button_save = QPushButton("Add Data")
        button_save.setDisabled(True)
        button_save.clicked.connect(self.table._saveRowData)
        buttonLayout.addWidget(button_save)

        button_importCSV = QPushButton("Import File")
        button_importCSV.clicked.connect(self.table._importFile)
        buttonLayout.addWidget(button_importCSV)

        button_remove = QPushButton("Remove")
        button_remove.clicked.connect(self.table._removeRow)
        button_remove.setDisabled(True)
        buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)

        button_showDataOrder = QPushButton("Show Data")
        button_showDataOrder.clicked.connect(self.table._showDataOrder)
        buttonLayout.addWidget(button_showDataOrder)

        button_save = QPushButton("Save")
        button_save.clicked.connect(self.table.getAndSaveDataFileTable)
        buttonLayout.addWidget(button_save)

        tableFunLayout.addLayout(buttonLayout)
        # mainLayout.addLayout(generalLayout)
        mainLayout.addWidget(group_Menu)
        mainLayout.addLayout(tableFunLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Express Order Detail")
        self.set_Style()
        self.showMaximized()
        icon = QIcon("logo.ico")  # Thay đổi đường dẫn tới biểu tượng của bạn
        self.setWindowIcon(icon)

    def set_Style(self):
        self.btnBack.setFixedHeight(30)
        self.btnGoData.setFixedHeight(50)
        self.btnGoData.setFixedWidth(200)

    def handleOnChangeAuto(self):
        self.valueChange = self.checkAutoGennerated.isChecked()

    def handleOnChangeGenerated(self, state):
        if state:
            self.table.setColumnCount(23)
            self.table.setHorizontalHeaderLabels(
                [
                    "OrderNo",
                    "PickUp",
                    "Ship To Code",
                    "Ship To Address",
                    "Trip Type",
                    "Weight",
                    "Volume",
                    "Item Note",
                    "Qty",
                    "COD Amount",
                    "Wave Priority",
                    "Complete Date",
                    "Request Group",
                    "Request Truck Type",
                    "Other Ref No1",
                    "Equipment Code",
                    "Driver Id",
                    "ETP",
                    "ETA",
                    "ATD",
                    "ATA",
                    "Vendor",
                    "Driver Desc",
                ]
            )
            self.table.showDataETP()
        else:
            self.table.setColumnCount(15)
            self.table.setHorizontalHeaderLabels(
                [
                    "OrderNo",
                    "PickUp",
                    "Ship To Code",
                    "Ship To Address",
                    "Trip Type",
                    "Weight",
                    "Volume",
                    "Item Note",
                    "Qty",
                    "COD Amount",
                    "Wave Priority",
                    "Complete Date",
                    "Request Group",
                    "Request Truck Type",
                    "Other Ref No1",
                ]
            )
    def suggest_Cluster(self,data,input):
        order=[]
        for value in data:
            order.append(value[2])
        data_Select = get_Data_DB().data_Select(order)
        data_ = data_Proc().get_Data(data_Select)
        print('check value data suggest',data_)
        num_Cluster=self.convent_Suggest(data_)
        input.setText(str(num_Cluster))
    def convent_Suggest(self,data):
        sse = []
        arr_ = np.array(
            [
                [
                    float(item[5]),
                    float(item[6]),
                ]
                for item in data
            ]
        ).tolist()
        k_values = range(1, len(arr_) - 1)
        for k in k_values:
            kmeans = KMeans(n_clusters=k)
            kmeans.fit(arr_)
            sse.append(kmeans.inertia_)
        kl = KneeLocator(k_values, sse, curve="convex", direction="decreasing")
        optimal_k = int(kl.elbow)
        return optimal_k
    def show_Map(self,data,equipment,cluster):
        if len(data) == 0:
            mb.showwarning(title="Notification!!!", message="No Data")
        elif len(data) <= 4:
            mb.showwarning(title="Notification!!!", message="At least five data")
        elif len(data) >= 5 and len(data) < 10:
            ClusterData(data, self, 0, equipment)
            self.showMinimized()
        else:
            ClusterData(data, self, int(cluster), equipment)
            self.showMinimized()
    def get_Data(self):
        try:
            selected_data = self.table.get_selected_data()
            input_dialog = InputDialog(self)
            input_dialog.btn_Suggest.clicked.connect(lambda:self.suggest_Cluster(selected_data,input_dialog.input_Cluster))
            if input_dialog.exec_() == QDialog.Accepted:
                num_Cluster = input_dialog.input_Cluster.text()
                equipment = input_dialog.cb_Equipment_Type.currentText()[:-1]
                type_Equipment = float(equipment) * 1000
                
            self.show_Map(selected_data,type_Equipment,num_Cluster)
        except ValueError as e:
            print("Log Error", e)



menu_UI = QApplication(sys.argv)
menu_UI.setStyleSheet("QPushButton{font-size: 20px; width: 200px; height: 50px}")
view_UI = AppDemo()
view_UI.show()
sys.exit(menu_UI.exec_())
