import os
import re
import sys
from PyQt5.QtCore import Qt, QByteArray, QBuffer, QIODevice
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView


class ImageBrowser(QMainWindow):
    def __init__(self):
        super(ImageBrowser, self).__init__()

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Image Browser")
        self.showMaximized()
        folder_path = "Assets/Img_Compare"
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageBrowser()
    window.show()
    sys.exit(app.exec_())
