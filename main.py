import cv2 as cv
from tkinter import *
from tkinter import filedialog

# method for resizing window
def rescale_pic(img, scale=0.75, wid=0.8):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * wid)
    w = int(img.shape[1] + width)
    h = int(img.shape[0] + height)
    dimensions = (w, h)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

# ourimage
def pic():
    parent.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", ".jpeg"), ("all files", ".*")))
    img_file = parent.filename
    parent.destroy()

    # readimagefile
    imginput = cv.imread(img_file)

    # resizing image
    imageres = rescale_pic(imginput)

    # convert to grayscale for haar features
    blacknwhite = cv.cvtColor(imageres, cv.COLOR_BGR2GRAY)

    # classification file
    classifier_file = 'cars.xml'

    # createclassifier
    car_trackeralgo = cv.CascadeClassifier(classifier_file)

    # detectcars
    carscord = car_trackeralgo.detectMultiScale(blacknwhite)

    # loop for rectangle layout
    for (x, y, w, h) in carscord:
        cv.rectangle(imageres, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv.imshow('detect_car', imageres)
    cv.waitKey(0)

parent = Tk()
parent.geometry("900x900")
parent.configure(background="#AED6F1")
parent.title("Vehicle Detection Using Opecv")
Label(parent, text='Click to Select Image File',bg="#AED6F1", height="5",width="20").grid(row=6)
b = Button(parent, text="Upload Image", bg="#EDBB99", command=pic)
b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
b.place(x=150, y=25)
mainloop()

