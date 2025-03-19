import datetime as  tarih 
import math 

class DogumGunuHesapla ():

    def __init__ (self)  -> None : 
     while True :
      try :  
          dogumtarihi = input("dogum tarihinizi girin örn 05-07-1990 \n").split("-")
          if len (dogumtarihi) != 3 :
               raise ValueError  
          dgun = int(dogumtarihi[0])
          day = int (dogumtarihi[1])
          dyil = int (dogumtarihi[2])

          gun = int (tarih.datetime.now().day)
          ay = int (tarih.datetime.now().month)
          yil = int (tarih.datetime.now().year)
         
          farkgun = gun - dgun
          farkay = (ay-day)*30 
          farkyil = (yil-dyil)*12*30
          break 
      except ValueError:                   
         print("lutfen dogum tarihini  dogru sekilde  girin")