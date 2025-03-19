# map  fonksiyonu 

#yüzde 10 zam

def MaasZam (maas): 
    zamliMaas = maas * 1.1 
    zamliMaas = round (zamliMaas,2)
    return zamliMaas 
maaslar = [5000,3000,2600,4000,5000,1500]
print(list(map(MaasZam,maaslar))) # map(fonksiyon_adi , listenin_adi)