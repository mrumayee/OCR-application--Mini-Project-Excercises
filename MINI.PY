from tkinter import *
import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image,ImageTk
import cv2
import numpy as np
import pytesseract
from pytesseract import Output

#from Backend_v2 import mouse,warp_function,Get_Image,blur_function,ocr_function,save_img,auto_crop
#og=np.zeros((),np.uint8)
my_image=np.zeros((),np.uint8)

root = tk.Tk()

def select_image():
    filename = filedialog.askopenfilename(initialdir = "/Users/anishpawar/",title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    print(filename)
    global og
    global my_image
    OG = cv2.imread(filename)
    og=cv2.resize(OG,(700,700))
    cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
    
    my_image=og.copy()
    cv2.imshow('frame',og)
    
def show_original_image():
    cv2.imshow("frame",og)
    
def live_webcam():
    cap=cv2.VideoCapture(0)
    while True:
        x,shot=cap.read()
        face_cascade=cv2.CascadeClassifier("face.xml")
        gray_scale=cv2.cvtColor(shot,cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray_scale,1.1,4)
        for (x,y,w,h) in face:
            cv2.rectangle(shot,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow("screen",shot)
            cv2.imwrite("capture.jpg",shot)
        if cv2.waitKey(1)    & 0xFF== ord('q'):
            break
    cap.release()
    cvq 
     

def blur_image():
    global my_image
    

    gray_photo=cv2.cvtColor(og,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((3,3))
    blur=cv2.GaussianBlur(gray_photo,(5,5),3)
    my_image=blur.copy()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.imshow("frame",blur)
    
def canny():
    global my_image
    gray_photo=cv2.cvtColor(og,cv2.COLOR_BGR2GRAY)
    edges= cv2.Canny(gray_photo,50,200)
    my_image=edges.copy()
    cv2.imshow("frame",edges)

     
           
    
def destroy_btn():
    cv2.destroyAllWindows()

count=0
point=np.zeros((4,2),np.float32)
def manual_button_click():
    def mouse(event,x,y,flag,para):
        global count 
        global point
        global cropped
        if event==cv2.EVENT_LBUTTONDOWN:
            
            point[count]=x,y
            count=count+1
            
        if count == 4:
                
                pts_1 = np.float32([point[0],point[1], point[2], point[3]])
                pts_2 = np.float32([(0, 0), (500,0), (0,600), (500,600)])
                perspective = cv2.getPerspectiveTransform(pts_1,pts_2)
                cropped = cv2.warpPerspective(og, perspective, (500,600))            
                my_image=cropped.copy()
                cv2.imshow('img',cropped)
                
                
    cv2.namedWindow("frame")
    cv2.setMouseCallback("frame",mouse)



def auto_crop():
    global my_image,og
    image=cv2.cvtColor(og,cv2.COLOR_BGR2GRAY)

    gaussian_blur=cv2.GaussianBlur(image,(3,3),2)
    canny =cv2.Canny(gaussian_blur,130,180)

    contours,heirarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour=contours[max_index]

    perimeter=cv2.arcLength(max_contour,True)
    co_ordinates=cv2.approxPolyDP(max_contour,0.01*perimeter,True)
    cv2.drawContours(og,[co_ordinates],-1,(0,255,0),2)

    pts_1=np.array([co_ordinates[0],co_ordinates[1],co_ordinates[3],co_ordinates[2]],np.float32)
    pts_2=np.array([(0,0),(500,0),(0,600),(500,600)],np.float32)
    perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
    transformed=cv2.warpPerspective(og,perspective,(500,500))

    my_image=transformed.copy()
    cv2.imshow('tramsformed',transformed)


def ocr():
    global content ,my_image
    content = pytesseract.image_to_string(og,lang= 'eng')
    
    data=pytesseract.image_to_data(og,lang="eng",output_type=Output.DICT)
    no_word=len(data['text'])
    for i in range(no_word):
        if int(data['conf'][i]) > 50:
            x,y,w,h = data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(og,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(og,data['text'][i],(x,y),cv2.FONT_ITALIC,0.5,(255,0,0),1)
            cv2.waitKey(1)
    my_image=og.copy()
    cv2.imshow("frame",og)  

def detect_text():
    text_box=Text(frame,bg='#FDFFD6')
    text_box.place(relx = 0.25,rely = 0.2,relwidth =0.5,relheight =0.6)
    text_box.insert(END,content)



counter=0
def save_img():
    global counter
    global my_image
    counter+=1
    cv2.imwrite('image_'+str(counter) + '.jpg', my_image)
    
no=0
def save_manual_crop():
    global cropped
    global no
    no+=1 
    cv2.imwrite("cropped_image_"+str(no)+'.jpg', cropped)  

def flip():
    global my_image
    flipped=cv2.flip(og,-1)
    my_image=flipped.copy()
    cv2.imshow('frame',flipped)

def rotate():
    global new_img
    rotate=cv2.rotate(og,cv2.ROTATE_90_CLOCKWISE)
    my_image=rotate.copy()
    cv2.imshow('frame',rotate) 

          

canvas = tk.Canvas(root,height = 900,width = 900,bg = '#EFF294')
canvas.pack()

frame = tk.Frame(canvas,bg = 'white')
frame.place(relx = 0.1,rely = 0.1,relwidth =0.8,relheight =0.8)

label=tk.Label(frame,text="Detected Text",fg="blue",bg = 'white',font=("Ariel",30))
label.place(relx=0.35,rely=0.1)

dummy_btn = tk.Button(frame,text = 'Browse',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5, command = select_image)
dummy_btn.place(relx=0.05,rely=0.15)

ocr_btn=tk.Button(frame,text = 'O.C.R',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5, command = ocr)
ocr_btn.place(relx=0.05,rely=0.25)

manual_crop_btn=tk.Button(frame,text = 'Manual crop',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5, command = manual_button_click)
manual_crop_btn.place(relx=0.05,rely=0.35)

auto_btn=Button(frame,text = 'Auto Crop',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5, command = auto_crop)
auto_btn.place(relx=0.05,rely=0.45)


blur_btn=tk.Button(frame,text = 'Blur',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5, command = blur_image)
blur_btn.place(relx=0.8,rely=0.55)

live_cam_btn=tk.Button(frame,text="Webcam",fg="black",bg="#F6D8E2",font=("Times"),padx=5,pady=5,command=live_webcam)
live_cam_btn.place(relx=0.8,rely=0.15)


og_image_btn = tk.Button(frame,text = 'Original',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5, command = show_original_image)
og_image_btn.place(relx=0.05,rely=0.75)


destroy_btn=tk.Button(frame,text = "Clear",fg = 'black',bg="#F6D8E2",font=("Times"),padx = 5,pady = 5, command = destroy_btn)
destroy_btn.place(relx=0.8,rely=0.75)

rotate_btn=tk.Button(frame,text = 'Rotate',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5 ,command =rotate)
rotate_btn.place(relx=0.05,rely=0.65)

flip_btn=tk.Button(frame,text = 'Flip',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5 ,command =flip)
flip_btn.place(relx=0.8,rely=0.65) 

show_txt_btn=tk.Button(frame,text = 'Show Text',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5 ,command =detect_text)
show_txt_btn.place(relx=0.8,rely=0.35)

canny_btn=tk.Button(frame,text = 'Canny',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5 ,command =canny)
canny_btn.place(relx=0.8,rely=0.25)

save_btn=tk.Button(frame,text = 'Save Image',fg = 'black',bg="#F6D8E2",font=("Times"),padx=5,pady=5 ,command =save_img)
save_btn.place(relx=0.8,rely=0.45)

save_manual=tk.Button(frame,text = 'Save M.Crop',fg = 'black',bg="#F6D8E2",font=("Times"),padx=4.4,pady=4.4 ,command =save_manual_crop)
save_manual.place(relx=0.05,rely=0.55)


root.mainloop()