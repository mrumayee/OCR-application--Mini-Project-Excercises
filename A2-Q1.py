#strinking an image using image.shape.
import cv2
import random
image=cv2.imread('index.jpg')
random.randint(0,255)

size=image.shape
cv2.line(image,(0,0),(size[1],size[0]),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),6)
cv2.imshow('frame',image)
cv2.waitKey(0)
