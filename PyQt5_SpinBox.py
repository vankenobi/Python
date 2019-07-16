from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.sp = QSpinBox()
        # self.sp = QDoubleSpinBox() #Ondalıklı Spin box
        v_box = QVBoxLayout()
        
        #self.sp.setMinimum(200) #Minimum Değer ayarlanır.
        #self.sp.setMaximum(500) #Maximum Deger ayarlanır.
        self.sp.setRange(20,2000) # min ve max aralığı belirler.
        self.sp.setValue(300) #Program başladığında çıkacak olan değer.
        
        self.sp.setSingleStep(5) # Artım oranını veriyor.

        v_box.addWidget(self.sp)
        self.setLayout(v_box)

        
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
