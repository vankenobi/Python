import cv2
import numpy as np

kamera = cv2.VideoCapture(1)
kamera.set(3,300)
kamera.set(4,300)
alcak = np.array([88,50,50])
yuksek = np.array([130,255,255])


while True:
    ret,goruntu = kamera.read()
    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    mavi = cv2.inRange(hsv,alcak,yuksek)
    wise = cv2.bitwise_and(goruntu,goruntu,mask=mavi)
    kernel = np.ones((5,5),np.uint8)

    erosion = cv2.erode(mavi,kernel,iterations=1)
    diolation = cv2.dilate(mavi,kernel,iterations=1)

    opening = cv2.morphologyEx(mavi,cv2.MORPH_OPEN,kernel)
    closing =cv2.morphologyEx(mavi,cv2.MORPH_CLOSE,kernel)

    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)
    cv2.imshow("erosion",erosion)
    cv2.imshow("diolation",diolation)
    cv2.imshow("wise",wise)
    cv2.imshow("Mavi",mavi)
    cv2.imshow("hsv", hsv)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()

