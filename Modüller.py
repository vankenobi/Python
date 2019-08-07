#Modül1 Sayfasi

def selamver():
    print("Selam")
def mutlak_deger_al(sayi):
    if sayi < 0:
        return -sayi
    return sayi

#Modüller sayfasi

from modul1 import *         #iki çeşit modül ekleme seçeneği var.    
import modul1 

modul1.selamver()
print(modul1.mutlak_deger_al(45))
