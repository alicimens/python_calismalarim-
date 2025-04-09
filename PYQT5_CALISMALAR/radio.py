from PyQt5.QtWidgets import QWidget
from radio_python import Ui_Form

class radioPage (QWidget) : 
    def __init__ (self): 
        super().__init__()
        self.radioform = Ui_Form()
        self.radioform.setupUi(self)

        #pushbuttonöde  olaylar 
        self.radioform.radioButton_buyuk.toggled.connect(self.menusecim) # toggled  yani  tıklandı

    def menusecim(self, checked):
        secim = self.sender()
        if checked :
            print(secim.text())