import cv2
import numpy as np

kamera = cv2.VideoCapture(1)
dusuk = np.array([25,50,50])
yuksek = np.array([33,255,255])

while True:
    ret,goruntu = kamera.read()
    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV) #goruntuyu hsv cam e dönüştürüyor.
    cv2.imshow("Goruntu",goruntu)
    Duzenlenmis = cv2.inRange(hsv,dusuk,yuksek) #Alınan hsv görünütüsünde (istenen rengin) hsv değerlerini belirliyor.
    cv2.imshow("Duzenlenmiş",Duzenlenmis)
    maskeleme = cv2.bitwise_and(goruntu,goruntu,mask=Duzenlenmis) #8 bit lik pixelleri and operatörüyle karşılaştırıyor.
    cv2.imshow("Maskelenmis",maskeleme)
    #BULANIKLAŞTIRMA
    kernel = np.ones((15, 15), dtype=np.float32) / 225
    smothed = cv2.filter2D(maskeleme,-1,kernel)
    #BLURLAMA
    cv2.imshow("Smoth goruntu",smothed) #smothlanan görüntüyü ekrana çıkardık.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()



