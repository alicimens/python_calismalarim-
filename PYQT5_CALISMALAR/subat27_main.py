from PyQt5.QtWidgets import *
from subat27 import Ui_MainWindow 


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qtTasarim = Ui_MainWindow #obje   turettik
        self.qtTasarim.setupUi(self)

app = QApplication ([])
pencere = main()  # nesne  turettik
pencere.show()
app.exec_() #sonsuz  bir  çalışma  kendini  tazelesin dedi videoda


    #kodu  yarida  bıraktık izleyerek  devam  edecez (düzenli kod  yazma  videosu  dakika: 10 :55)