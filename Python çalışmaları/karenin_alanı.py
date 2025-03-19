class KareAlan():

    def __init__(self, yukseklik , genislik ):
        self.yukseklik = yukseklik
        self.genislik = genislik
    def Hesapla (self):
        return self.yukseklik * self.genislik

Kare1 = KareAlan(15,10) 
print("Karenin Alani :",Kare1.Hesapla())
