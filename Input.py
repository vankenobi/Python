a = input("Lutfen birinci degeri giriniz:")
b = input("Lutfen ikinci degeri giriniz:")
c = input("Lutfen ucuncu degeri giriniz:")

print("girilen sayilarin toplami",int(a)+int(b)+int(c))

######################################################

ad = input("Lutfen oyuncunun adini giriniz:")
soyad = input("Lutfen oyuncunun soyadini giriniz:")
numara = input("Lutfen oyuncunun numarasini giriniz:")

bilgiler = [ad,soyad,numara]

#ikiside aynı özelliktedir.

 print("Oyuncunun adi:",ad,"Oyuncunun soyadi:",soyad,"oyuncunun numarasi:",numara)
 print("Oyuncunun adi:{} Oyuncunun soyadi:{} Oyuncunun numarasi:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))
