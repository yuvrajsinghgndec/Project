import tkinter as tk
from tkinter import *
from turtle import bgcolor
from tkinter.filedialog import askopenfilename,asksaveasfilename
from turtle import width
import moviepy.editor as me

filename=''

def convert():
        global filename
        filetypes=(("Audio files","*.mp3 , *.waw , *.ogg"),("All files","*.*"))
        video=me.VideoFileClip(filename)
        audio=video.audio
        file=asksaveasfilename(filetypes=filetypes)
        audio.write_audiofile(f'{file}{format.get()}')
        label5=Label(root,text="Done",font=("Arial",18),fg="gold")
        label5.pack()
        label5.place(x=450,y=300)
def select():
    global filename
    filetypes = (
        ('video files', '*.WEBM , *.MPG, *.MP2 , *.MPEG , *.MPE , *.MPV , *.MP4 , *.M4P , *.M4V , *.AVI , *.WMV , *.MOV , *.QT , *.FLV , *.SWF , *.AVCHD'),
        ('All files', '*.*')
    )
    filename=askopenfilename(filetypes=filetypes)
    label3.config(text="File Selected",fg="green",background = "black")
    label4=Label(root,text="Select Audio format :-",font=("Arial",18,),fg ="dark goldenrod" , background= "black")
    label4.pack()
    label4.place(x=100,y=460)
    options=[".mp3",".ogg",".wav"]
    format.set(".mp3")
    menu=OptionMenu(root,format,*options)
    menu["bg"] = "dark goldenrod" 
    menu.pack()
    menu.place(x=350,y=460)
    button3=Button(root,text="Export",font=("Harlow Solid",14,"bold"),command=convert,width=20,height=1,background="dark goldenrod")
    button3.pack()
    button3.place(x=110,y=530)
    button4=Button(root,text="Quit",font=("Harlow Solid",14 ,"bold"),command=quit,width=20,height=1,background="dark goldenrod")
    button4.pack()
    button4.place(x=110,y=580)

root=Tk()
root.geometry("455x650")
root.minsize(455,650)
root.maxsize(455,650)
root["bg"] = "black"
photo = PhotoImage(file="logo.png")
new_label = Label(image=photo)
new_label["bg"] = "black"
new_label.pack()

label2=Label(root,text="Select Video file to Convert",font=("Arial",16),fg = "dark goldenrod" , background = "black")
label2.pack()
label2.place(x=105,y=330)
button1=Button(root,text="Select",font=("Harlow Solid",14,"bold"),command=select,width=20,height=1,background="dark goldenrod")
button1.pack()
button1.place(x=110,y=365)

label3=Label(root,font=("Footlight MT",18,"bold"))
label3["bg"] = "black"
label3.pack()
label3.place(x=150,y=410)
format=StringVar()
root.mainloop()


root.mainloop()


