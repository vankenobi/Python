from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        form = QFormLayout()

        self.button1 = QPushButton("En sevdiğiniz dili seçin")
        self.button2 = QPushButton("İsminizi giriniz")
        self.button3 = QPushButton("Yaşınızı giriniz")

        self.giriş1 = QLineEdit()
        self.giriş2 = QLineEdit()
        self.giriş3 = QLineEdit()
        
        form.addRow(self.button1,self.giriş1)
        form.addRow(self.button2,self.giriş2)
        form.addRow(self.button3,self.giriş3)

        self.button1.clicked.connect(self.dil_al)
        self.button2.clicked.connect(self.isim_al)
        self.button3.clicked.connect(self.yas_al)

        self.setWindowTitle("QINPUT")
        self.setLayout(form)
        self.show()

    def yas_al(self):
        seçilen,tamam = QInputDialog.getInt(self,"Yaş","Yaşınızı Giriniz")
        if tamam:
            self.giriş3.setText(str(seçilen))

    def isim_al(self):
        seçilen,tamam = QInputDialog.getText(self,"İsim","İsiminizi Giriniz")
        if tamam:
            self.giriş2.setText(str(seçilen))

    def dil_al(self):
        diller = ("İngilizce","Fransızca","Türkçe","Japonca","İtalyanca","Çince")
        seçilen,tamam = QInputDialog.getItem(self,"Sevdiğiniz Dil","Sevdiğiniz Dili Seçiniz",diller,0,False)    
        if tamam:
            self.giriş1.setText(str(seçilen))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())

