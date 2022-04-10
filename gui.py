from tkinter import Toplevel, filedialog, Label, Button, Tk
import cv2
from PIL import Image, ImageTk
import os

window = Tk()
window.title('Skin Cancer Checker')
window.resizable(width=False,height=False)
window.geometry('650x750')

label = Label(window)
label.grid(row=0,column=0)
  
cap = cv2.VideoCapture(0)
   

def restartApp():
    global window
    window.destroy()
    os.startfile("gui.py")
    
def display():
    cv2image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(20,display)

def replacewebcam():
    #label = Label(window)
    label.grid(row=0,column=0)
    img2=ImageTk.PhotoImage(Image.open("current_display.jpg"))
    label.configure(image=img2)
    label.image=img2

    
def takeImage():
    img_1 = ImageTk.getimage(label.imgtk)
    copy = img_1.convert('RGB')
    copy.save('current_display.jpg')
    display = copy
    copy = copy.resize((450,600),Image.ANTIALIAS)
    copy.save('current.jpg')
    cap.release()
    
    
def selectImage():
    filename = filedialog.askopenfilename(title='Open Image')
    copy = Image.open(filename)
    copy.save('current_display.jpg')
    display = copy
    copy = copy.resize((450,600),Image.ANTIALIAS)
    copy.save('current.jpg')
    

def computePrediction():
    #current.jpg is the file for processing, at ./
    print("asdf")
    
def takeandreplace():
    takeImage()
    replacewebcam()

def selectandreplace():
    selectImage()
    replacewebcam()


take_image = Button(window,text="Take Picture", command=takeandreplace)
take_image.grid(row=1,column=0)

select_image = Button(window,text="Select Image",command=selectandreplace)
select_image.grid(row=2,column=0)

compute_btn = Button(window,text="Compute Prediction",command=computePrediction)
compute_btn.grid(row=3,column=0)

camera_btn = Button(window, text="camera", command = display)
camera_btn.grid(row=7,column=0)

reset_btn = Button(window, text='Restart', command=restartApp)
reset_btn.grid(row=8, column=0)

out_label = Label(window,text='Prediction Percentage: ')
out_label.grid(row=4,column=0)

warning_label = Label(window,text='Warning, this is experimental software, not to be used for giving any\n form of medical diagnosis, and not to be used in place of a doctor.')
warning_label.grid(row=6,column=0)

buffer = Label(window,text='')
buffer.grid(row=5,column=0)

window.bind("<Return>", replacewebcam)

window.mainloop()