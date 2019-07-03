rehber = {"Karakter1":{"telefon":"0532545123"
                       ,"Ev adresi":"Vatan cad"
                       ,"Numara":"12032"
                       ,"Kapı numarası":"758"}
                       }

isimler = rehber.keys()
aranan_kisi = input("Aradıgınız kisinin ismini giriniz: ")
aranan_ozellik = input("Aranan özellik giriniz:")
 
if aranan_kisi == isimler:
    flag = True
else:
    flag = False
if flag:
    print(rehber.get(aranan_kisi,"Bu").get(aranan_ozellik,"Aranan özellik bulunamadı"))
else:
    print("Aranan kisi rehberde var özelliği yok")


    
