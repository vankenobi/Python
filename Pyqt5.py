v
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


import sys
def mesaj1():
    print("Mesaj 1 görüntülendi.")
def mesaj2():
    print("Mesaj 2 görüntülendi.")
def pencere ():
    app = QApplication(sys.argv)
    window = QWidget()

    h_box = QHBoxLayout()
    v_box = QVBoxLayout()

    buton1 = QPushButton(window)
    buton1.setText("Buton 1")

    buton3 = QPushButton(window)
    buton3.setText("Buton 3")

    buton2 = QPushButton(window)
    buton2.setText("Buton 2")

    buton4 = QPushButton(window)
    buton4.setText("Buton 4")

    h_box.addWidget(buton3)
    h_box.addWidget(buton4)

    v_box.addWidget(buton1)
    v_box.addWidget(buton2)

    v_box.addLayout(h_box)

    window.setLayout(v_box)
    window.setLayout(h_box)

    window.setWindowTitle("Kütüphane Uygulaması")
    window.setGeometry(150,150,500,500)
    window.show()
    sys.exit((app.exec()))

if __name__== "__main__":

    pencere()
