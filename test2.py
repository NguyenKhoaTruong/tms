import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QDialog,QApplication

from test1 import MyDialog  # Import class từ file dialog.py
from kneed import KneeLocator
from sklearn.cluster import KMeans
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.data=[]
        self.setWindowTitle('Main Window')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.button = QPushButton('Mở Dialog', self)
        self.button.clicked.connect(self.show_dialog)

        self.label = QLabel('Dữ liệu từ Dialog: ', self)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.central_widget.setLayout(self.layout)

    def show_dialog(self):
        data1 = [
    [10.79873892744089, 106.58475073864138],
    [10.764949051934444, 106.63425262680195],
    [10.806544151486372, 106.63419073199863],
    [10.764079789979318, 106.57976890751715],
    [10.7400530995737, 106.7338764787851],
    [10.790089319833042, 106.64003441699646],
    [10.823614351505748, 106.68602501436756],
    [10.765105259503555, 106.6013630947109],
    [10.754275999507401, 106.65038486747628],
    [10.732523192626422, 106.7069379362698],
    [10.779682363758237, 106.63120245625056],
    [10.825261241106542, 106.70667993346213],
    [10.737699613991722, 106.72571767515892],
    [10.828667037403232, 106.67410762602444],
    [10.778491793268698, 106.66544417327842],
    [10.741083499365942, 106.70203763215794],
    [10.823955431371676, 106.69219393905452],
    [10.836741476104356, 106.68341207235753],
    [10.833827624045112, 106.67059323605213],
    [10.926737581225254, 106.55686147657384],
    [10.749504024802121, 106.65453533199823],
    [10.959016288745774, 106.50469227862662],
    [10.754712703279315, 106.63326099624115],
    [10.694726756700211, 106.58839643199786],
    [10.864422978832003, 106.58982153727769],
    [10.769063188224223, 106.6530953335917],
    [10.739350713879652, 106.62920119338125],
    [10.767611232403523, 106.68591328391079],
    [10.769049682361974, 106.66577650080094],
    [10.753644717579572, 106.6133352973548],
    [10.827283008576414, 106.81193993662411],
    [10.762954140781089, 106.65702261420729],
    [10.756317534699074, 106.69231770751723],
    [10.8053001493701, 106.67858331832046],
    [10.755112433441516, 106.690042442933],
    [10.685585396099569, 106.62249706823035],
    [10.796232738243804, 106.74053639547414],
    [10.74838755597344, 106.70536196146102],
    [10.824285079737, 106.68272749434792],
    [10.834930016798408, 106.66219501977464],
    [10.826086717333506, 106.8173342644842],
    [10.868224893898695, 106.73579148784809],
    [10.736633059860063, 106.61394473840016],
    [10.760277509184522, 106.66189973845366],
    [10.744333365337354, 106.6550291679002],
    [10.859054175855906, 106.77776523805082],
    [10.801408751565196, 106.61857143060715],
    [10.827939670249133, 106.72155997085434],
    [10.800965497496932, 106.65353682632195],
    [10.749530100247858, 106.70849129687295],
    [10.754222040359897, 106.6516615480369],
    [10.785468096971915, 106.64193116565633],
    [10.834527603648134, 106.66475695577076],
    [10.830911251743272, 106.61499504415322],
    [10.666857886706726, 106.72514616742377],
    [10.75313395509537, 106.7007388263215],
    [10.815241990112296, 106.67207382944194],
    [10.633211745181494, 106.76237678601967],
    [10.775691481392982, 106.63053733789408],
    [10.787963341854569, 106.69955300059291],
    [10.77059663982937, 106.66947987384219],
]
        dialog = MyDialog(self)
        dialog.ok_button.clicked.connect(lambda:self.test_Suggest(data1,dialog.textbox))
        dialog.textbox.setText('10')
        result = dialog.exec_()
        if result == QDialog.Accepted:
            print()
        

    def test_Suggest(self,data,ui):
        k_values = range(1, len(data) - 1)
        sse = []
        for k in k_values:
            kmeans = KMeans(n_clusters=k)
            kmeans.fit(data)
            sse.append(kmeans.inertia_)
        
        self.data=self.test_1(k_values,sse)
        ui.setText(str(self.data))
    def test_1(self,data,se):        
        kl = KneeLocator(data, se, curve="convex", direction="decreasing")
        optimal_k = kl.elbow
        return int(optimal_k)
menu_UI = QApplication(sys.argv)
menu_UI.setStyleSheet("QPushButton{font-size: 20px; width: 200px; height: 50px}")
view_UI = MainWindow()
view_UI.show()
sys.exit(menu_UI.exec_())