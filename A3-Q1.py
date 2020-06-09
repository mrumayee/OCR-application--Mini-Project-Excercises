import cv2
import random
image=cv2.imread("index.jpg")
size=image.shape
x1=int(size[0]/7)
y1=int(size[1]/7)
print(x1)
print(y1)

j=0
for j in range(1,size[1],1):
    i=0
    while i<=size[0]:
        cv2.rectangle(image,(i,j),(i+x1,j+y1),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        i=i+x1
       
       
      
    j=j+y1    
cv2.imshow("frame",image)
cv2.waitKey(0)
