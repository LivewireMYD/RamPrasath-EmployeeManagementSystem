import tkinter
import pymysql
from tkinter import*
from tkinter import ttk,font,messagebox
import tk as tk

def add_employee(name,qualification,dop):
        if entry_fname.get()=="" or entry_Qualification.get()=="" or entry_Dop.get()=="":
            messagebox.showerror("Error","All fields are Required!!!")
        else:
            conn=pymysql.connect(host="localhost",user="root",password="753883mr",database="emp")
            cur=conn.cursor()
            cur.execute("insert into employee values(%s,%s,%s)",(entry_fname.get(),
                                                                 entry_Qualification.get(),
                                                                 entry_Dop.get(),

                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Record has been Inserted")

a=Tk()
a.title("Employee System")
a.geometry("1350x700+0+0")

title=Label(a,text="EMPLOYEE REGISTRATION",bd=12,relief=GROOVE,font=("monospace",40,"bold"),bg="navy",fg="cyan")
title.pack(side=TOP,fill=X)

M_Frame=Frame(a,bd=4,relief=RIDGE,bg="#0E4D92")
M_Frame.place(x=200,y=100,width=1000,height=590)

#content
lbl_fname=Label(M_Frame,text="Firstname:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
lbl_fname.grid(row=1,column=0,pady=10,padx=20,sticky="w")
entry_fname=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
entry_fname.grid(row=1,column=1,pady=10,padx=20,sticky="W")

lbl_Qualification=Label(M_Frame,text="Qualification:",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
lbl_Qualification.grid(row=3,column=0,pady=10,padx=20,sticky="W")

entry_Qualification=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
entry_Qualification.grid(row=3,column=1,pady=10,padx=20,sticky="W")

lbl_Dop=Label(M_Frame,text="Date Of Birth:",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
lbl_Dop.grid(row=4,column=0,pady=10,padx=20,sticky="W")

entry_Dop=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
entry_Dop.grid(row=4,column=1,pady=10,padx=20,sticky="W")

btn_submit=Button(M_Frame,text="SUBMIT",font=("times new roman",15,"bold"),command=lambda:add_employee(entry_fname.get(),entry_Qualification.get(),entry_Dop.get()))
btn_submit.place(x=700,y=450)

a.mainloop()




