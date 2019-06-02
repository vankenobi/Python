defkullanici = "musa0123"
defsifre = "123456"

kullaniciadi = input("Lutfen kullanici adini giriniz.")
kullanicisifre = input("Lutfen sifreyi giriniz")

if( defkullanici == kullaniciadi and defsifre == kullanicisifre ):
    print("Giris izni verildi.")
elif(defkullanici != kullaniciadi and defsifre == kullanicisifre):
    print("Kullanici adi yanlis girdiniz.")
elif(defkullanici == kullaniciadi and defsifre != kullanicisifre):
    print("Sifreyi yanlis girdiniz.")
else:
    print("Kullanici adi ve sifre yanlis. Giris izni verilmedi.")

