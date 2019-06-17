#Modül1 Sayfasi

def selamcak():
    print("Naber Canım")
def mutlakdegeral(sayi):
    if sayi < 0:
        return -sayi
    return sayi

#Modüller sayfasi

from modul1 import *                     #iki çeşit modül ekleme seçeneği var.    
import modul1 

modul1.selamcak()
print(modul1.mutlakdegeral(45))
