import cv2
import numpy as np
foto = cv2.imread("Tyler.jpg")
"""
foto[100:200,300:400,0] = 255
cv2.imshow("Tyler Durden Blue",foto) # Resimdeki mavi renk tonunu ağır bastırır.

foto[:,:,1] = 255
cv2.imshow("Tyler Durden Green",foto)
"""

foto[:,:,2] = 255
cv2.imshow("Tyler Durden Red",foto)

cv2.waitKey(0)
cv2.destroyAllWindows()
