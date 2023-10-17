from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
)


class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.stackedWidget = QStackedWidget(self)
        self.label = QLabel(self)
        self.stackedWidget.addWidget(self.label)
        btn_Add = QPushButton("Add")
        self.stackedWidget.addWidget(btn_Add)
        self.layout.addWidget(self.stackedWidget)
        self.startAnimation()

    def startAnimation(self):
        self.movie = QMovie("loader.gif")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMovie(self.movie)
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()


if __name__ == "__main__":
    app = QApplication([])
    window = LoadingGif()
    window.setWindowTitle("Loading GIF")
    window.setGeometry(100, 100, 400, 200)
    window.show()
    app.exec()
