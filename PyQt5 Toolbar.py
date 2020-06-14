from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Ana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        
        self.ara = QLineEdit()
        self.ara.setPlaceholderText("Ara")
        self.button = QPushButton("Gönder")
        
        toolbar = self.addToolBar("Dosya")
        toolbar2 = self.addToolBar("Düzenle")
        #Toolbara eleman ekleme
        temizle = QAction(QIcon("/home/musa/Desktop/rubbish.png"),"Temizle",self)
        toolbar2.addAction(temizle)

        engel = QAction(QIcon("/home/musa/Desktop/Çarpı.png"),"Çarpı",self)
        toolbar2.addAction(engel)
        
        kaydet = QAction(QIcon("/home/musa/Desktop/save.png"),"Kaydet",self)
        toolbar.addAction(kaydet)

        yazdır = QAction(QIcon("/home/musa/Desktop/printer.png"),"Yazdır",self)
        toolbar.addAction(yazdır)

        yeni_dosya = QAction(QIcon("/home/musa/Desktop/add.png"),"Yeni Dosya",self)
        toolbar.addAction(yeni_dosya) 
        #Toolbara Widget Ekleme
        toolbar2.addWidget(self.ara)
        toolbar2.addWidget(self.button)
        #Toolbarın Hareketini engeller
        toolbar.setMovable(True)
        #Toolbar Konumunu belirler
        toolbar.setOrientation(Qt.Vertical)
        #Toolbarın içinde herhangi bir butona basıldığında uygula fonksiyonu çalışsın
        toolbar.actionTriggered.connect(self.uygula)
 
        self.setGeometry(100,100,300,300)
        self.show()
        #Aşağıdaki Q bir sinyal 
    def uygula(self,q):
        print(q.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
