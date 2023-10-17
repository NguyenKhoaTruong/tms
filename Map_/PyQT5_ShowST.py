import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QTableWidget,
    QLabel,
    QLineEdit,
    QWidget,
    QGridLayout,
    QPushButton,
)
import Map_.css_Map_Route as css


class show_ResultST:
    def __init__(self, layout):
        self.html_Trip(layout)

    def html_Trip(self, layout):
        grid_layout = QGridLayout()
        vbox_container = QWidget()
        # Tạo QVBoxLayout và thiết lập nó cho QWidget
        vbox_layout = QVBoxLayout(vbox_container)
        table_widget = QTableWidget(4, 3)
        table_widget.setMinimumSize(400, 200)

        label_Direct = QLabel("Direct Distance")
        label_Route = QLabel("Route Distance")
        label_Time = QLabel("Route Time")
        input_Direct = QLineEdit()
        input_Route = QLineEdit()
        input_Time = QLineEdit()
        vbox_layout
        grid_layout.addWidget(table_widget, 0, 0)
        grid_layout.addWidget(label_Direct, 1, 0)
        grid_layout.addWidget(input_Direct, 1, 1)

        grid_layout.addWidget(label_Route, 2, 0)
        grid_layout.addWidget(input_Route, 2, 1)

        grid_layout.addWidget(label_Time, 3, 0)
        grid_layout.addWidget(input_Time, 3, 1)

        grid_layout.setHorizontalSpacing(10)
        layout.addLayout(grid_layout)
