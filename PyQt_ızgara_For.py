from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(150,150,300,300)

    izgara = QGridLayout(window)  #window.setlayout(izgara) diyerekte izgarayı ekranımıza ekleyebiliriz.
    for i in range(1,7):
        for j in range(1,7):
            izgara.addWidget(QPushButton("Buton Satır:{}, Sutun:{} ".format(i,j) ),i,j)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
