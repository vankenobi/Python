from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere ():
    app = QApplication(sys.argv)
    window = QWidget()
    yazi = QLabel(window) #label ekledik.
    yazi.setText("Bu Programda olan bir yazi") #labelin içinde yazan yazıyı değiştirdik.
    yazi.move(50,50) #labelin form ekranındaki konumunu belirledik.
    window.setWindowTitle("Kütüphane Otomasyonu") #Form ekranının başlığı.
    window.setGeometry(200,200,300,300) #ilk iki parametre form ekranının konumu
    window.show()                       #Sonraki iki parametre genişlik ve yükseklik
    sys.exit(app.exec())
if __name__ =="__main__":
    pencere()

