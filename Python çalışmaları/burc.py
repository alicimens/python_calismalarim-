
import datetime 

def hangiburc (isim = "",gun = 0 , ay = 0, yil = 0):
       
        simdikiyil = datetime.datetime.now().year # datetime modülündeki  datetime sınıfını kullan 
        yas = simdikiyil-yil

        burc = " "

        if (ay == 12 and gun >= 22) or  (ay== 1 and gun <=20):
            burc = "Oğlak"
        if (ay == 1 and gun >= 21) or  (ay== 2 and gun <=18):
            burc = "Kova"
        if (ay == 2 and gun >= 19) or  (ay== 3 and gun <=20):
            burc = "Balik"
        if (ay == 3 and gun >= 21) or  (ay== 4 and gun <=20):
            burc = "Koç"
        if (ay == 4 and gun >= 21) or  (ay== 5 and gun <=20):
             burc = "Boğa"
        if (ay == 5 and gun >= 21) or  (ay== 6 and gun <=21):
             burc = "İkizler"
        if (ay == 6 and gun >= 22) or  (ay== 7 and gun <=22):
             burc = "Yengeç "
        if (ay == 7 and gun >= 23) or  (ay== 8 and gun <=22):
             burc = "Aslan"
        if (ay == 8 and gun >= 23) or  (ay== 9 and gun <=22):
            burc = "Başak"
        if (ay == 9 and gun >= 23) or  (ay== 10 and gun <=23):
            burc = "Terazi"
        if (ay == 10 and gun >= 24) or  (ay== 11 and gun <=22):
            burc = "Akrep" 
        if (ay == 11 and gun >= 23) or  (ay== 12 and gun <=21):
            burc = "Yay"

        #return "ali {} yasinda ve  burcu {}".format (yas,burc)
        return f"{isim} {yas} yasinda  ve burcu {burc}" 
        
         
     