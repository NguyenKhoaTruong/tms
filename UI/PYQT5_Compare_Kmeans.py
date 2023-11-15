import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtCore import QBuffer, QIODevice
from PyQt5.QtGui import QImage
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
import os
import re


class ui_Test(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_ = QVBoxLayout()
        self.browser = QWebEngineView()
        self.ui_()

    def ui_(self):
        self.setWindowTitle("Kmeans Cluster Iteration")
        self.showMaximized()
        self.layout_.addWidget(self.browser)
        self.setLayout(self.layout_)
        folder_path = "Assets\Img_Compare"
        self.load_images(folder_path)

    def load_images(self, folder_path):
        html_content = """
        <html>
            <head>
                <style>
                    .image-container {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-between;
                    }
                    .image-item {
                        flex: 0 0 30%;
                        margin-bottom: 10px;
                    }
                </style>
            </head>
            <body>
                <div class="image-container">
        """
        image_formats = ["png", "jpg", "jpeg", "gif", "bmp"]
        image_files = [
            f
            for f in os.listdir(folder_path)
            if f.split(".")[-1].lower() in image_formats
        ]
        image_files.sort(key=lambda x: int(re.search(r"\d+", x).group()))
        for file_name in image_files:
            file_path = os.path.join(folder_path, file_name)
            image_data = self.image_to_base64(file_path)
            html_content += f'<div class="image-item"><img src="data:image/png;base64,{image_data}" alt="{file_name}"></div>'
        html_content += """
                </div>
            </body>
        </html>
        """
        self.browser.setHtml(html_content)
        self.show()

    def image_to_base64(self, image_path):
        image = QImage(image_path)
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly)
        image.save(buffer, "PNG")
        return buffer.data().toBase64().data().decode("utf-8")
