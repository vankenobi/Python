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
        dosya = menu.addMenu("Dosya")
        duzen = menu.addMenu("Düzen")
        yardım = menu.addMenu("Yardım")

        yeni_dosya = dosya.addAction("Yeni Dosya")
        dosya_aç = dosya.addAction("Dosya Aç")
        kaydet = dosya.addAction("Kaydet")
        yazdir = QAction("yazdir",self)
        temizle = duzen.addAction("Temizle")

        #QAction objesi gönderdim
        ayarlar = dosya.addMenu("Ayarlar")
        ayarlar.addAction("Ses Ayarları")
        ayarlar.addAction("Görüntü Ayarları")
        ayarlar.addAction("Sistem Ayarları")
        
        

        yazdir.setShortcut("Ctrl+P")
        kaydet.setIcon(QIcon("/home/musa/Desktop/save.png"))
        yazdir.setIcon(QIcon("/home/musa/Desktop/printer.png"))
        yeni_dosya.setIcon(QIcon("/home/musa/Desktop/add.png"))
        temizle.setIcon(QIcon("/home/musa/Desktop/rubbish.png"))

        self.setWindowTitle("Menu_bar")
        self.setGeometry(150,150,300,300)
        self.show()


        




        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
