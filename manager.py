import tkinter
from tkinter import*
from tkinter import ttk,font,messagebox
import tk as tk
from PIL import Image



hrlogin=Tk()
hrlogin.geometry("925x500+200+100")
hrlogin.title("Hr Login")
hrlogin.configure(background='white')
hrlogin.resizable(False,False)
hrlogimg=PhotoImage(file="login.png")
Label(hrlogin,image=hrlogimg,bg="white").place(x=50,y=5)

l_label=Label(hrlogin,text="Welcome..!",bd=0,relief=GROOVE,font=("monospace",20,"bold"),bg="white",fg="Blue")
l_label.place(x=650,y=50,width=160,height=40)

hr_Frame=Frame(hrlogin,bd=4,relief=RIDGE,bg="#0E4D92")
hr_Frame.place(x=500,y=100,width=400,height=200)
lbl_admin1=Label(hr_Frame,text="Admin id:",bg="#0E4D92",fg="#B0DFE5",font=("monospace",15,"bold"))
lbl_admin1.grid(row=1,column=0,pady=10,padx=10,sticky="W")
entry_admin1=Entry(hr_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
entry_admin1.grid(row=1,column=1,pady=10,padx=10,sticky="W")
lbl_password1=Label(hr_Frame,text="Password:",bg="#0E4D92",fg="#B0DFE5",font=("monospace",15,"bold"))
lbl_password1.grid(row=2,column=0,pady=10,padx=10,sticky="W")
entry_password1=Entry(hr_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
entry_password1.grid(row=2,column=1,pady=10,padx=10,sticky="W")
hrlogin1=Button(hr_Frame,text="Login",fg='Red',bd=0,relief=RIDGE,font=("monospace",20,"bold"))
hrlogin1.place(x=130,y=140,width=100,height=40)

hrlogin.mainloop()
