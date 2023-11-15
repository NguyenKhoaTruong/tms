import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
    QLineEdit,
    QDialogButtonBox,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QComboBox,
    QPushButton
)
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtCore import Qt
import UI.css_UI as css


class InputDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__()
        self.setWindowTitle("Add Cluster")

        layout = QVBoxLayout()
        layout_Input = QHBoxLayout()
        layout_Type = QHBoxLayout()

        label_Cluster = QLabel("Number Cluster:")
        label_Cluster.setStyleSheet("font-size:15px")
        
        self.btn_Suggest=QPushButton("Suggest",self)

        label_Equipment_Type = QLabel("Equipment Type:")
        label_Equipment_Type.setStyleSheet("font-size:15px")

        self.cb_Equipment_Type = QComboBox()
        self.cb_Equipment_Type.setStyleSheet("font-size:15px")
        self.cb_Equipment_Type.setFixedWidth(310)
        self.cb_Equipment_Type.addItem("5T")
        self.cb_Equipment_Type.addItem("10T")
        self.cb_Equipment_Type.addItem("15T")
        self.cb_Equipment_Type.addItem("20T")

        self.input_Cluster = QLineEdit(self)
        self.input_Cluster.setFixedHeight(30)
        self.input_Cluster.setText("10")
        self.input_Cluster.setStyleSheet("font-size:15px")
        self.input_Cluster.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_Input.addWidget(label_Cluster)
        layout_Input.addWidget(self.input_Cluster)
        layout_Input.addWidget(self.btn_Suggest)
        layout_Type.addWidget(label_Equipment_Type)
        layout_Type.addWidget(self.cb_Equipment_Type)
        layout.setSpacing(20)
        layout.addLayout(layout_Input)
        layout.addLayout(layout_Type)
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self
        )
        # self.button_box.setStyleSheet("margin-top:20px")
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)
        self.resize(400, 150)
        self.css_Layout()

    def css_Layout(self):
        self.button_box.setFixedHeight(30)
        self.button_box.setStyleSheet("font-size:15px")
        self.btn_Suggest.setStyleSheet("font-size:15px")
        self.btn_Suggest.setFixedHeight(30)
        self.btn_Suggest.setFixedWidth(100)
        css.css_Clsuter()

