from tkinter import *
from tkinter import filedialog
from shutil import copyfile
import shutil
from sys import exit
from PIL import Image
import subprocess


def openBrowser():
    #subprocess.call("explorer C:\\", shell=True)
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files", "*.png"),("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)
    shutil.copy(root.filename,"C:\\Users\k\Desktop\GUI\original.png")
    im = Image.open("C:\\Users\k\Desktop\GUI\original.png")
    img = Image.open("C:\\Users\k\Desktop\GUI\original.png") # image extension *.png,*.jpg
    originalCrispyWidth = int(im.size[0])
    originalCrispyHeight = int(im.size[1])

    new_width  = int((500/ originalCrispyHeight) * originalCrispyWidth)
    new_height = 500
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save("C:\\Users\k\Desktop\GUI\original.png") # format may what u want ,*.png,*jpg,*.gif

def changeImage1():
    canvas.delete("all")
    newImage1 = PhotoImage(file = "original.png")
    canvas.create_image(0,0, anchor='nw',image=newImage1)
    canvas.image = newImage1

def changeImage2():
    canvas.delete("all")
    newImage2 = PhotoImage(file = "sf.png")
    canvas.create_image(0,0, anchor='nw',image=newImage2)
    canvas.image = newImage2

def changeImage3():
    canvas.delete("all")
    newImage3 = PhotoImage(file = "seattle.png")
    canvas.create_image(0,0, anchor='nw',image=newImage3)
    canvas.image = newImage3

#initialize root view
root = Tk()
#override default layout and functionalities
root.overrideredirect(True)
#customize screen size
root.geometry('1280x680+0+0')

topFrame = Frame(root, height=50, padx=10, pady=5, bg="#343434")
topFrame.pack(side=TOP, fill=X, expand=False, anchor=N)

photo = PhotoImage(file="window_thumbnail_icon_52x60.png")
titleImage = Label(topFrame, image=photo, anchor=W, bg="#343434")
titleImage.photo = photo
titleImage.pack(side=LEFT)

titleLabel = Label(topFrame, font=('arial', 12, 'bold'),
                   text="Dimension Detector",
                   bd=5, anchor=W, bg="#343434", fg="white")
titleLabel.pack(side=LEFT)

windowCloseFrame = Frame(topFrame, width=50, height=50)
windowCloseFrame.pack(side=RIGHT)
closeButton = Button(windowCloseFrame, font=('arial', 12, 'bold'), text="X", command=root.destroy, bg="#343434", fg="white")
closeButton.pack()


#MAIN WINDOW
mainFrame = Frame(root, width=1350, height=50, bg="#343434")
mainFrame.pack(side=BOTTOM, fill=BOTH, expand=1, anchor=S)




#Left Frame
leftFrame = Frame(mainFrame, width=125, height=50, bg="#343434", padx=20, pady=12)
leftFrame.pack(side=LEFT, fill=Y, expand=False, anchor=W)

uploadButton = Button(leftFrame, width=6, height=3, font=('arial', 12, 'bold'), text="IMG", bg="#343434", fg="white", command=openBrowser)
uploadButton.pack(pady=8)

secondButton = Button(leftFrame, width=6, height=3, font=('arial', 12, 'bold'), text="SEC", bg="#343434", fg="white")
secondButton.pack(pady=8)

thirdButton = Button(leftFrame, width=6, height=3, font=('arial', 12, 'bold'), text="THI", bg="#343434", fg="white")
thirdButton.pack(pady=8)





#Center Frame
centerFrame = Frame(mainFrame, width=900, height=100, bg="#808080")
centerFrame.pack(side=LEFT, fill=Y, expand=False, anchor=W)

mainPhoto = PhotoImage(file="emp.png")

canvas = Canvas(centerFrame, width=900, height=500)
canvas.pack(side=LEFT, pady=10, padx=50)

###NOTE: IMAGE HEIGHT MUST BE 500 or less - will need to use opencv to resize
#mainPhotoView = Label(centerFrame, image=mainPhoto, anchor=CENTER, bg="#343434")
#mainPhotoView.photo = photo

#mainPhotoView.place(x=25, y=25, anchor="center")
#mainPhotoView.pack(side=LEFT, pady=10, padx=50)




#Right Frame
rightFrame = Frame(mainFrame, width=255, height=150, bg="#343434")
rightFrame.pack(side=LEFT, fill=Y, expand=False, anchor=W)

originalButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="ORI", bg="#343434", fg="white", command=changeImage1)
originalButton.pack(fill=NONE, expand=True, padx=8, pady=8)

objectButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="OBJ", bg="#343434", fg="white", command=changeImage2)
objectButton.pack(fill=NONE, expand=True, padx=8, pady=8)

measurementButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="MEA", bg="#343434", fg="white", command=changeImage3)
measurementButton.pack(fill=NONE, expand=True, padx=8, pady=8)












#Divides the top and main frames with a small black bar
divider = Frame(root, width=1350, height=5, bg="black")
divider.pack(side=BOTTOM, fill=X, expand=False, anchor=S)

#Closes application when escape button is pressed
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
