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
)
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtCore import Qt
import UI.css_UI as css


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Cluster")

        layout = QVBoxLayout()
        layout_Input = QHBoxLayout()
        self.label_Cluster = QLabel("Number Cluster:")
        self.label_Cluster.setStyleSheet("font-size:15px")
        self.input_Cluster = QLineEdit(self)
        self.input_Cluster.setText("10")
        self.input_Cluster.setStyleSheet("font-size:15px")
        self.input_Cluster.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_Input.addWidget(self.label_Cluster)
        # spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # layout_Input.addItem(spacer)
        layout_Input.addWidget(self.input_Cluster)

        layout.setSpacing(20)
        layout.addLayout(layout_Input)
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
        self.input_Cluster.setFixedHeight(30)
        self.button_box.setStyleSheet("font-size:15px")
        css.css_Clsuter()
