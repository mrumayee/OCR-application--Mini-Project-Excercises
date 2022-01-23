
# Optical Recognition Application

**Installation**



The following code can be executed using any code editor(VS,Pycharm,etc). To run this application we are required to install libraries such as

Open CV
Tkinter
PIL
Tesseract.


We can do the above by simply typing “pip install name-python”.
2.	But for installation of tesseract(library mainly used for ocr application) ,you have to download the tesseract library and then during the installation process you have to select the languages for which the above library tesseract should work for(if selected nothing then by default only English language is selected).Then finally go to the command prompt and write ‘pip install tesseract’ and tesseract is finally installed and you can start your coding.
3.	OpenCV already contains many pre-trained classifiers for face, eyes, smile etc. Those XML files are stored in OpenCV/data/haarcascades/ folder. We need to download it 
In this application like for accessing photos in the directory of your computer you have to change the directory name as per your need in the code since different system have different locations where images are stored. 
4.	For example (‘Users/Desktop/’ can be changed to ‘E:\’)


**Working of GUI app: -** 

We have created button using Tkinter.  which perform certain functions on the images selected. We have also created a textbox to display the recognized information in OCR. We can perform different operations on images using this app.

1. **Browse** – This button helps you select an image. 

2. **Blur image** – This button helps you perform Gaussian blur on the image after converting it to gray scale. 

3. **Auto Crop Image** – This button finds four different edges which are most appropriate according to the large change in the color of the pixels which are adjacent to each other and forms a closed loop around those 4 points and crops the image automatically using contours. 

4. **Manual Crop** – We can select any 4 different points manually and the image will be cropped using array slicing. 

5. **Canny**– This button helps to canny an gray scale image which is used for edge detection. 

6. **Webcam** – This button helps to use the live web cam for face detection and to capture a image. 

7. **OCR** – This button helps us to find if there are any characters of English in the image by highlighting it in green colored rectangle and displays the text above it in blue color. 

8. **Show Text** – This button shows the text detected in the text box.

9. **Save Image** – This button saves the image displayed after applying various function on it. imwrite function is used for the same 

10.**Save M. Crop Image**- This button is specially designed to save the manually cropped image.

11. **Original**– This button helps you get the original image before any changes.

12. **Clear** – This button is used to clear the window.

13.**Rotate**-This is used to rotate the image by 90 degree clockwise

14.Flip- It is used to flip the image vertically.


