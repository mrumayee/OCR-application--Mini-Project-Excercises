import cv2
capture=cv2.VideoCapture(0)
count=0
while True:
    
    x,frame=capture.read()
    cv2.imshow('Image',frame)
    cv2.imwrite('IMG_'+str(count)+'.jpg',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    count+=1
