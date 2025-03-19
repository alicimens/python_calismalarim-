
# raise  bizim  bir hatayı istediğimiz  fonksiyonun, methodun falan içine  göndermemize yarar  

#  bak  bu  kodda  hatayı olusturduk ama  try  except ile  hatayı  yonetmeliyiz aynı zamanda 

def pozitif_sayi_kontrol(sayi):

    if sayi < 0:
        raise  ValueError ("negatif sayilar kabul edilmez ")  # Bilinçli hata fırlatma
    else:
        print("Geçerli sayi:", sayi)

try:
    pozitif_sayi_kontrol(-5)  # Hata oluşacak
except ValueError as e:
    print("Hata yakalandi:", e)  # Program çökmeyecek, hata mesajı ekrana yazdırılacak
