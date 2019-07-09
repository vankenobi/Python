from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
   def giriş():
       if g1.text() == "musa" and g2.text() == "küçük":
           durumlabel.setText("Giriş Başarılı")
       else:
           durumlabel.setText("Giriş Başarısız")
           g1.clear()
           g2.clear() # textbox içerisindeki yazıyı siler


   app = QApplication(sys.argv)
   window = QWidget()
   form = QFormLayout() #Form adında bir form layout oluşturduk.

   g1 = QLineEdit()  #g1 ve g2 adında textbox oluşturduk.
   g2 = QLineEdit()
   g2.setEchoMode(QLineEdit.Password) #textin parola şeklinde yazılmasını sağlar.

   durumlabel = QLabel()
   # textbox.setInputMask("+90-999-999-99-99")  Yazıyı kalıplara ayıtmak ör:tel no
   button = QPushButton(window)
   button.setText("Bağlan")
   button.clicked.connect(giriş) #Buton basıldığında fonksiyona yönlendiriyor.

   form.addRow(QLabel("Kullanıcı Adı:"),g1)
   form.addRow(QLabel("Şifre:"),g2)

   form.addRow(button)
   form.addRow(durumlabel)
   window.setLayout(form)
   window.setWindowTitle("Kullanıcı Paneli")
   window.show()
   sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
