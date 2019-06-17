dersler = {"Ahmet":["Veritabanı,isletim sistemleri"],"Oguz":["Script dersi,Nesne tabanlı programlama"],"Mehmet":["Lineer cebir dersi"]}

isim = input("isim giriniz:")

print("{} aldığı dersler:".format(isim))

for i in (dersler[isim]):
    print(i)
        
   
