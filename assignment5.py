#Display upright images from the live webcam feed for 4 seconds. The images during the 
# 5 th second should be vertically inverted. This cycle of upright-inverted images should
# continue till the program terminates. You should be able to demonstrate at-least 3 cycles of
# this pattern.
import cv2
import time
capture=cv2.VideoCapture(0)
start_time=0
start_time=time.time()

while True:
    end_time=time.time()
    diff=int(start_time-end_time)
    print(diff)
    x,frame=capture.read()
    flipped=cv2.flip(frame,-1)
    if diff%5==0:
        cv2.imshow("image",flipped)
    else:
        cv2.imshow("image",frame)
    if cv2.waitKey(23) & 0xFF==ord('a') :
        break