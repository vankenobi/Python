from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):

        menu = self.menuBar()
        dosya = menu.addMenu("Dosya")  #menubar üzerine butonları ekledik
        duzen = menu.addMenu("Düzen")
        yardım = menu.addMenu("Yardım")

        
        yeni_dosya = dosya.addAction("Yeni Dosya") #Dosya butonununa alt seçenek ekliyoruz.
        dosya_aç = dosya.addAction("Dosya Aç") 
        kaydet = dosya.addAction("Kaydet")
        
        #Hazırla adında bir Qaction objesi oluşturduk.

        hazırla = QAction("hazırla",self) 
        hazırla.setShortcut("Ctrl+l) # Bir kısayol ekledik
        dosya.addAction(hazırla) #Dosya butonunun altına gönderdik.
    

        temizle = duzen.addAction("Temizle")
        sil = duzen.addAction("Sil")

        ayarlar = dosya.addMenu("Ayarlar") 
        
        ayarlar.addAction("Ses Ayarları")
        ayarlar.addAction("Görüntü Ayarları")
        ayarlar.addAction("Sistem Ayarları")
        
        kaydet.setIcon(QIcon("/home/musa/Desktop/save.png")) # Icon ekledik.
        yeni_dosya.setIcon(QIcon("/home/musa/Desktop/add.png"))
        temizle.setIcon(QIcon("/home/musa/Desktop/rubbish.png"))

        

        self.setWindowTitle("Menu_bar")
        self.setGeometry(150,150,300,300)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
