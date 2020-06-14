from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

import sys  

class Pencere(QTabWidget):
    def __init__(self):
        super().__init__()
        
        self.tablo1  = QWidget() # Qwidget sınıfından tablo1 adında nesne oluşturduk.
        self.tablo2 = QWidget()
        self.tablo3 = QWidget()

        self.Tablo1UI() #Tablo1UI Fonksiyonunu çağırıyoruz.
        self.Tablo2UI()
        self.Tablo3UI()

        self.addTab(self.tablo1,"Bilgiler") # tab ekledik.
        self.addTab(self.tablo2,"Kahraman Seçimi")
        self.addTab(self.tablo3,"Giriş")

        self.setTabsClosable(True) # Tabların Yanlarında Çarpı işareti çıkar 

        self.setTabToolTip(0,"Kişisel bilgilerinizigirmeye yarar") #Tabın üzerine geldiğinizde bilgi verir 
        self.setTabToolTip(1,"Kahraman seçimi yapmanızı sağlar")
        self.setTabToolTip(2,"Resim mevcut") 

        self.tabCloseRequested.connect(self.kapat)

        self.setMovable(True) #Sekmelerin yerini değiştirebilme özelliğini aktif eder.
        self.setTabIcon(1,QIcon("/home/musa/Desktop/superman.png")) #Sekmenin başına Icon Ekler "1" indis değeridir.
        self.setTabShape(QTabWidget.Triangular) #Sekmelerin uçlarını yumuşatıyor.
        self.setTabPosition(QTabWidget.North) #Tabların konumunu alta aldı (north,south,east,Wet) 
        self.show()

    def Tablo1UI(self):
        form = QFormLayout()
        form.addRow("İsim:",QLineEdit())
        form.addRow("Yaşınız:",QSpinBox())
        self.tablo1.setLayout(form) 
    
    def Tablo2UI(self):
        form = QFormLayout()
        self.combo = QComboBox()
        self.combo.addItems(["SüperMan","Batman","SpiderMan"])
        
        form.addRow("Kahraman Seç",self.combo)
        form.addRow("Yıldız Sayısı",QLineEdit())
        self.tablo2.setLayout(form)
        


    def Tablo3UI(self):
        form = QFormLayout()
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label2.setText("PyQT5 Developer")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label1.setPixmap(QPixmap("/home/musa/Desktop/background.jpg"))
        self.label1.setAlignment(Qt.AlignCenter)  # Label1 objesini ortalıyor. 

        form.addRow(self.label1)
        form.addRow(self.label2)
        self.tablo3.setLayout(form)
    def kapat(self,q): 
        suanki_index = self.currentIndex() # şuanki index değerini döndürür.
        if suanki_index == q: #şuanki index q ya eşit ise geç
            pass
        else:
            self.removeTab(q) # değilse kapat
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())

