from PyQt5.QtWidgets import QApplication, QWidget  # PyQt5'ten uygulama ve pencere sınıfını içe aktarıyoruz
from login_python import Ui_Form  # Qt Designer'dan çevirdiğimiz arayüz sınıfını içe aktarıyoruz
from anapencere import AnapencerePage

class LoginPage(QWidget):  # QWidget sınıfından kalıtım alarak yeni bir pencere oluşturuyoruz

    def __init__(self) -> None:  # Sınıfın yapıcı (constructor) fonksiyonu
        super().__init__()  # Üst sınıfın (QWidget) başlatıcısını çağırıyoruz
        self.loginform = Ui_Form()  # Qt Designer'dan gelen arayüz sınıfının bir örneğini oluşturuyoruz
        self.loginform.setupUi(self)  # setupUi fonksiyonu ile arayüz elemanlarını bu pencereye çiziyoruz
        self.anapencereac = AnapencerePage()
        self.loginform.pushButton.clicked.connect(self.GirisYap)
    def GirisYap(self) : 
        kadi = self.loginform.lineEdit_kullaniciadi.text()     
        sifre = self.loginform.lineEdit_sifre.text()
        if kadi == "ali"  and  sifre == "123":
            self.hide
            self.anapencereac.show()

