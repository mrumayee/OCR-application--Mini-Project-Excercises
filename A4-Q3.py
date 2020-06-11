import cv2
import numpy as np

image=cv2.imread("card.png")

count=0
point=np.zeros((4,2),np.float32)

def mouse(event,x,y,flag,para):
    global count 
    global point
    if event==cv2.EVENT_LBUTTONDOWN:
        
        point[count]=x,y
        count=count+1
        print(point)
        print(f'the count is{count}')
    if count == 4:
            print("yeah we have four co ordinates")
            pts_1 = np.float32([point[0],point[1], point[2], point[3]])
            pts_2 = np.float32([(0, 0), (500,0), (0,600), (500,600)])
            perspective = cv2.getPerspectiveTransform(pts_1,pts_2)
            transformed = cv2.warpPerspective(image, perspective, (500,600))            

            cv2.imshow('img',transformed)
            cv2.imshow("frame",image)
            cv2.waitKey(0) 
           
        
        
        
    
cv2.namedWindow("frame")
cv2.setMouseCallback("frame",mouse)

cv2.imshow("frame",image)
cv2.waitKey(0)