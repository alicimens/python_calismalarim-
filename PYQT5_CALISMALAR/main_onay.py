from cProfile import label 
from PyQt5.QtWidgets import * 
from  onay_python import Ui_Form


class MainPage (QWidget) :
    def __init__(self) :
        self.secilensoslar = list()
        self.liste = list() # burada  nesne olusturmuyoz  ha  liste  tanimliyoruz (muhtemelen o da nesne  olusturma  giriyordur teknik olarak ama  bu bildigimiz  liste tanimalama yani)
        super().__init__() 
        self.onay = Ui_Form() # burada  nesne  olusturuyoz
        self.onay.setupUi(self)
        self.onay.pushButton.clicked.connect(self.Goster)
    def Goster(self):
        self.secilensoslar.clear()
        if self.onay.checkBox.isChecked ():  # buradaki  checkbox mayonezin  checkbox'i
            self.secilensoslar.append("mayonez")
        if self.onay.checkBox_2.isChecked(): # buradaki checkbox ketcap in checkbox'i
            self.secilensoslar.append("ketcap")
        if self.onay.checkBox_3.isChecked():  # buradaki  checkbox  aci sosun checkbox'i
            self.secilensoslar.append("Aci sos")
        self.onay.label_soslar.setText(str(self.secilensoslar))


app = QApplication([])    # Uygulama başlatılır.
pencere = MainPage()      # MainPage sinifindan pencere nesnesi oluşturulur.
pencere.show()            # Pencere ekranda gösterilir.
app.exec_()               # PyQt olay döngüsü başlatılır, arayüz çalışır durumda kalır.