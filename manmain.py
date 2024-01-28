import tkinter
from tkinter import*
from tkinter import ttk,font,messagebox
import tk as tk
from PIL import Image


b=Tk()
b.title("Manager page")
b.geometry("1350x700+0+0")

title=Label(b,text="EMPLOYEE DETAILS",bd=2,relief=GROOVE,font=("monospace",40,"bold"),bg="navy",fg="cyan")
title.pack(side=TOP,fill=X)

btn_send=Button(b,text="SELECT",height=0,width=7,borderwidth=1,bg="Blue",activebackground="skyblue",fg="yellow",font=("Verdana",15,"bold"))
btn_send.place(x=1200,y=450)


#content

d_Frame=Frame(b,bd=4,relief=RIDGE,bg="#0E4D92")
d_Frame.place(x=50,y=100,width=1100,height=590)







#viewtable

Table_Frame=Frame(d_Frame,bd=4,relief=RIDGE,bg="#0E4D92")
Table_Frame.place(x=10,y=70,width=1050,height=500)

scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
employee_table=ttk.Treeview(Table_Frame,columns=("Name","Qualification","Skills","Emailid","Phoneno","gender","Date of birth","Experience"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=employee_table.xview)
scroll_y.config(command=employee_table.yview)
employee_table.heading("Name",text="Name")
employee_table.heading("Qualification",text="Qualification")
employee_table.heading("Skills",text="Skills")
employee_table.heading("Emailid",text="Emailid")
employee_table.heading("Phoneno",text="Phoneno")
employee_table.heading("gender",text="gender")
employee_table.heading("Date of birth",text="Date of birth")
employee_table.heading("Experience",text="Experience")
employee_table['show']='headings'
employee_table.column("Name",width=115)
employee_table.column("Qualification",width=155)
employee_table.column("Skills",width=155)
employee_table.column("Emailid",width=115)
employee_table.column("Phoneno",width=115)
employee_table.column("gender",width=115)
employee_table.column("Date of birth",width=115)
employee_table.column("Experience",width=115)
employee_table.pack(fill=BOTH,expand=1)


b.mainloop()
