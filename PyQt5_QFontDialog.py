from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.label = QLabel("Deneme Yazısı")
        self.button = QPushButton("Değiştir")
        v_box = QVBoxLayout()   
        form = QFormLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.button)
        form.addRow(v_box)
        self.setLayout(form)
        self.button.clicked.connect(self.uygula)
        self.show()
    def uygula(self):
        alinanQfontObjesi,durum = QFontDialog.getFont() 
        if durum:
            self.label.setFont(alinanQfontObjesi)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())

