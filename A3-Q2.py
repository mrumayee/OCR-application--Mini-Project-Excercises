import cv2
import random
image=cv2.imread("index.jpg")
size=image.shape
x1=int(size[0]/7)
y1=int(size[1]/7)
print(x1)
print(y1)
i=0
j=0
count=0
while j<=size[1] :
    
    count=count+1
    while i<=size[0] and i>=0:
        if count%2!=0:
            cv2.rectangle(image,(i,j),(i+x1,j+y1),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
            
            cv2.imshow("frame",image)
            cv2.waitKey(500)
            i=i+x1
           
        else:
            cv2.rectangle(image,(i,j),(i+x1,j+y1),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
            
            cv2.imshow("frame",image)
            cv2.waitKey(500)
            i=i-x1
           
    if count%2!=0:
        i=i-x1
    else:
        i=0

    j=j+y1                


cv2.imshow("frame",image)
cv2.waitKey(0)