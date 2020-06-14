import cv2
import numpy as np

resim = cv2.imread("Tyler.jpg")
tablo = resim[100:400,200:400]

b,g,r = cv2.split(resim) # liste şeklinde gelen resimin renk (b,g,r) şekillerini sırayla b,g,r olarak tanımladı.

resim[0:200,0:200] = resim[100:300,200:400] # Resimin belirli bölgesini kesip orjinalinin sol üst köşesine yapıştırdı.

cv2.imshow("Tyler Durden Orjinal",resim)
cv2.imshow("Tyler Durden Blue",b)  # Resimde mavi olan yerleri açık beyaz yapıyor aynı şekilde diğerleride
cv2.imshow("Tyler Durden Green",g)
cv2.imshow("Tyler Durden Red",r)

yeni_resim = cv2.merge((b,g,r)) #bgr olarak ayrılmış resimi eski haline birleştiriyor. (merge = birleştirmek)
cv2.imshow("Merge edilmiş resim",yeni_resim)

cv2.imshow("Tyler kesilen",tablo) # kesilen resmi farklı bir pencerede gösteriyo

cv2.waitKey(0)
cv2.destroyAllWindows()
