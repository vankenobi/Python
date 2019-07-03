import os
kitaplistesi = list()
kitap = ()

def kitapekle(kitap:tuple,liste:list):

    liste.append(kitap)
    print("Ekleme işlemi tamamlandı")
    print("Ana Menüye dönmek için 'Enter' a basın.")
    input()
def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False
def kitap_listele(liste:list):
    for i in liste:
        print("Kitap adi: {} Kitabin yazari: {}".format(i[0],i[1]))
def kitap_cikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste) == True:
        liste.remove(kitap)
    else:
        print("Boyle bir kitap bulunamadı")
    
menu = """
       [1]Kitap Ekle
       [2]Kitap Listele
       [3]Kitap çıkar
       [Q]Çıkış       
       """

while True:
    os.system("cls")
    print(menu)
    secim = input("Lutfen Seciminizi yapiniz:")
    if secim == "1":

        kitap_adi = input("Kitap Adi giriniz:")
        kitap_yazar = input("Kitabın yazarini giriniz:")
        kitap = (kitap_adi,kitap_yazar)
        kitapekle(kitap,kitaplistesi) #Kitap Ekleniyor

    elif secim == "2":
        kitap_listele(kitaplistesi)
        input()

    elif secim == "3":
        kitap_adi = input("Kitap Adi giriniz:")
        kitap_yazar = input("Kitabın yazarini giriniz:")
        kitap = (kitap_adi,kitap_yazar)
        kitap_cikar(kitap,kitaplistesi)

    elif secim == "q" or secim == "Q":
        print("Keyifli Okumalar.")
        quit()
    else:
        print("Hatalı tuşlama yaptiniz.")
    
    

    
        
 
