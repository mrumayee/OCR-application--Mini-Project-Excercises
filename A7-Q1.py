import cv2
import numpy as np

cap= cv2.VideoCapture(0)
cv2.namedWindow('frame')


def empty(x):
    print()


cv2.createTrackbar('h1','frame',0,180,empty)
cv2.createTrackbar('h2','frame',255,180,empty)

cv2.createTrackbar('s1','frame',0,255,empty)
cv2.createTrackbar('s2','frame',255,255,empty)

cv2.createTrackbar('v1','frame',0,255,empty)
cv2.createTrackbar('v2','frame',255,255,empty)

while True:

    ret,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h1=cv2.getTrackbarPos('h1','frame')
    h2=cv2.getTrackbarPos('h2','frame')
    s1=cv2.getTrackbarPos('s1','frame')
    s2=cv2.getTrackbarPos('s2','frame')
    v1=cv2.getTrackbarPos('v1','frame')
    v2=cv2.getTrackbarPos('v2','frame')



    lower_bound=np.array([h1,s1,v1])
    upper_bound=np.array([h2,h2,h2])

    mask_final=cv2.inRange(hsv_frame,lower_bound,upper_bound)
    res=cv2.bitwise_and(frame,frame,mask=mask_final)

    contours,_=cv2.findContours(mask_final,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour=contours[max_index]
    cv2.drawContours(frame,[max_contour],-1,(0,0,255),5)

    cv2.imshow('frame',frame)
    cv2.imshow('hsv',res)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break