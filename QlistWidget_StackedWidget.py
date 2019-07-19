from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        h_box = QHBoxLayout()
        self.liste = QListWidget() #ListWidget oluşturduk
        self.liste.insertItem(0,"Firma") #list widgetta gösterilenlerin isimleri ve indisleri girdik.
        self.liste.insertItem(1,"Hakkımızda")
        self.liste.insertItem(2,"Bize Ulaşın")

        self.stackedwidget = QStackedWidget() #StackedWidget oluşturduk

        self.w1 = QWidget() # 3 tane Qwidget oluşturduk.
        self.w2 = QWidget()
        self.w3 = QWidget()

        self.w1lay() #Fonksiyonları çağırdık
        self.w2lay()
        self.w3lay()

        self.stackedwidget.addWidget(self.w1) #QWidgetları Stackedwidget içine ekledik.
        self.stackedwidget.addWidget(self.w2)
        self.stackedwidget.addWidget(self.w3)
        
        h_box.addWidget(self.liste)
        h_box.addWidget(self.stackedwidget)

        self.setLayout(h_box)
        self.liste.currentRowChanged.connect(self.uygula) #listWidgetta listedeki herhangi bir elemana basıldığında uygula fonk'a git.
        self.show()
    def uygula(self,q):
        self.stackedwidget.setCurrentIndex(q) #basılan seçeneğin sinyalini ....
         
    def w1lay(self):
        form = QFormLayout()
        form.addRow("Adınız:",QLineEdit())
        form.addRow("Yaşınız:",QSpinBox()) 
        form.addRow("Kabul Ediyor musunuz:",QCheckBox())
        self.w1.setLayout(form)
    def w2lay(self):
        form = QFormLayout()
        form.addRow("karakteriniz:",QLineEdit())
        form.addRow("ayak numaraznız:",QSpinBox()) 
        form.addRow("Kabul Ediyor musunuz:",QCheckBox())
        self.w2.setLayout(form)
    def w3lay(self):
        form = QFormLayout()
        form.addRow("Adınız:",QLineEdit())
        form.addRow("bardak sayısı:",QSpinBox()) 
        form.addRow("Kabul Ediyor musunuz:",QCheckBox())
        self.w3.setLayout(form)
def ana():
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
if __name__ == "__main__":
    ana()
