from tkinter import Tk, Label, Button, filedialog 
import cv2
from PIL import Image, ImageTk
window = Tk()
window.title('placeholder name, change this later')
window.geometry('650x700')
label = Label(window)
label.grid(row=0,column=0)
cap = cv2.VideoCapture(0)
def display():
	cv2image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	label.imgtk = imgtk
	label.configure(image=imgtk)
	label.after(20,display)


def takeImage():
    img_1 = ImageTk.getimage(label.imgtk)
    save_img = img_1.convert('RGB')
    save_img.save('current_display.jpg')
    save_img = save_img.resize((450,600),Image.ANTIALIAS)
    save_img.save('current.jpg')

def selectImage():
    filename = filedialog.askopenfilename(title='Open Image')
    copy = Image.open(filename)
    copy.save('current.jpg')
    copy.save('current_display.jpg')

def computePrediction():
    #current.jpg is the file for processing, at ./
    print("asdf")

take_image = Button(window,text="Take Picture", command=takeImage)
take_image.grid(row=1,column=0)
select_image = Button(window,text="Select Image",command=selectImage)
compute_btn = Button(window,text="Compute Prediction",command=computePrediction)
out_label = Label(window,text='Prediction Percentage: ')
warning_label = Label(window,text='Warning, this is experimental software, not to be used for giving any\n form of medical diagnosis, and not to be used in place of a doctor.')
select_image.grid(row=2,column=0)
compute_btn.grid(row=3,column=0)
out_label.grid(row=4,column=0)
buffer = Label(window,text='')
buffer.grid(row=5,column=0)
warning_label.grid(row=6,column=0)
display()
window.mainloop()

