from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(150,150,300,300)

    izgara = QGridLayout(window)  #window.setlayout(izgara) diyerekte izgarayı ekranımıza ekleyebiliriz.
    izgara.addWidget(QPushButton("Buton 1"),1,1)
    izgara.addWidget(QPushButton("Buton 2"),1,2)
    izgara.addWidget(QPushButton("Buton 3"),1,3)
    izgara.addWidget(QPushButton("Buton 4"),2,1)
    izgara.addWidget(QPushButton("Buton 5"),2,2)
    izgara.addWidget(QPushButton("Buton 6"),2,3)
    izgara.addWidget(QPushButton("Buton 7"),3,1)
    izgara.addWidget(QPushButton("Buton 8"),3,2)
    izgara.addWidget(QPushButton("Buton 9"),3,3)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
    
    
