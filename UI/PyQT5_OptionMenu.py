import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QGridLayout
from  PyQT5_TripSimple import ViewTripSimple
from  PyQT5_SimpleTripDetail import ViewTripSimpleDetail
from  PyQT5_ExpressOrder import AppDemo
from  PyQT5_ExpressOrderDetail import AppDemo
class ViewOptionMenu(QWidget):
   def __init__(self):
        super().__init__()
        self.resize(1600, 600)
        mainLayout = QVBoxLayout()
        generalLayout=QGridLayout()
        btnSimpleStrip = QPushButton("Simple Trip")
        btnSimpleStrip.setGeometry(200, 150, 100, 30)
        btnSimpleStrip.clicked.connect(self.clickSimpleTrip)
        
        btnSimpleStripDetail=QPushButton('Simple Trip Detail')
        btnSimpleStripDetail.setGeometry(200,150,100,30)
        btnSimpleStripDetail.clicked.connect(self.clickSimpleTripDetail)
        
        btnExpressOrder = QPushButton("Express Order")
        btnExpressOrder.setGeometry(200, 150, 100, 30)
        btnExpressOrder.clicked.connect(self.clickExpressOrder)
        
        btnExpressOrderDetail=QPushButton('Express Order Detail')
        btnExpressOrderDetail.setGeometry(200,150,100,30)
        btnExpressOrderDetail.clicked.connect(self.clickExpressOrderDetail)
        
        generalLayout.addWidget(btnSimpleStrip,0,0)
        generalLayout.addWidget(btnSimpleStripDetail,0,1)
        generalLayout.addWidget(btnExpressOrder,1,0)
        generalLayout.addWidget(btnExpressOrderDetail,1,1)
        
        mainLayout.addLayout(generalLayout) 
        self.setLayout(mainLayout)
        self.setWindowTitle('Option Menu')
   def clickSimpleTrip(self):
      self.viewTrip=ViewTripSimple()
      self.viewTrip.show()
      self.close()
   def clickSimpleTripDetail(self):
      self.viewTripDetail=ViewTripSimpleDetail()
      self.viewTripDetail.show()
      self.close()
   def clickExpressOrder(self):
      self.viewExpress=AppDemo()
      self.viewExpress.show()
      self.close()
   def clickExpressOrderDetail(self):
      self.viewExpressDetail=AppDemo()
      self.viewExpressDetail.show()
      self.close()
optionMenu = QApplication(sys.argv)
optionMenu.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}')   
viewOptionMenu = ViewOptionMenu()
viewOptionMenu.show()
sys.exit(optionMenu.exec_())