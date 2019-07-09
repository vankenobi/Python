from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():

   app = QApplication(sys.argv)
   window = QWidget()

   form = QFormLayout()
   form.addRow(QLabel("Kullanıcı Adı:"),QLineEdit())
   form.addRow(QLabel("Şifre:"),QLineEdit())
   form.addRow(QLabel("Adres:"),QLineEdit())


   rd1 = form.addRow(QRadioButton("Erkek"))
   rd2 = form.addRow(QRadioButton("Kadın"))
   label = QLabel("Cinsiyet:")

   h_box = QHBoxLayout()

   h_box.addWidget(rd1)
   h_box.addWidget(rd2)

   form.addRow(label,h_box)

   h_box2 = QHBoxLayout()
   h_box2.addWidget(QPushButton("Gönder"))
   h_box2.addWidget(QPushButton("İptal"))

   form.addRow(h_box2)

   window.setLayout(form)
   window.show()
   sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
