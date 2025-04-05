from PyQt5.QtWidgets import QApplication,QWidget
from urun_listele_python import Ui_Form

class UrunListelePage(QWidget) :

    def __init__(self) -> None:  # Sınıfın yapici (constructor) fonksiyonu
        super().__init__()  
        self.urunlisteleform = Ui_Form()   # nesne olusturduk  uurunlisteleform adinda
        self.urunlisteleform.setupUi(self) # setupUi  metodunu  kullanmak için de  bu  kodu  yazdık 

