class Birey:
    def __init__(self,isim:str,soyisim:str,cinsiyet:str,kimlik:int):
        self.isim = isim
        self.soyisim = soyisim
        self.cinsiyet = cinsiyet
        self.kimlik = kimlik
class Çalışan(Birey):
    def __init__(self,isim:str,soyisim:str,cinsiyet:str,kimlik:int,maaşı:int):
        Birey.__init__(self,isim,soyisim,cinsiyet,kimlik)
        self.maaşı = maaşı
    def Maaşzam(self,zam:int):
        self.maaşı += zam

class Mühendis(Çalışan):
    def __init__(self,isim:str,soyisim:str,cinsiyet:str,kimlik:int,maaşı:int,diller:tuple,yazilim_dilleri:tuple):
        Çalışan.__init__(self,isim,soyisim,cinsiyet,kimlik,maaşı)
        self.yazilim_dilleri = yazilim_dilleri
        self.diller = diller
    def get(self):
        print(self.isim,self.soyisim,self.cinsiyet,self.kimlik,self.maaşı,self.diller,self.yazilim_dilleri)

class Muhasebeci(Çalışan):
    def __init__(self,isim:str,soyisim:str,cinsiyet:str,kimlik:int,maaşı:int,bilinen_programlar:tuple):
        Çalışan.__init__(self,isim,soyisim,cinsiyet,kimlik,maaşı)
        self.bilinen_programlar = bilinen_programlar
    

mühendis = Mühendis("Musa","Küçük","Erkek",("C#","C++","Python"),1500,21599,("İngilizce","Fransızca","Almanca",))
print("Eski maaş:",mühendis.maaşı)
mühendis.Maaşzam(123) #Mühendisin Maaşına 123 tl zam yapıldı.
print("Yeni Maaş:",mühendis.maaşı)
mühendis.get()

        



        
