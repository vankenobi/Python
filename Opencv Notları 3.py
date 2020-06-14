import cv2
import numpy as np

foto = cv2.imread("Tyler.jpg")
cv2.imshow("Tyler Reis",foto)

#Resmi Uzatma

uzatılan_resim = cv2.copyMakeBorder(foto,100,100,100,100,cv2.BORDER_REPLICATE)

#Resmi Aynalama

aynalanan_resim = cv2.copyMakeBorder(foto,100,100,100,100,cv2.BORDER_REFLECT)

#Resmi Tekrar Etme

tekrar_eden_resim = cv2.copyMakeBorder(foto,100,100,100,100,cv2.BORDER_WRAP)

#Resmin Etrafını Sarma

etrafı_sarılı_resim = cv2.copyMakeBorder(foto,100,100,100,100,cv2.BORDER_CONSTANT,value=[255,0,0])


cv2.imshow("Uzatılan Resim",uzatılan_resim)
cv2.imshow("Aynalanan Resim",aynalanan_resim)
cv2.imshow("Tekrar Eden Resim",tekrar_eden_resim)
cv2.imshow(" Etrafı Sarılı Resim",etrafı_sarılı_resim)



cv2.waitKey(0)
cv2.destroyAllWindows()
