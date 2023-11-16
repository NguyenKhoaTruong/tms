from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Dialog Window')

        self.layout = QVBoxLayout()

        self.label = QLabel('Nhập dữ liệu:')
        self.textbox = QLineEdit(self)
        self.ok_button = QPushButton('OK', self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

