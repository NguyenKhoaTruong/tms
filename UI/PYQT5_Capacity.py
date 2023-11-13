from PyQt5.QtWidgets import (
    QPushButton,
    QComboBox,
    QLabel,
    QGridLayout,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
import numpy as np


class Capacity_Mode:
    def __init__(self, *argv, **kwargs):
        items_Mode = ["Volume", "Weight", "Trip Type"]
        ui_ = argv[0]
        self.ui_Capacity(ui_, items_Mode)

    def ui_Capacity(self, ui, items):
        boder_Capacity = QHBoxLayout()
        mode_Capacity = QGridLayout()
        label_Capacity = QLabel("Capacity View Mode")
        btn_Mode = QPushButton("Refresh")
        btn_Mode.clicked.connect(self.handle_Refresh)
        cb_Mode = QComboBox()
        figure = Figure()
        canvas = FigureCanvas(figure)
        mode_Capacity.addWidget(label_Capacity, 1, 0)
        mode_Capacity.addWidget(cb_Mode, 2, 0)
        mode_Capacity.addWidget(btn_Mode, 2, 1)
        mode_Capacity.setRowStretch(3, 1)
        mode_Capacity.setContentsMargins(10, 200, 0, 0)
        boder_Capacity.addLayout(mode_Capacity)
        boder_Capacity.addWidget(canvas)
        self.add_ItemMode(cb_Mode, items)
        self.chart(figure, canvas)
        self.custom_CSS(ui, label_Capacity, btn_Mode, cb_Mode)
        ui.addLayout(boder_Capacity)
        # hande add event button

    def add_ItemMode(self, cb, item):
        for value in item:
            cb.addItem(value)
        return cb

    def custom_CSS(self, layout, title, button, cb):
        title.setStyleSheet("font-size:15px")
        button.setFixedHeight(40)
        button.setFixedWidth(100)
        cb.setFixedHeight(40)
        cb.setFixedWidth(150)

    def chart(self, figure, canvas):
        ax = figure.add_subplot(111)
        categories = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        values = [25, 40, 30, 45, 50, 55, 65, 75, 75, 85]
        ax.bar(categories, values, color="skyblue")
        ax.set_title("K-Mean Cluster")
        ax.set_xlabel("Trip")
        ax.set_ylabel("Weight")
        canvas.draw()

    def handle_Refresh(self):
        a = 1
        print("a", a)
        print("Có cái con cá")
