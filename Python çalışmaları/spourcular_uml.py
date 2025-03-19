
import datetime 

class Sporcular ():
    def __init__ (self ,isim  = "", cinsiyet = "", boy = "", kilo ="",dtarihi ="",kategorisi = "sporcu"):
       self.isim = isim 
       self.cinsiyet = cinsiyet
       self.boy = float(boy) 
       self.kilo = float (kilo) 
       self.dtarihi = dtarihi 
       self.kategorisi = kategorisi
    def VKE_hesaplama (self):
        vke =float(self.kilo/(self.boy*self.boy))
        return vke
        
    def yas_hesaplama(self):
    
      yas =  int (datetime.datetime.now().year)-int(self.dtarihi.split(".")[2]) # bu satiri  tekrar et 
      return yas     
      
    def bilgi_goster (self):
        
         
        return f"""
        {self.kategorisi}
        ismi : {self.isim}
        Cinsiyeti : {self.cinsiyet}
        Dogum tarihi :{self.dtarihi}
        """
class Antrenor(Sporcular):

    def __init__(self, isim="", cinsiyet="", boy="", kilo="", dtarihi="", Brans= "",Kidem = 0, ):
        super().__init__(isim, cinsiyet, boy, kilo, dtarihi,Antrenor.__name__ )
        self.Brans = Brans
        self.Kidem = Kidem
        self.maas = 5700 + (Kidem*100)

    def Maas_Hesapla (self ):
       return self.maas
    def VKE_hesaplama(self):
        return super().VKE_hesaplama()
    def yas_hesaplama(self):
        return super().yas_hesaplama()
    def bilgi_goster (self):
        return f"""
        {super().bilgi_goster}
        Maasi : {self.Maas_Hesapla()}
        VKE   : {self.VKE_hesaplama()}
        Brans :  {self.Brans}
        Kidem : {self.Kidem}
        """

class Uye (Sporcular):
    
    def __init__(self, isim="", cinsiyet="", boy="", kilo="", dtarihi="", kategorisi="sporcu", 
                 uyebastarih = "5.5.2021", uyebitistarih = "5.5.2022" , programbastarih ="1.1.2021", programbitistarih = "3.3.2021"):
        super().__init__(isim, cinsiyet, boy, kilo, dtarihi, kategorisi,Uye.__name__)
        
        self.uyesbastarih = uyebastarih
        self.uyebitistarih = uyebitistarih
        self.programbastarih = programbastarih
        self.programbitistarih = programbitistarih

    def kacgunkaldi(self):
        pass    

    def programbitis(self):
        pass
    def VKE_hesaplama(self):
        return super().VKE_hesaplama()
    def yas_hesaplama(self):
        return super().yas_hesaplama()
    def bilgi_goster (self):
        pass
    
antrenor1= Antrenor ("unsal", "erk","1.70","70","05.05.1990","Pilates",10)
print(antrenor1.bilgi_goster())