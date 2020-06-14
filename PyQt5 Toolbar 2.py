from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(Pencere2()) # Program Başladığında Pencere2 yi ekrana verir.
        self.setUI()
    def setUI(self):
        self.setGeometry(300,300,250,250) # Program penceresinin boyutunu verir.

        menu = self.menuBar() #bir tane MenuBar oluşturduk.
        file = menu.addMenu("Dosya") # MenuBar ın içine Dosya adında seçenek ekledik
        file.addAction("Hakkımızda") #Menu barın içindeki dosyanın içine Hakkımızda kısmı ekledik. 

        toolbar = self.addToolBar("Dosya İşleri") # Dosyaİşleri adında Toolbar oluşturduk.

        house = QAction(QIcon("/home/musa/Desktop/house.png"),"house",self)
        toolbar.addAction(house)

        new = QAction(QIcon("/home/musa/Desktop/add.png"),"New",self)
        toolbar.addAction(new)

        _print = QAction(QIcon("/home/musa/Desktop/printer.png"),"Printer",self)
        toolbar.addAction(_print)

        info = QAction(QIcon("/home/musa/Desktop/information.png"),"İnfo",self)
        toolbar.addAction(info)

        kapat = QAction(QIcon("/home/musa/Desktop/Çarpı.png"),"kapat",self)
        toolbar.addAction(kapat)

        toolbar.actionTriggered.connect(self.new) #Toolbar içinde herhangi bir butona basıldığında fonk tetiklensin
        toolbar.actionTriggered.connect(self.Info)

        self.show()
    def new(self,q): # 'q' Parametresi sinyal alıyor.
        print(q.text())
        if q.text() == "New":
            self.setCentralWidget(Pencere3())
    def Info(self,q):
        print(q.text())
        if q.text() == "İnfo":
            self.setCentralWidget(Pencere2())
    def Çarpı(self,q):
        print(q.text())
        if q.text() == "kapat":
            self.close()


class Pencere2(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        form = QFormLayout()
        self.label = QLabel("2. Sayfa")
        self.button = QPushButton("3.sayfaya geç")
        form.addRow(self.label)
        form.addRow(self.button)
        self.setLayout(form)
        self.show()
               
class Pencere3(QWidget):      
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        form = QFormLayout()
        self.label = QLabel("3. Sayfa")
        form.addRow(self.label)
        self.setLayout(form)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Pencere = Pencere()
    sys.exit(app.exec())

