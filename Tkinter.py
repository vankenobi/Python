from tkinter import *
pencere = Tk() # pencere oluşturduk.

pencere.title("Kütüphane Kitap Kayıt") #Form ekranına başlık 

pencere.geometry(550x150+100+150) #Form ekranının boyutunu belirledik 
#ilk + dan sonraı form penceresinin ekranın neresinde belireceğini belirler

pencere.resizable(FALSE,FALSE) #pencerenin sonradan boyutlandırılmasına izin vermez.

pencere.minsize(100,100)  #Penceremizin minumum alacağı boyuttur.
pencere.maxsize(500,500)  #Penceremizin maximum alacağı boyuttur.

pencere.state("normal")   #pencere durumu (normal= normal bi şekilde başlar) #pencere durumu (iconic = ikon şeklinde başlar) 
#pencere durumu (zoomed = tam ekran)

pencere.wm_attributes("-alpha",0.8) #Pencere saydamlığını ayarlar. örn:0 dan 1 e kadardır şuan %80 saydam

yazi = Label(text = "Merhaba Dünya",fg = "red", bg = "")  # Form ekranına etiket eklemek için kullanılır.
yazi.pack() #yazi.pack yazmassak görünmez. #İkinci parametre yazi rengini belirler.üçüncü parametre yazi arkaplan rengini belirler.


mainloop() #pencereyi döngüye soktuk ki kapanmasın.
