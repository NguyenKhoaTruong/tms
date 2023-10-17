import sys
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QLineEdit, QDialogButtonBox, QLabel
from PyQt5.QtCore import QFile, QTextStream


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Start Point")

        layout = QVBoxLayout()

        self.label_Address = QLabel("Address:")
        self.input_Address = QLineEdit(self)

        self.label_Code = QLabel("Code:")
        self.input_Code = QLineEdit(self)

        layout.addWidget(self.label_Address)
        layout.addWidget(self.input_Address)

        layout.addWidget(self.label_Code)
        layout.addWidget(self.input_Code)

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout.addWidget(self.button_box)

        self.setLayout(layout)
        self.resize(500, 200)
        self.css_Layout()

    def css_Layout(self):
        self.button_box.setFixedHeight(30)
        style_file = QFile("UI\style.css")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            self.setStyleSheet(stream.readAll())
            style_file.close()
