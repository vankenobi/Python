from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.combo = QComboBox()
        self.label = QLabel("Bilgi")
        self.combo.addItems(self.ekle())

        v_box = QVBoxLayout()
        v_box.addWidget(self.combo)
        v_box.addWidget(self.label)
        self.combo.currentIndexChanged.connect(self.Hesapla)
        

        self.setLayout(v_box)
        self.show()
    def ekle(self):
        liste = [str(x) for x in range(1940,2020)]
        return liste
        
    def Hesapla(self):
        suankiyıl = 2019
        kullanıcı_dogum_tarihi = int(self.combo.currentText())
        sonuc = suankiyıl - kullanıcı_dogum_tarihi
        print("Yaşınız: {} ".format(sonuc))
        self.label.setText(str(sonuc))
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
