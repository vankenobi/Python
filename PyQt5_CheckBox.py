from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Pencere(QWidget): #QtWidget alt class
    def __init__(self):
        super().__init__()
        self.setUI() #Özellik eklemek için var.
    def setUI(self):
        self.cb = QCheckBox("Kabul Ediyorum")
        self.cb2 = QCheckBox("Kabul Etmiyorum")
        form = QFormLayout()

        self.button = QPushButton("Gonder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.cb)
        v_box.addWidget(self.cb2)
        form.addRow(v_box)
        form.addRow(self.button)
        
        self.setLayout(form)
        self.button.clicked.connect(self.yap)
    
        self.show()
    def yap(self):
        if self.cb.isChecked():
            print("Anlaşma Kabul Edilmiştir.")
        elif self.cb2.isChecked():
            print("Anlaşma Kabul Edilmemiştir.")
        else:
            print("Henüz bir seçim yapılmadı.")  

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere() # Pencere sınıfından bir nesne oluşturduk.
    sys.exit(app.exec())
