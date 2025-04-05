from PyQt5.QtWidgets import QApplication  # Uygulama başlatmak için gereken sınıf
from login import LoginPage  # Az önce oluşturduğumuz LoginPage sınıfını içe aktarıyoruz

app = QApplication([])  # Uygulama nesnesi oluşturuyoruz (event loop başlatmak için şart)
pencere = LoginPage()  # LoginPage sınıfından bir pencere adında nesne oluşturuyoruz

pencere.show()  # Pencereyi ekranda gösteriyoruz

app.exec_()  # PyQt5 uygulamasını çalıştırmak için event loop'u başlatıyoruz
