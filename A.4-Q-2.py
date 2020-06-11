import cv2
import numpy as np
image=cv2.imread("index.jpg")
count=0
point= np.zeros((2,2),np.int)
def mouse(event,x,y,flag,para):
    global count
    global point
    if event==cv2.EVENT_LBUTTONDOWN:
        point[count]=x,y
        count=count+1
        print(count)
        print(point)
        if count==2:
            print("Yeahhhh we have two points")
            crop=image[point[0][0]:point[1][0],point[0][1]:point[1][1]]
            cv2.imshow("frame2",crop)
            cv2.waitKey(0)
        
        
                    
cv2.namedWindow("frame")
cv2.setMouseCallback("frame",mouse)
cv2.imshow("frame",image)
cv2.waitKey(0)
   


   


   
        


