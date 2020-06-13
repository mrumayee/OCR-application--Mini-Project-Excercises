import cv2
import numpy as np

cap=cv2.VideoCapture(0)

counter=0
point= np.zeros((2,2),np.int)
def mouse(event,x,y,flags,param):
    
    global counter
    global points
    if event==cv2.EVENT_LBUTTONDOWN:
            point[counter]=x,y
            counter+=1
            cv2.imwrite('img.jpg',frame)
            
       

while True:
    x,frame=cap.read()
    
    img=cv2.imread('img.jpg')
    if counter==2:
        cropped=img[point[0][0]:point[1][0],point[0][1]:point[1][1]]
        cv2.imshow('cropped',cropped)
        template_gray=cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)#template matching requires gray scale images
        width=cropped.shape[1]
        height=cropped.shape[0]
    
        img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        resolution=cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED)
        loc=np.where(resolution>=0.9)
        
        for x,y in zip(*loc[::-1]):
            cv2.rectangle(frame,(x,y),(x+height,y+width),(0,255,0),1)
            cv2.putText(frame,'Object',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',mouse)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
