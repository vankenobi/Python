kullanicilar = {"Ahmet":"qwerty",
                "Mehmet":"asdfg"}
kull_adi = kullanicilar.keys()
giris = input("Lutfen kullanici adinizi giriniz:")
if giris in kull_adi:
    print("Hosgeldin {}".format(giris))
    password = input("Lutfen parolani gir:")
    if password in kull_adi:
        print("Sisteme giris yaptiniz. Hosgeldiniz.")
    else:
        print("Parola hatali")
else:
    print("Hatali Kullanici Adi")
