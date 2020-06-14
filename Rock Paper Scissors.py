import random
import os

def karar(hamleo,hamleb):
    if hamleo == hamleb:
        print("Sonuç : Berabere")
    elif hamleo == "taş" and hamleb == "kağıt":
        print("Sonuç : Bot Eddy kazandı.")
    elif hamleb == "taş" and hamleo == "kağıt":
        print("Sonuç : Oyuncu kazandı.")
    elif hamleo == "kağıt" and hamleb == "makas":
        print("Sonuç : Bot Eddy kazandı.")
    elif hamleb == "kağıt" and hamleo == "makas":
        print("Sonuç : Oyuncu kazandı.")
    elif hamleo == "makas" and hamleb == "taş":
        print("Sonuç : Bot Eddy kazandı.")
    elif hamleb == "makas" and hamleo == "taş":
        print("Sonuç : Oyuncu kazandı.")

class Oyuncu():
    def hamlegir(self):
       hamle = input("Hamleni gir(taş,kağıt,makas):")
       return hamle

class Bot():

    def __init__(self):
        self.isim = "BOT Eddy"
    def hamle(self):
       rand = random.randint(1,4)
       if rand == 1:
           hamle = "taş"
           print("Bot Eddy'nin hamlesi:",hamle)
           return hamle
       elif rand == 2:
           hamle = "kağıt"
           print("Bot Eddy'nin hamlesi:", hamle)
           return hamle
       elif rand == 3:
           hamle = "makas"
           print("Bot Eddy'nin hamlesi:", hamle)
           return hamle




while True:

    b = Bot()
    o = Oyuncu()

    print("Oyun Başladı Keyifli Oyunlar")


    hamleo = o.hamlegir()
    hamleb = b.hamle()

    karar(hamleo,hamleb)




