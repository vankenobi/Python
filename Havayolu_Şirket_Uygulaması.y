
from datetime import date,time,datetime
from random import randint 

# ============= CLASSES =================

class Şehir:
    def __init__(self,isim):
        self.__isim = isim
        self.__sicaklik = randint(18,25)
        self.__HavaDurumu = ["Açık","Kapalı","Yağmurlu","Sağanak Yağışlı"][randint(0,3)]
    def getİsim(self):
        return self.__isim
    def getSicaklik(self):
        return self.__sicaklik
    def getHavaDurumu(self):
        return self.__HavaDurumu
    def setHavaDurumu(self,durum):
        if durum not in ["Açık","Kapalı","Yağmurlu","Sağanak Yağışlı"]:
            pass
        else:
            self.__HavaDurumu = durum


class Uçuş: 
    def __init__(self,nereden:Şehir,nereye:Şehir,tarih:datetime):
        self.__nereden = nereden
        self.__nereye = nereye
        self.__tarih = tarih
    def getUçuşTarihi(self):
        return self.__tarih
    def getNereden(self):
        return self.__nereden
    def getNereye(self):
        return self.__nereye



class Yolcu:
    def __init__(self,isim:str,soyisim:str,tc:int):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__tc = tc

    def getİsim(self):
        return self.__isim
    def getSoyisim(self):
        return self.__soyisim
    def getTc(self):    
        return self.__tc



class Bilet:
    def __init__(self,yolcu:Yolcu,uçuş:Uçuş,koltukNumarası:str):
        self.__yolcu = yolcu
        self.__uçuş = uçuş
        self.__koltuknumarası = koltukNumarası
        
    def getUçuş(self):
        return self.__uçuş
    def __str__(self):

        string = """
        isim:            {}
        soyisim:         {}
        T.C.:            {}
        Uçuş Tarihi:     {}
        Nereden:         {}
        Nereye:          {}   Hava durumu: {} / Sıcaklık: {} °C
        Koltuk Numarası: {}
        
        """.format( self.__yolcu.getİsim() , self.__yolcu.getSoyisim() , self.__yolcu.getTc() , self.__uçuş.getUçuşTarihi().date() , self.__uçuş.getNereden().getİsim() ,self.__uçuş.getNereye().getİsim() ,self.__uçuş.getNereye().getHavaDurumu()  ,self.__uçuş.getNereye().getSicaklik() ,self.__koltuknumarası)
        return string
    

class Pegasus():
    def __init__(self):
        self.__aktifbiletler = list()
        self.__geçmişbiletler = list()
        self.__Aktifuçuşlar = list()
        self.__geçmişuçuşlar= list()

    def BiletAl(self,yolcu:Yolcu,uçuş:Uçuş,koltukNumarası:str):
        if uçuş in self.__Aktifuçuşlar:
            bilet = Bilet(yolcu,uçuş,koltukNumarası)
            self.__aktifbiletler.append(bilet)
            return bilet
    
    def uçuşOluştur(self,nereden:Şehir,nereye:Şehir,tarih:datetime):
        uçuş = Uçuş(nereden,nereye,tarih)
        self.__Aktifuçuşlar.append(uçuş)
        return uçuş 

    def Biletİptal(self,bilet:Bilet):
        self.__aktifbiletler.remove(bilet)

    def UçuşGerçekleşti(self,uçuş:Uçuş):
        for bilet in self.__aktifbiletler:
            if bilet.getUçuş == uçuş:
                self.__aktifbiletler.remove(bilet)
                self.__geçmişbiletler.append(bilet)
        self.__Aktifuçuşlar.remove(uçuş)
        self.__geçmişuçuşlar.append(uçuş)

    def __str__(self):

        string = """
        isim:            {}
        soyisim:         {}
        T.C.:            {}
        Uçuş Tarihi:     {}
        Nereden:         {}
        Nereye:          {}
        Koltuk Numarası: {}
        
        """.format( self.__yolcu.getİsim() , self.__yolcu.getSoyisim() , self.__yolcu.getTc() , self.__uçuş.getUçuşTarihi().date() , self.__uçuş.getNereden().getİsim() ,self.__uçuş.getNereye().getİsim(),self.__koltuknumarası)
        return string


#========================================
def Main():
    x = """
    Adana
    Adıyaman
    Afyonkarahisar
    Ağrı
    Amasya
    Ankara
    Antalya
    Artvin
    Aydın
    Balıkesir
    Bilecik
    Bingöl
    Bitlis
    Bolu
    Burdur
    Bursa
    Çanakkale
    Çankırı
    Çorum
    Denizli
    Diyarbakır
    Edirne
    Elazığ
    Erzincan
    Erzurum
    Eskişehir
    Gaziantep
    Giresun
    Gümüşhane
    Hakkâri
    Hatay
    Isparta
    Mersin
    İstanbul
    İzmir
    Kars
    Kastamonu
    Kayseri
    Kırklareli
    Kırşehir
    Kocaeli
    Konya
    Kütahya
    Malatya
    Manisa
    Kahramanmaraş
    Mardin
    Muğla
    Muş
    Nevşehir
    Niğde
    Ordu
    Rize
    Sakarya
    Samsun
    Siirt
    Sinop
    Sivas
    Tekirdağ
    Tokat
    Trabzon
    Tunceli
    Şanlıurfa
    Uşak
    Van
    Yozgat
    Zonguldak
    Aksaray
    Bayburt
    Karaman
    Kırıkkale
    Batman
    Şırnak
    Bartın
    Ardahan
    Iğdır
    Yalova
    Karabük
    Kilis
    Osmaniye
    Düzce
    """

    şehirler = list()
    for i in x.split():
        şehirler.append(Şehir(i))
    musa = Yolcu("Musa","Küçük",2149645168)
    pegasus = Pegasus()
    uçuş1 = pegasus.uçuşOluştur(şehirler[5],şehirler[12],datetime(2018,4,9,7,40))
    bilet1 = pegasus.BiletAl(musa,uçuş1,"A15")
    print(bilet1)
    
if __name__ == "__main__":
    Main()

   
    
