from tkinter import *
from tkinter import filedialog
from shutil import copyfile
import shutil
import PIL
from sys import exit
from PIL import Image
import subprocess
import time

#
# Function: uploadImageFile()
#    - Copies image in various sizes to root folder,
#       *overwrites existing image files with same names
#       uses images_sized to load algorithms
def uploadImageFile():
    #subprocess.call("explorer C:\\", shell=True)

    #askopenfilename method opens dialog with the computer
    #  and stores selected photo into filename
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files", "*.png"),("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename) #Console Check Test

    #open image, resize, and save
    shutil.copy(root.filename,"./userimage_full.png")
    userImg = Image.open("./userimage_full.png")

    userImg.save("./userimage_full.png")

    width = int(userImg.size[0])
    height = int(userImg.size[1])

    canvasDimsHeight = 500
    canvasDimsWidth = int((500 / height) * width)
    canvasImg = userImg.resize((canvasDimsWidth, canvasDimsHeight), Image.ANTIALIAS)
    canvasImg.save("./userimage_canvas.png")

    buttonDimsHeight = 160
    buttonDimsWidth = 220
    buttonImg = userImg.resize((buttonDimsWidth, buttonDimsHeight), Image.ANTIALIAS)
    buttonImg.save("./userimage_button.gif")

    #Create the buttons with the appropriate images contained on button interface
    createImgButtons()

def changeImage1():
    canvas.delete("all")
    newImage1 = PhotoImage(file = "userimage_canvas.png")
    canvas.create_image(0,0, anchor='nw',image=newImage1)
    canvas.image = newImage1

def changeImage2():
    canvas.delete("all")
    newImage2 = PhotoImage(file = "sf.png")
    canvas.create_image(0,0, anchor='nw',image=newImage2)
    canvas.image = newImage2
    canvas.pack(side=LEFT, pady=10, padx=50)

def changeImage3():
    canvas.delete("all")
    newImage3 = PhotoImage(file = "seattle.png")
    canvas.create_image(0,0, anchor='nw',image=newImage3)
    canvas.image = newImage3
    canvas.pack(side=LEFT, pady=10, padx=50)

#
# Function: createImgButtons()
#    - Creates the imageDetection, objectDetection, and mesurementDetection
#      buttons with the matched images from the root folder
#      and apply image to button surface
def createImgButtons():
    #count testing purposes
    originalPhoto = PhotoImage(file="userimage_button.gif")
    originalButton = Button(rightFrame, image=originalPhoto, command=changeImage1)
    originalButton.image = originalPhoto
    originalButton.pack(padx=8, pady=8)

    count = 0
    while(count != 5):
        count = count + 1
        formatString = "gif -index" + str(count)
        objectPhoto = PhotoImage(file="Untitled-3.gif", format=formatString)
        objectButton = Button(rightFrame, image=objectPhoto, command=changeImage2)
        objectButton.image = objectPhoto
        objectButton.pack(padx=8, pady=8)
        #objectButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="OBJ", bg="#343434", fg="white", command=changeImage2)
        #objectButton.pack(fill=NONE, expand=True, padx=8, pady=8)

        measurementPhoto = PhotoImage(file="Untitled-4.gif", format=formatString)
        measurementButton = Button(rightFrame, image=measurementPhoto, command=changeImage3)
        measurementButton.image = measurementPhoto
        measurementButton.pack(padx=8, pady=8)
        #measurementButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="MEA", bg="#343434", fg="white", command=changeImage3)
        #measurementButton.pack(fill=NONE, expand=True, padx=8, pady=8)

    '''
    count = 0
    while(count != 3):
        rightFrameRef = rightFrame
        rightFrame.pack_forget()
        if(count == 0):
            count = count + 1
            photo = PhotoImage(file="userimage_canvas.png")
            originalButton = Button(rightFrame, width=30, height=8, command=changeImage1)
            originalButton.config(image=photo)

            #originalButton.config(image=photo, width=30, height=8)
            originalButton.pack(fill=NONE, expand=True)
            root.update()
            count = count + 1
        elif(count == 1):
            time.sleep(3)
            print("yes")
            photo = PhotoImage(file="userimage_canvas.gif")
            originalButton = Button(rightFrame, width=30, height=8, command=changeImage1)
            originalButton.config(image=photo)

            #originalButton.config(image=photo, width=30, height=8)
            originalButton.pack(fill=NONE, expand=True)

            objectButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="OBJ", bg="#343434", fg="white", command=changeImage2)
            objectButton.pack(fill=NONE, expand=True, padx=8, pady=8)
            root.update()
            count = count + 1
        else:
            time.sleep(3)
            print("no")
            photo = PhotoImage(file="userimage_canvas.png")
            originalButton = Button(rightFrame, width=30, height=8, command=changeImage1)
            originalButton.config(image=photo)

            #originalButton.config(image=photo, width=30, height=8)
            originalButton.pack(fill=NONE, expand=True)

            objectButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="OBJ", bg="#343434", fg="white", command=changeImage2)
            objectButton.pack(fill=NONE, expand=True, padx=8, pady=8)

            measurementButton = Button(rightFrame, width=30, height=8, font=('arial', 12, 'bold'), text="MEA", bg="#343434", fg="white", command=changeImage3)
            measurementButton.pack(fill=NONE, expand=True, padx=8, pady=8)
            root.update()
        '''
#initialize root view
root = Tk()
#override default layout and functionalities
#root.overrideredirect(True)
#customize screen size
#root.geometry('1280x680+0+0')

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


uploadPhoto = PhotoImage(file="1.png")
uploadButton = Button(leftFrame, image=uploadPhoto, command=uploadImageFile)
uploadButton.image = uploadPhoto
uploadButton.pack(pady=8)
#uploadButton = Button(leftFrame, width=6, height=3, font=('arial', 12, 'bold'), text="IMAGE", bg="#343434", fg="white", command=uploadImageFile)
#uploadButton.pack(pady=8)


linkPhoto = PhotoImage(file="2.png")
linkButton = Button(leftFrame, image=linkPhoto, command=uploadImageFile)
linkButton.image = linkPhoto
linkButton.pack(pady=8)
#secondButton = Button(leftFrame, width=6, height=3, font=('arial', 12, 'bold'), text="LINK", bg="#343434", fg="white")
#secondButton.pack(pady=8)

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












#Divides the top and main frames with a small black bar
divider = Frame(root, width=1350, height=5, bg="black")
divider.pack(side=BOTTOM, fill=X, expand=False, anchor=S)

#Closes application when escape button is pressed
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
