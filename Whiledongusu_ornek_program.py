kullanici = "Musa123"
sifre = "123456"

while(True):

    girkullanici = input("Kullanici adi giriniz:")
    girsifre = input("Sifre giriniz:")

    if (girkullanici == kullanici and girsifre == sifre):
       print("Giris izni verildi.")
       break
    elif(girkullanici != kullanici and girsifre == sifre):
       print("Kullanici adi yanlis girdiniz.")
       print("Tekrar giris yapiniz.")
    elif(girkullanici == kullanici and girsifre != sifre):
       print("Sifreyi yanlis girdiniz.")
       print("Tekrar giris yapiniz")
    elif(girkullanici != kullanici and girsifre != sifre):
       print("kullanici adi ve sifre yanlis girdiniz.")
       print("Tekrar giris yapiniz.")
        
 """
 kullanici = "Musa123
 sifre = "123456"

while(True):

    girkullanici = input("Kullanici adi giriniz:")
    girsifre = input("Sifre giriniz:")

    if (girkullanici == kullanici and girsifre == sifre):
       print("Giris izni verildi.")
       break
    elif(girkullanici == kullanici and girsifre != sifre):
        print("Sifreyi yanlis girdiniz.")
        cevap = input("Sifrenizi unuttuysaniz degistirmek ister misiniz (E/H) ?:")
        if (cevap == "E"):
             yenisifre = input("Lutfen yeni sifre giriniz:")
             sifre = yenisifre
             print("Sifreniz degisti artik yeni sifreniz:",sifre)
             break      
        elif (cevap == "H"):
                break    
    elif(girkullanici != kullanici and girsifre != sifre):
       print("kullanici adi ve sifre yanlis girdiniz.")
       print("Tekrar giris yapiniz.")
  """
