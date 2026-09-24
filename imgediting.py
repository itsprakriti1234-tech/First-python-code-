import cv2
import numpy as python
import matplotlib.pyplot as plt
img = cv2.imread("C:/Users/PRAKRITI/OneDrive/Pictures/Screenshots/Screenshot 2026-09-23 001116.png")
print(type(img))
print(img.shape)
cv2.imshow("photos", img)
cv2.waitKey(0)
img_resize=cv2.resize(img,(500,356))
cv2.imshow("photos",img_resize)
cv2.waitKey(0)
img_flip=cv2.flip(img,0)
cv2.imshow("photos",img_flip)
cv2.waitKey(0)
img_crop=img[100:300, 200:500]
cv2.imshow("photos", img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
