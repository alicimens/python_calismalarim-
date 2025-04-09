from PyQt5.QtWidgets import QApplication,QMainWindow
from anapencre_python import Ui_MainWindow 
from urun_listele import  UrunListelePage

class AnapencerePage (QMainWindow) : #  bak burada QMainWindow dan  kalitim aliyoruz ya yukarıda  kutuphanesini de dahil etmeyi  unutma
    def __init__(self) -> None:  # Sınıfın yapıcı (constructor) fonksiyonu
        super().__init__()  
        self.anapencereform = Ui_MainWindow()  
        self.anapencereform.setupUi(self)
        self.urunlisteleform = UrunListelePage() # nesne  olusturduk yine 
        self.anapencereform.urunlistele.triggered.connect(self.UrunListeleFormu)
        # 11. satirdaki kod icin urunlistele kısmı  anapencere nin menu kısmından  geliyor  QT designerdan bakabiliriz buna 
    def UrunListeleFormu (self): 
        self.anapencereform.urunlisteleform.show()