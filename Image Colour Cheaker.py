# Image Colour Cheaker Free !!

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from colorthief import ColorThief
import os




root=Tk()
root.title("Color Picker From Image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False,False)

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title = 'Select Image File', filetype=(('PNG file', '*.png'),('JPG file','*.jpg'),("All Files",'*.txt')))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=310, height=270)
    lbl.image=img

def Findcolor():
    ct=ColorThief(filename)
    palette=ct.get_palette(color_count=11)

    rgb1=palette[0]
    rgb2=palette[1]
    rgb3=palette[2]
    rgb4=palette[3]
    rgb5=palette[4]
    rgb6=palette[5]
    rgb7=palette[6]
    rgb8=palette[7]
    rgb9=palette[8]
    rgb10=palette[9]

    print(rgb1)
    color1=f"#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    color2=f"#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    color3=f"#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    color4=f"#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    color5=f"#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    color6=f"#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    color7=f"#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    color8=f"#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    color9=f"#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    color10=f"#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"

    color.itemconfig(id1, fill=color1)
    color.itemconfig(id2, fill=color2)
    color.itemconfig(id3, fill=color3)
    color.itemconfig(id4, fill=color4)
    color.itemconfig(id5, fill=color5)

    color2.itemconfig(id6, fill=color6)
    color2.itemconfig(id7, fill=color7)
    color2.itemconfig(id8, fill=color8)
    color2.itemconfig(id9, fill=color9)
    color2.itemconfig(id10, fill=color10)



    '''print(color1)
    print(color2)
    print(color3)
    print(color4)
    print(color5)
    print(color6)
    print(color7)
    print(color8)
    print(color9)
    print(color10)'''

    hex1.config(text=color1)
    hex2.config(text=color2)
    hex3.config(text=color3)
    hex4.config(text=color4)
    hex5.config(text=color5)
    hex6.config(text=color6)
    hex7.config(text=color7)
    hex8.config(text=color8)
    hex9.config(text=color9)
    hex10.config(text=color10)



#ICON
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

Label(root,width=120,heigh=10, bg="#4272f9").pack()
# frame

frame=Frame(root,width=700,height=370,bg="#fff")
frame.place(x=50,y=50)

logo=PhotoImage(file="logo.png")
Label(frame, image=logo,bg="#fff").place(x=10,y=10)

Label(frame,text="Color Finder", font="arial 25 bold",bg="white").place(x=100,y=20)


# COLOR1
color=Canvas(frame,bg="#fff",width=150, height=265,bd=0)
color.place(x=20,y=90)

id1=color.create_rectangle((10,10,50,50),fill="#b8255f")
id2=color.create_rectangle((10,50,50,100),fill="#db4035")
id3=color.create_rectangle((10,100,50,150),fill="#ff9933")
id4=color.create_rectangle((10,150,50,200),fill="#fad000")
id5=color.create_rectangle((10,200,50,250),fill="#afb83b")

hex1=Label(color,text="#b825f",fg="#000",font="arial 12 bold",bg="white")
hex1.place(x=60,y=15)

hex2=Label(color,text="#db4035",fg="#000",font="arial 12 bold",bg="white")
hex2.place(x=60,y=65)

hex3=Label(color,text="#ff9933",fg="#000",font="arial 12 bold",bg="white")
hex3.place(x=60,y=115)

hex4=Label(color,text="#fad000",fg="#000",font="arial 12 bold",bg="white")
hex4.place(x=60,y=165)

hex5=Label(color,text="#afb83b",fg="#000",font="arial 12 bold",bg="white")
hex5.place(x=60,y=215)

# COLOR2
color2=Canvas(frame,bg="#fff",width=150, height=265,bd=0)
color2.place(x=180,y=90)

id6=color2.create_rectangle((10,10,50,50),fill="#7ecc49")
id7=color2.create_rectangle((10,50,50,100),fill="#299438")
id8=color2.create_rectangle((10,100,50,150),fill="#6accbc")
id9=color2.create_rectangle((10,150,50,200),fill="#158fad")
id10=color2.create_rectangle((10,200,50,250),fill="#14aaf5")
 
hex6=Label(color2,text="#7ecc49",fg="#000",font="arial 12 bold",bg="white")
hex6.place(x=60,y=15)

hex7=Label(color2,text="#299438",fg="#000",font="arial 12 bold",bg="white")
hex7.place(x=60,y=65)

hex8=Label(color2,text="#6accbc",fg="#000",font="arial 12 bold",bg="white")
hex8.place(x=60,y=115)

hex9=Label(color2,text="#158fad",fg="#000",font="arial 12 bold",bg="white")
hex9.place(x=60,y=165)

hex10=Label(color2,text="#14aaf5",fg="#000",font="arial 12 bold",bg="white")
hex10.place(x=60,y=215)


#Select Image
selectimage=Frame(frame,width=340,height=350,bg="#d6dee5")
selectimage.place(x=350,y=10)

f=Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lbl=Label(f,bg="black")
lbl.place(x=0,y=0)

Button(selectimage,text="Select Image",width=12,height=1,font="arial 14 bold", command=showimage).place(x=10,y=300)
Button(selectimage,text="Find Colors", width=12,height=1,font="arial 14 bold", command=Findcolor).place(x=176,y=300)

root.mainloop()
