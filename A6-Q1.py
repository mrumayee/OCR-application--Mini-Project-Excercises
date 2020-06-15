import cv2
import numpy as np
image=cv2.imread("pic.jpg")
image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((25,25))/625

blur = cv2.filter2D(image_gray,-1,kernel)
dilate = cv2.dilate(image_gray,kernel)

canny = cv2.Canny(dilate,50,200)
cv2.namedWindow ('canny', cv2.WINDOW_NORMAL)
cv2.namedWindow ('dilate', cv2.WINDOW_NORMAL)
cv2.imshow("dilate",dilate)
cv2.imshow("canny",canny)
cv2.waitKey(0)
