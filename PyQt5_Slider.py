from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        
        # self.setGeometry(100,100,300,300)
        self.label_1 = QLabel("Değer:")
        self.label_2 = QLabel()
        self.qs = QSlider(Qt.Horizontal) # içerisine aldığı parametre slideın dikeymi yataymı olacağını belirler.
        self.qs.setTickPosition(QSlider.TicksBelow) # Qslider altına derecelendirme yapar.
        self.qs.setGeometry(0,150,70,120) 
        self.qs.setMinimum(100) #Minimum alacağı değer
        self.qs.setMaximum(500) #Maksimum alacağı değer
        self.qs.setSingleStep(1) #Artış azalış miktarı
        form = QFormLayout()
        h_box = QHBoxLayout()
        v_box = QVBoxLayout()
        v_box.addWidget(self.qs)
        h_box.addWidget(self.label_1)
        h_box.addWidget(self.label_2)
        form.addRow(v_box)
        form.addRow(h_box)
        self.setLayout(form)
        self.qs.valueChanged.connect(self.yap) 
        #self.qs.sliderReleased.connect(self.yap)

                
        self.show()
    def yap(self):
        self.label_2.setText(str(self.qs.value()))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencre = Pencere()
    sys.exit(app.exec())

    """
    value.Changed()
    Kaydırıcının değerini değiştirdiğinde
    slider.Pressed
    Kullanıcı sliderı sürüklemeye başladığında
    slider.Moved()
    Kullanıcı kaydırıcıyı sürüklediğinde 
    slider.Released()
    Kullanıc kaydırıcıyı serbest bıraktığında
    """
