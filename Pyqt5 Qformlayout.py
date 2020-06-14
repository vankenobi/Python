from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():

    app = QApplication(sys.argv)
    window = QWidget()

    form = QFormLayout()
    form.addRow(QLabel("isim: "),QLineEdit())
    lb = QLabel("Cinsiyet:")
    rd1 = QRadioButton("Erkek")
    rd2 = QRadioButton("Kadın")

    h_box = QHBoxLayout()
    h_box.addWidget(rd1)
    h_box.addStretch()
    h_box.addWidget(rd2)

    form.addRow(lb, h_box)
    form.addRow(QPushButton("Gönder"))

    window.setLayout(form)


    window.show()
    sys.exit(app.exec())
if __name__ =="__main__":
    pencere()
