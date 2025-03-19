class Ogrenci ():
    
    def __init__(self):
        self.isim        = ""
        self.sinif       = ""
        self.numara      = ""
        self.cinsiyet    = ""
        self.dtarihi     = ""
        self.devamsizlik = 0
    def ekle (self):
        self.isim         =input("ogrenci ismini giriniz ")
        self.sinif        =input ("ogenci sinifini  giriniz ")
        self.numara       =input("ogrenci numaraini  giriniz ")
        self.cinsiyet     =input("ogrenci  cinsiyetini  giriniz ")
        self.dtarihi      =input("ogrenci yilini  giriniz ")
        self.devamsizlik  =input ("ogrenci devamsizlik ekleyiniz ")
    def sil (self):
        del self
    def guncelle (self):
        self.sinif     = input("ogrenci sinifini giriniz")
        self.numara    = input ("ogrenci  numarasini  giriniz")     
        self.devamsizlik += int(input("ogrenci devamsizlik ekleyiniz")) 
    def goster (self):

        return  f"""
        Ogrencinin: 
        Adi: {self.isim}
        Soyadi:{self.sinif}
        Numarasi: {self.numara}
        Cinsiyeti: {self.cinsiyet}
        Dogum Tarihi: {self.dtarihi}
        Devamsizlik sayisi: {self.devamsizlik}
        """

ogrenci1 = Ogrenci()
ogrenci1.ekle()
print(ogrenci1.goster())        

#ogrenci2 = Ogrenci("ali" , "9" , "45", "erkek" , "1990", "6") #  eger  bunu  kullanacaksak  init de  parantez icinde attributeleri  yazmamız lazım
print(ogrenci2.goster())