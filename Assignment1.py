import cv2
cap  =  cv2.VideoCapture(0)

counter = 0
n = int(input("enter the value of n:"))
while True:
    x,frame = cap.read()
    counter = counter + 1
     
    if counter%n ==0 :
        flipped =  cv2.flip(frame,-1) 
        cv2.imshow("image",flipped)
    else:
        cv2.imshow("image",frame)   
    if cv2.waitKey(5) & 0xFF==ord('a') :
        break 
