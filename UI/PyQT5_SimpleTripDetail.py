from .PyQT5_OptionMenu import ViewOptionMenu
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
    QDesktopWidget,
    QLabel,
    QLineEdit,
    QDoubleSpinBox,
    QGroupBox,
    QPlainTextEdit,
    QGridLayout,
)
from PyQt5.QtCore import Qt, pyqtSignal, QObject, pyqtSlot
from ..DB.Migration import (
    showDataTableEquipment,
    showDataContact,
    showDataTripPickUpAndShipTo,
    showDataTripType,
    checkOrderNo,
    checkTrip,
    checkTripNo,
    addTripSimpleDL,
    addOrderSimple,
    showDataEquipmentGroupTrip,
)
from PyQt5 import QtCore, QtWidgets
import random
import datetime
from datetime import date
from tkinter import messagebox as mb


class Communicate(QObject):
    mysignal = pyqtSignal(str)


class datePickerCompleteDate(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            "font-size: 25px ; padding-left: 20px ; padding-right:20px; padding-top:5px; background-color:none"
        )
        self.date = QtWidgets.QDateEdit(calendarPopup=True)
        self.menuBar().setCornerWidget(self.date, QtCore.Qt.TopLeftCorner)
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date.dateChanged.connect(self.onDateChanged)

    def onDateChanged(self, qDate):
        print("check date {0}/{1}/{2}".format(qDate.day(), qDate.month(), qDate.year()))


class TableWidget(QTableWidget):
    item_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__(1, 7)
        self.dataEquimentTrip = []
        self.dataEquipmentCode = ""
        self.setHorizontalHeaderLabels(
            [
                "Equipment Decs",
                "Equip Type No",
                "Staff Name",
                "Trips",
                "Pending Trips",
                "Staff User ID",
                "Default Staff ID",
            ]
        )
        dataEquipment = showDataTableEquipment()
        for value in dataEquipment:
            self.dataEquimentTrip.append(value)
            for i, row in enumerate(self.dataEquimentTrip):
                for j, val in enumerate(row):
                    self.setRowCount(len(dataEquipment))
                    self.setItem(i, j, QTableWidgetItem(str(val)))
        self.verticalHeader().setDefaultSectionSize(50)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.cellClicked.connect(self.get_row)
        # focus data table and get value table

    def get_row(self, row, column):
        self.row_items = []
        for i in range(self.columnCount()):
            item = self.item(row, i)
            if item != None:
                self.row_items.append(item.text())
        print(f"Row {row}:", self.row_items, self.row_items[0])
        self.dataEquipmentCode = self.row_items[0]
        # sending data
        dataQ = self.dataEquipmentCode
        self.item_selected.emit(dataQ)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount() - 1)

    def _copyRow(self):
        self.insertRow(self.rowCount())
        rowCount = self.rowCount()
        columnCount = self.columnCount()

        for j in range(columnCount):
            if not self.item(rowCount - 2, j) is None:
                self.setItem(
                    rowCount - 1, j, QTableWidgetItem(self.item(rowCount - 2, j).text())
                )

    def _saveRowData(self):
        self.wintwo = uiTripSample()
        self.wintwo.inputEquipmentCode.setText(self.row_items[0])
        self.wintwo.driverId.setText(self.row_items[3])
        self.wintwo.equipmentTypeNo.setText(self.row_items[1])
        self.wintwo.move_to_center()
        self.wintwo.show()

    def showFormAddTrip(self):
        self.wntwo = uiTripSample()
        self.wntwo.move_to_center()
        self.wntwo.show()


class uiTripSample(QWidget):
    def __init__(self):
        super().__init__()
        self.dataContact = []
        self.dataPickUp = []
        self.dataShipTo = []
        self.dataTripType = []
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Trip Simple")
        tableFunLayout = QVBoxLayout()
        gridTrip = QGridLayout()

        labelContact = QLabel("Contact")
        self.cbContact = QComboBox(self)
        self.cbContact.setStyleSheet("font-size: 15px; height:40px")
        for value in showDataContact():
            self.dataContact.append(value[0])
        self.cbContact.addItems(self.dataContact)

        labelEquipmentCode = QLabel("Equipment Code")
        self.inputEquipmentCode = QLineEdit()
        self.inputEquipmentCode.setStyleSheet("height:40px")
        ##
        self.driverId = QLineEdit()
        self.equipmentTypeNo = QLineEdit()
        ##

        labelShipTopAddress = QLabel("Ship To Address")
        self.inputShipToAddress = QPlainTextEdit()
        self.inputShipToAddress.move(10, 10)
        self.inputShipToAddress.resize(5, 5)

        labelVolum = QLabel("Volume")
        self.inputVolume = QLineEdit()
        self.inputVolume.setStyleSheet("height:40px")

        labelItemNote = QLabel("Item Note")
        self.inputItemNote = QPlainTextEdit()
        self.inputItemNote.move(10, 10)
        self.inputItemNote.resize(5, 5)

        labelPikUp = QLabel("Pick Up")
        self.cbPickUp = QComboBox(self)
        self.cbPickUp.setStyleSheet("font-size: 15px; height:40px")
        for value in showDataTripPickUpAndShipTo():
            self.dataPickUp.append(value[0])
        self.cbPickUp.addItems(self.dataPickUp)

        labelShipTo = QLabel("Ship To")
        self.cbShipTo = QComboBox(self)
        self.cbShipTo.setStyleSheet("font-size: 15px; height:40px")
        for value in showDataTripPickUpAndShipTo():
            self.dataShipTo.append(value[0])
        self.cbShipTo.addItems(self.dataShipTo)

        labelTripType = QLabel("Trip Type")
        self.cbTripType = QComboBox(self)
        self.cbTripType.setStyleSheet("font-size: 15px; height:40px")
        for value in showDataTripType():
            self.dataTripType.append(value[0])
        self.cbTripType.addItems(self.dataTripType)

        labelWeight = QLabel("Weight")
        self.inputWeight = QLineEdit()
        self.inputWeight.setStyleSheet("height:40px")
        labelQty = QLabel("Qty")
        self.inputQty = QLineEdit()
        self.inputQty.setStyleSheet("height:40px")
        labelTrip = QLabel("Trips")
        self.inputTrips = QLineEdit()
        self.inputTrips.setStyleSheet("height:40px")

        btnSave = QPushButton("Save")
        btnSave.clicked.connect(self.saveTripSimple)

        gridTrip.addWidget(labelContact, 0, 0)
        gridTrip.addWidget(self.cbContact, 0, 1)
        gridTrip.addWidget(labelEquipmentCode, 0, 2)
        gridTrip.addWidget(self.inputEquipmentCode, 0, 3)
        gridTrip.addWidget(labelPikUp, 1, 0)
        gridTrip.addWidget(self.cbPickUp, 1, 1)
        gridTrip.addWidget(labelShipTopAddress, 1, 2)
        gridTrip.addWidget(self.inputShipToAddress, 1, 3)
        gridTrip.addWidget(labelShipTo, 2, 0)
        gridTrip.addWidget(self.cbShipTo, 2, 1)
        gridTrip.addWidget(labelTripType, 3, 0)
        gridTrip.addWidget(self.cbTripType, 3, 1)
        gridTrip.addWidget(labelVolum, 3, 2)
        gridTrip.addWidget(self.inputVolume, 3, 3)
        gridTrip.addWidget(labelWeight, 4, 0)
        gridTrip.addWidget(self.inputWeight, 4, 1)
        gridTrip.addWidget(labelItemNote, 4, 2)
        gridTrip.addWidget(self.inputItemNote, 4, 3)
        gridTrip.addWidget(labelQty, 5, 0)
        gridTrip.addWidget(self.inputQty, 5, 1)
        gridTrip.addWidget(labelTrip, 6, 0)
        gridTrip.addWidget(self.inputTrips, 6, 1)
        gridTrip.addWidget(btnSave, 7, 3)

        tableFunLayout.addLayout(gridTrip)
        self.setLayout(tableFunLayout)

    def move_to_center(self):
        rect = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(center_point)
        self.move(rect.topLeft())

    def closeWindow(self):
        self.destroy(destroyWindow=True)

    def saveTripSimple(self):
        # get value combobox
        CreateUser = "TEST"
        tripStatus = "PLAN"
        priority = 99
        cod = 0.0
        splitOrderIndex = 0
        isUse = 1
        codAmount = 0.00000
        DCCode = "DNA01"

        random_numbers = "".join([str(random.randint(1, 9)) for _ in range(10)])
        orderNo = "S{}".format(str(random_numbers))
        # check data order no
        dataCheckOrderNo = checkOrderNo(orderNo)
        if dataCheckOrderNo == orderNo:
            valuie = int(random_numbers) + 1
            orderNo = "S{}".format(str(valuie))

        contact = self.cbContact.currentText()
        equipmentCode = self.inputEquipmentCode.text()
        pickUp = self.cbPickUp.currentText()
        shipToAddress = self.inputShipToAddress.toPlainText()
        shipTo = self.cbShipTo.currentText()
        tripType = self.cbTripType.currentText()
        volumne = self.inputVolume.text()
        weight = self.inputWeight.text()
        itemNote = self.inputItemNote.toPlainText()
        qty = self.inputQty.text()
        trips = self.inputTrips.text()
        driverId = self.driverId.text()
        equipmentTypeNo = self.equipmentTypeNo.text()
        today = date.today()
        time_now = datetime.datetime.now().time()
        ETP = datetime.datetime.combine(today, time_now)
        ETA = ETP + datetime.timedelta(minutes=20)
        CreateDate = ETP + datetime.timedelta(minutes=1)

        # exeption
        TripNo = "S{}".format(str(random_numbers))
        dataCheckTripNo = checkTrip(TripNo)
        if dataCheckTripNo:
            tripNoBefore = checkTripNo()
            if tripNoBefore:
                value = int(tripNoBefore[1:11]) + 1
                TripNo = "S{}".format(str(value))
            try:
                addTripSimpleDL(
                    TripNo,
                    ETP.__format__("%Y-%m-%d %H:%M:%S"),
                    ETA.__format__("%Y-%m-%d %H:%M:%S"),
                    CreateDate.__format__("%Y-%m-%d %H:%M:%S"),
                    CreateUser,
                    qty,
                    equipmentCode,
                    equipmentCode,
                    driverId,
                    tripStatus,
                    DCCode,
                    equipmentTypeNo,
                    codAmount,
                )
                addOrderSimple(
                    orderNo,
                    float(weight),
                    float(volumne),
                    shipTo,
                    shipToAddress,
                    ETA.__format__("%Y-%m-%d %H:%M:%S"),
                    priority,
                    ETP.__format__("%Y-%m-%d %H:%M:%S"),
                    TripNo,
                    DCCode,
                    "NABATI",
                    codAmount,
                    CreateUser,
                    isUse,
                    splitOrderIndex,
                    tripType,
                    qty,
                    pickUp,
                    cod,
                    itemNote,
                )
                mb.showinfo(title="Notification", message="Add Trip Success")
                self.close()
            except ValueError as error:
                print("Log Error", error)
        else:
            try:
                addTripSimpleDL(
                    TripNo,
                    ETP.__format__("%Y-%m-%d %H:%M:%S"),
                    ETA.__format__("%Y-%m-%d %H:%M:%S"),
                    CreateDate.__format__("%Y-%m-%d %H:%M:%S"),
                    CreateUser,
                    qty,
                    equipmentCode,
                    equipmentCode,
                    driverId,
                    tripStatus,
                    DCCode,
                    equipmentTypeNo,
                    codAmount,
                )
                addOrderSimple(
                    orderNo,
                    float(weight),
                    float(volumne),
                    shipTo,
                    shipToAddress,
                    ETA.__format__("%Y-%m-%d %H:%M:%S"),
                    priority,
                    ETP.__format__("%Y-%m-%d %H:%M:%S"),
                    TripNo,
                    DCCode,
                    "NABATI",
                    codAmount,
                    CreateUser,
                    isUse,
                    splitOrderIndex,
                    tripType,
                    qty,
                    pickUp,
                    cod,
                    itemNote,
                )
                mb.showinfo(title="Notification", message="Add Trip Success")
                self.close()
            except ValueError as error:
                print("Log Error", error)


class ViewTripSimpleDetail(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)
        self.dataContact = []
        self.tableView = TableWidget()
        self.tableView.item_selected.connect(self.on_item_selected)

        mainLayout = QVBoxLayout()
        self.date = QDateEdit(calendarPopup=True)
        self.date.setStyleSheet("width: 200px ; height: 50px")
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())

        searchGroup = QGroupBox("Search")
        gridSearch = QGridLayout()
        searchGroup.setLayout(gridSearch)
        labelDeliveryDate = QLabel("Delivery Date:")

        data = TableWidget()
        self.dataEquipmentGroup = data.dataEquimentTrip

        labelEquipmentGroup = QLabel("Equipment Group:")
        self.cbEquipmentGroup = QComboBox(self)
        self.cbEquipmentGroup.setStyleSheet(
            "font-size: 15px; width:100px ;height:40px; float:left"
        )
        for value in showDataEquipmentGroupTrip():
            self.dataContact.append(value[0])
        self.cbEquipmentGroup.addItems(self.dataContact)
        self.btnBackMenu = QPushButton("Back")
        self.btnBackMenu.setStyleSheet("font-size:15px;height:50px")
        self.btnBackMenu.clicked.connect(self.goOptionMenu)
        gridSearch.addWidget(labelDeliveryDate, 0, 0)
        gridSearch.addWidget(self.date, 0, 1)
        gridSearch.addWidget(labelEquipmentGroup, 0, 2)
        gridSearch.addWidget(self.cbEquipmentGroup, 0, 3)
        gridSearch.addWidget(self.btnBackMenu, 0, 4)

        tableFunLayout = QHBoxLayout()
        date_edit_now = QDateEdit()
        date_edit_now.editingFinished.connect(self.update)
        date_edit_before = QDateEdit()
        date_edit_before.editingFinished.connect(self.update)
        # Table
        self.table = TableWidget()
        table = TableWidget()
        tableFunLayout.addWidget(table)
        buttonLayout = QVBoxLayout()
        gridSpinTime = QGridLayout()
        labelSelect = QLabel("Selected Equipment")
        self.inputSelect = QLineEdit()
        if self.dataEquipmentGroup != None:
            self.inputSelect.setText(self.dataEquipmentGroup[0][0])
        labelTripMemo = QLabel("Trip Memo")
        inputTripMemo = QPlainTextEdit()
        inputTripMemo.move(10, 10)
        inputTripMemo.resize(10, 10)
        # Use Spinbox
        labelTimeTrip = QLabel("Arrival/ Deparrt / ETA")
        # frameSpinBox=QGridLayout()
        buttonLayout.addWidget(labelSelect)
        buttonLayout.addWidget(self.inputSelect)
        buttonLayout.addWidget(labelTripMemo)
        buttonLayout.addWidget(inputTripMemo)
        buttonLayout.addWidget(labelTimeTrip)
        # buttonLayout.addWidget(frameSpinBox)

        spinArrival = QDoubleSpinBox()
        spinArrival.setGeometry(100, 100, 100, 40)
        spinArrival.setValue(10)
        spimDepart = QDoubleSpinBox()
        spimDepart.setGeometry(100, 100, 100, 40)
        spimDepart.setValue(10)
        spinATA = QDoubleSpinBox()
        spinATA.setGeometry(100, 100, 100, 40)
        spinATA.setValue(10)

        gridSpinTime.addWidget(spinArrival, 0, 0)
        gridSpinTime.addWidget(spimDepart, 0, 1)
        gridSpinTime.addWidget(spinATA, 0, 2)
        buttonLayout.addLayout(gridSpinTime)
        # frameSpinBox.addWidget(spimDepart,0,2)
        # # buttonLayout.addWidget(formSpinbox)
        button_new = QPushButton("New Trip Individual")
        button_new.setDisabled(True)
        button_new.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_new)

        button_copy = QPushButton("New Trip Add One")
        button_copy.setDisabled(True)
        button_copy.clicked.connect(table._copyRow)
        buttonLayout.addWidget(button_copy)

        button_save = QPushButton("Add Simple Trip")
        button_save.clicked.connect(table._saveRowData)
        buttonLayout.addWidget(button_save)

        button_remove = QPushButton("Assign To Trip")
        button_remove.setDisabled(True)
        button_remove.clicked.connect(table._removeRow)
        buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)
        tableFunLayout.addLayout(buttonLayout)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(searchGroup)
        mainLayout.addLayout(tableFunLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Trip Simple Detail")

    @pyqtSlot(str)
    def on_item_selected(self, data):
        self.inputSelect.setText(data)

    def goOptionMenu(self):
        self.optionMenu = ViewOptionMenu()
        self.optionMenu.show()
        self.close()
