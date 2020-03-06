from tkinter import *
from PIL import ImageTk,Image


import time
root = Tk()
augmented_data = IntVar()
Train_the_data = IntVar()
Test_the_data = IntVar()
Original = IntVar()
Resize = IntVar()
Save = IntVar()
Detect = IntVar()


def augmented_data_original():
    #Here Code of Augmented Data will come
    pass


def Test_data():
    #Here Code of Test data will come
    pass


def next():

    if augmented_data.get() == 1 :
        augment_window = Toplevel()
        augment_window.maxsize(400,200)
        augment_window.geometry("400x200")
        photo4 = Label(augment_window, image=logo).pack(side=LEFT, anchor="nw")
        photo2 = Label(augment_window,image=logo).pack(side=RIGHT, anchor="ne")
        lable = Label(augment_window, text="Augment Data", font="lusica 19 bold")
        lable.pack()
        origin = Checkbutton(augment_window, text="Original", variable=Original)
        origin.pack()

        resize = Checkbutton(augment_window, text  ="Resize",variable = Resize)
        resize.pack()
        button1 = Button(augment_window, text="Apply", command=augmented_data_original, pady=5,
                         padx=15).pack(side=BOTTOM,anchor="se")

    if Test_the_data.get() ==1:
       Test_window  =Toplevel()
       Test_window.maxsize(400,200)
       Test_window.geometry("400x200")
       photo5 = Label(Test_window, image=logo).pack(side=LEFT, anchor="nw")
       photo2 = Label(Test_window,image=logo).pack(side=RIGHT, anchor="ne")
       lable = Label(Test_window, text="Test Data", font="lusica 19 bold")
       lable.pack()
       save = Checkbutton(Test_window, text="Save Performance", variable=Save)
       save.pack()
       view = Checkbutton(Test_window, text="View detection", variable=Detect)
       view.pack()
       button2 = Button(Test_window, text="Apply", command=Test_data, anchor="se", pady=5,
                        padx=15).pack(side=BOTTOM)

def login():
    """                  Menu Bar
            Here skin detection has devided into 3 parts
            1-> Augmented the Data set
            2-> Test The data
            3-> Train the data
            """
    top = Toplevel()
    top.maxsize(400,200)
    top.geometry("400x200")

    photo3 = Label(top, image=logo).pack(side=LEFT, anchor="nw")
    photo2 = Label(top,image=logo).pack(side=RIGHT, anchor="ne")

    lable = Label(top,text = "Menu" , font = "lusica 19 bold")
    lable.pack()
    button1 = Button(top,text="Apply", command=next, anchor="se", pady = 5, padx=15).pack(side=BOTTOM)
    augment = Checkbutton(top,text = "Augmented Data", variable = augmented_data)
    augment.pack()
    train = Checkbutton(top,text = "Train the Module",variable = Train_the_data)
    train.pack()
    test = Checkbutton(top, text="Test the Module", variable=Test_the_data)
    test.pack()

#First page Code:


root.geometry("400x200")

root.maxsize(400,200)
root.title("Skin detection")

image = Image.open("download (1).jpg")
logo = ImageTk.PhotoImage(image)
photo = Label(image=logo).pack(side = LEFT,anchor = "nw")
photo2 = Label(image=logo).pack(side = RIGHT,anchor = "ne")
title= Label(text = "Welcome " , font =  " lusica 19 bold").pack()
button = Button(root, text = "Start", command = login, anchor ='se').pack()

"""                           Animation                              """
canvas = Canvas(root, width = 300,height = 80)
canvas.pack()
ball1 = canvas.create_oval(10,40,30,60, fill = "orange")
text1  =  canvas.create_text(20,50, text="S")

ball2 = canvas.create_oval(30,40,50,60, fill  = "orange")
text2 = canvas.create_text(40,50,text="K")

ball3  = canvas.create_oval(50,40,70,60 ,fill = "orange")
text3 = canvas.create_text(60,50,text="I")

ball4  = canvas.create_oval(70,40,90,60 ,fill = "orange")
text4 = canvas.create_text(80,50,text="N")

ball5  = canvas.create_oval(100,40,120,60 ,fill = "orange")
text5 = canvas.create_text(110,50,text="D")

ball6  = canvas.create_oval(120,40,140,60 ,fill = "orange")
text6 = canvas.create_text(130,50,text="E")

ball7  = canvas.create_oval(140,40,160,60 ,fill = "orange")
text7 = canvas.create_text(150,50,text="T")

ball8  = canvas.create_oval(160,40,180,60 ,fill = "orange")
text8 = canvas.create_text(170,50,text="E")

ball9  = canvas.create_oval(180,40,200,60 ,fill = "orange")
text9 = canvas.create_text(190,50,text="C")

ball10  = canvas.create_oval(200,40,220,60 ,fill = "orange")
text10 = canvas.create_text(210,50,text="T")

ball11  = canvas.create_oval(220,40,240,60 ,fill = "orange")
text11 = canvas.create_text(230,50,text="I")

ball12  = canvas.create_oval(240,40,260,60 ,fill = "orange")
text12 = canvas.create_text(250,50,text="O")

ball13  = canvas.create_oval(260,40,280,60 ,fill = "orange")
text13 = canvas.create_text(270,50,text="N")

xspeed = 0
yspeed = 1
while True:
    canvas.move(ball1,xspeed,yspeed)
    canvas.move(text1,xspeed,yspeed)
    canvas.move(text2, xspeed, -yspeed)
    canvas.move(ball2, xspeed, -yspeed)
    canvas.move(ball3, xspeed, yspeed)
    canvas.move(text3, xspeed, yspeed)
    canvas.move(ball4, xspeed, -yspeed)
    canvas.move(text4, xspeed, -yspeed)
    canvas.move(ball5, xspeed, yspeed)
    canvas.move(text5, xspeed, yspeed)
    canvas.move(text6, xspeed, -yspeed)
    canvas.move(ball6, xspeed, -yspeed)
    canvas.move(ball7, xspeed, yspeed)
    canvas.move(text7, xspeed, yspeed)
    canvas.move(text8, xspeed, -yspeed)
    canvas.move(ball8, xspeed, -yspeed)
    canvas.move(ball9, xspeed, yspeed)
    canvas.move(text9, xspeed, yspeed)
    canvas.move(text10, xspeed, -yspeed)
    canvas.move(ball10, xspeed, -yspeed)
    canvas.move(ball11, xspeed, yspeed)
    canvas.move(text11, xspeed, yspeed)
    canvas.move(text12, xspeed, -yspeed)
    canvas.move(ball12, xspeed, -yspeed)
    canvas.move(ball13, xspeed, yspeed)
    canvas.move(text13, xspeed, yspeed)
    """     Logic for up and down """
    pos = canvas.coords(ball1)
    pos1 = canvas.coords(ball2)

    if(pos[3] >= 70):
        yspeed =-1
    if(pos[3]<= 50):
        yspeed = 1
    if pos1[3] <= 50:
        yspeed = -1
    if pos1[3] >= 70:
        yspeed = 1
    root.update()
    time.sleep(0.1)






root.mainloop()
