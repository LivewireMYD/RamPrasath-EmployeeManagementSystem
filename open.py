import tkinter
from tkinter import*
from tkinter import ttk,font,messagebox
import tk as tk
from PIL import Image


home=Tk()
home.title("Employee Management System")
home.geometry("1024x600+170+70")
home.resizable(False,False)

label1=Label(home)
label1.place(relx=0,rely=0,width=1024,height=600)
img=PhotoImage(file="backround1.png")
label1.configure(image=img)


img1=PhotoImage(file="manager1.png")
button2=Button(home,text="MANAGER",font=("monospace",20,"bold"),borderwidth=7,activebackground="Sky blue",image=img1,compound=LEFT,relief=GROOVE)
button2.place(x=260,y=210)

button2=Button(home,text="  HR  ",font=("monospace",20,"bold"),borderwidth=7,activebackground="Sky blue",image=img1,compound=LEFT,relief=GROOVE)
button2.place(x=580,y=210)

img3=PhotoImage(file="reg1img.png")
button2=Button(home,text="REGISTER",font=("monospace",20,"bold"),borderwidth=7,activebackground="Sky blue",image=img3,compound=LEFT,relief=GROOVE)
button2.place(x=400,y=460)

home.mainloop()
