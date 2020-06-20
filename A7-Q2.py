import cv2
import numpy as np 

img_1=cv2.imread('pic.jpg')

img_2=cv2.resize(img_1,(512,512))
image=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)

gaussian_blur=cv2.GaussianBlur(image,(3,3),2)
canny =cv2.Canny(gaussian_blur,130,180)

contours,heirarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
areas=[cv2.contourArea(c) for c in contours]
max_index=np.argmax(areas)
max_contour=contours[max_index]

perimeter=cv2.arcLength(max_contour,True)
co_ordinates=cv2.approxPolyDP(max_contour,0.01*perimeter,True)
cv2.drawContours(img_2,[co_ordinates],-1,(0,255,0),2)

pts_1=np.array([co_ordinates[0],co_ordinates[1],co_ordinates[3],co_ordinates[2]],np.float32)
pts_2=np.array([(0,0),(500,0),(0,600),(500,600)],np.float32)
perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
transformed=cv2.warpPerspective(img_2,perspective,(500,500))

cv2.imshow('img',img_2)
cv2.imshow('tramsformed',transformed)


cv2.waitKey(0)