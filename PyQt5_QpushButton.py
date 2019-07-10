from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Pencere(QWidget): #QtWidget alt class
    def __init__(self):
        super().__init__()
        self.setUI() #Özellik eklemek için var.
    def setUI(self):

        self.label = QLabel()

        button = QPushButton()
        button.setIcon(QIcon("return.png")) #butona ıcon ekledik (not:icon .p dosyası ile aynı dizinde olması gerekiyor.)

        button2 = QPushButton()
        button2.setIcon(QIcon("return.png"))  # butona ıcon ekledik (not:icon .p dosyası ile aynı dizinde olması gerekiyor.)

        button3 = QPushButton()
        button3.setIcon(QIcon("return.png"))  # butona ıcon ekledik (not:icon .p dosyası ile aynı dizinde olması gerekiyor.)

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(button)
        v_box.addWidget(button2)
        v_box.addWidget(button3)

        self.setLayout(v_box)
        button.setText("buton1")
        button2.setText("buton2")
        button3.setText("buton3")
        button.clicked.connect(lambda:self.yap(button))
        button2.clicked.connect(lambda:self.yap(button2))
        button3.clicked.connect(lambda:self.yap(button3))

        self.show()
    def yap(self,e):
        self.label.setText(e.text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere() # Pencere sınıfından bir nesne oluşturduk.
    sys.exit(app.exec())
