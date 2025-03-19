import burc

isim = input ("ismini gir \n")
dogumtarihi = input ("dogum tarihini  gir. örnek: 05-03-1996 \n").split ("-")

gun = int(dogumtarihi[0])
ay = int(dogumtarihi[1])
yil = int(dogumtarihi[2])

print (burc.hangiburc(isim,gun,ay,yil)) #bak  burda  print  edilen şey  burc modülünde hangiburc isimli fonksiyonda ordan  return da yazan şeyi alır ve print eder 
                                    
