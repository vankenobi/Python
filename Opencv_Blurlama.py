import cv2
import numpy as np
kamera = cv2.VideoCapture(1)

alcak = np.array([105,50,50])
yuksek = np.array([130,255,255])

kamera.set(3,300)
kamera.set(4,300)

while True:
    ret,goruntu = kamera.read()
    #Orjinali

    cv2.imshow("Orjinal Goruntu",goruntu)

    #Gri görüntü

    gri_goruntu = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gri Goruntu",gri_goruntu)

    #hsv li görüntüBGR2HSV)

    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    hsvli_goruntu = cv2.inRange(hsv,alcak,yuksek)
    cv2.imshow("Hsvli goruntu",hsvli_goruntu)

    #maskeleme

    mask = cv2.bitwise_and(goruntu,goruntu,mask=hsvli_goruntu)
    cv2.imshow("Maskelenen Goruntu",mask)

    #Blurlu_Goruntu

    median = cv2.medianBlur(mask,15)

    cv2.imshow("Blurlu Goruntu",median)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # Bilateral
    bilateral = cv2.bilateralFilter(goruntu,15,15,15)
    cv2.imshow("Bilateral",bilateral)

kamera.release()
cv2.destroyAllWindows()
