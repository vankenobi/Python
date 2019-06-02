while(True):
    sayi = int(input("Lutfen negatif olmayan bir sayi giriniz:"))
    if (sayi < 0):
        print("girdiginiz sayi negatif olamaz.")
    else:
        for i in range(1,sayi):
            sayi *=i
        print(sayi)    
