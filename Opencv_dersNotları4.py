import cv2
import numpy as np

foto = cv2.imread("Tyler.jpg")
cv2.imshow("Tyler",foto)

cv2.rectangle(foto,(50,300),(300,50),[0,0,255],2) #Resim içerisine çerçeve dikdörtgen bir çerçeve çizmek için kullanılır.
cv2.imshow("Tyler",foto)

cv2.waitKey(0)
cv2.destroyAllWindows()
