def sagslash(adet):
    for i in range(int(adet)):
        print("/",end="")
def solslash(adet):
    for i in range(int(adet)):
        print("\\",end="")
def bosluk(adet):
    for i in range(int(adet)):
        print(" ",end="")
def satiratla(adet):
    for i in range(int(adet)):
        print()
def ustkisim(cap):
    baslangicbosluk = cap/2-1
    for i in range(int(cap/2)):
        bosluk(baslangicbosluk-i)
        sagslash(1)
        bosluk(i*2)
        solslash(1)
        satiratla(1)
def altkisim(cap):
    baslangicbosluk = cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solslash(1)
        bosluk(baslangicbosluk-i*2)
        sagslash(1)
        satiratla(1)
ustkisim(20)
altkisim(20)
