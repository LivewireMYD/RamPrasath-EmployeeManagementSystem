import tkinter
from tkinter import*
from tkinter import ttk,font,messagebox
import tk as tk
from PIL import Image

def hr():
    b=Tk()
    b.title("Employee System")
    b.geometry("1350x700+0+0")

    title=Label(b,text="EMPLOYEE DETAILS",bd=12,relief=GROOVE,font=("monospace",40,"bold"),bg="navy",fg="cyan")
    title.pack(side=TOP,fill=X)

    btn_send=Button(b,text="SEND",height=0,width=7,borderwidth=1,bg="Blue",activebackground="skyblue",fg="yellow",font=("Verdana",15,"bold"))
    btn_send.place(x=1200,y=450)
    btn_delete=Button(b,text="DELETE",height=0,width=7,borderwidth=1,bg="Blue",activebackground="skyblue",fg="yellow",font=("Verdana",15,"bold"))
    btn_delete.place(x=1200,y=550)

    #content

    d_Frame=Frame(b,bd=4,relief=RIDGE,bg="#0E4D92")
    d_Frame.place(x=50,y=100,width=1100,height=590)

    lbl_search=Label(d_Frame,text="Search",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
    lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

    combo_search=ttk.Combobox(d_Frame,width=10,font=("times new roman",13,"bold"),state='readonly')
    combo_search['values']=('Name','Skills','Phoneno')
    combo_search.grid(row=0,column=1,pady=10,padx=20)

    txt_search=Entry(d_Frame,width=15,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
    txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")



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


def employee_register():
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
        entry_fname=Entry(M_Frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        entry_fname.grid(row=1,column=1,pady=10,padx=20,sticky="W")


        lbl_lname=Label(M_Frame,text="Lastname:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_lname.grid(row=2,column=0,pady=10,padx=20,sticky="W")

        entry_lname=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry_lname.grid(row=2,column=1,pady=10,padx=20,sticky="W")

        lbl_Qualification=Label(M_Frame,text="Qualification:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_Qualification.grid(row=3,column=0,pady=10,padx=20,sticky="W")

        entry_Qualification=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry_Qualification.grid(row=3,column=1,pady=10,padx=20,sticky="W")

        lbl_Dop=Label(M_Frame,text="Date Of Birth:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_Dop.grid(row=4,column=0,pady=10,padx=20,sticky="W")

        entry_Dop=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry_Dop.grid(row=4,column=1,pady=10,padx=20,sticky="W")

        lbl_ph=Label(M_Frame,text="Phone No:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_ph.grid(row=5,column=0,pady=10,padx=20,sticky="W")

        entry_ph=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry_ph.grid(row=5,column=1,pady=10,padx=20,sticky="W")

        lbl_email=Label(M_Frame,text="Email Id:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_email.grid(row=6,column=0,pady=10,padx=20,sticky="W")

        entry_email=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry_email.grid(row=6,column=1,pady=10,padx=20,sticky="W")


        lbl_course=Label(M_Frame,text="Skills:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_course.grid(row=7,column=0,pady=10,padx=20,sticky="W")

        combo_course=ttk.Combobox(M_Frame,font=("times new roman",13,"bold"),state='readonly')
        combo_course['values']=('Python Devoloper','Jave Developer','Full Stack Developer')
        combo_course.grid(row=7,column=1,pady=10,padx=20)

        lbl_gen=Label(M_Frame,text="Gender:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_gen.grid(row=8,column=0,pady=10,padx=20,sticky="W")

        combo_gen=ttk.Combobox(M_Frame,font=("times new roman",13,"bold"),state='readonly')
        combo_gen['values']=('Male','Female')
        combo_gen.grid(row=8,column=1,pady=20,padx=10)

        lbl_exp=Label(M_Frame,text="Experieance:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_exp.grid(row=9,column=0,pady=10,padx=20,sticky="W")

        combo_exp=ttk.Combobox(M_Frame,font=("times new roman",13,"bold"),state='readonly')
        combo_exp['values']=('Fresher','1year','2year','3year','4year')
        combo_exp.grid(row=9,column=1,pady=20,padx=10)

        lbl_address=Label(M_Frame,text="Adress:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_address.grid(row=2,column=3,pady=10,padx=20,sticky="W")

        entry_address=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,width=30)
        entry_address.grid(row=2,column=4,pady=10,padx=20,sticky="W")

        lbl_age=Label(M_Frame,text="Age:",bg="#0E4D92",fg="#B0DFE5",font=("Verdana",15,"bold"))
        lbl_age.grid(row=1,column=3,pady=10,padx=20,sticky="W")

        entry_age=Entry(M_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry_age.grid(row=1,column=4,pady=10,padx=20,sticky="W")

        btn_submit=Button(M_Frame,text="SUBMIT",height=0,width=7,borderwidth=1,bg="Blue",activebackground="skyblue",fg="yellow",font=("Verdana",15,"bold"))
        btn_submit.place(x=700,y=450)


        a.mainloop()

def managerlog():
    mlogin=Tk()
    mlogin.geometry("925x500+200+100")
    mlogin.title("Manager Login")
    mlogin.configure(background='white')
    mlogin.resizable(False,False)
    imglog=PhotoImage(file="login.png")
    Label(mlogin,image=imglog,bg="white").place(x=50,y=5)

    l_label=Label(mlogin,text="Welcome..!",bd=0,relief=GROOVE,font=("monospace",20,"bold"),bg="white",fg="Blue")
    l_label.place(x=650,y=50,width=160,height=40)

    l_Frame=Frame(mlogin,bd=4,relief=RIDGE,bg="#0E4D92")
    l_Frame.place(x=500,y=100,width=400,height=200)
    lbl_admin1=Label(l_Frame,text="Admin id:",bg="#0E4D92",fg="#B0DFE5",font=("monospace",15,"bold"))
    lbl_admin1.grid(row=1,column=0,pady=10,padx=10,sticky="W")
    entry_admin1=Entry(l_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    entry_admin1.grid(row=1,column=1,pady=10,padx=10,sticky="W")
    lbl_password1=Label(l_Frame,text="Password:",bg="#0E4D92",fg="#B0DFE5",font=("monospace",15,"bold"))
    lbl_password1.grid(row=2,column=0,pady=10,padx=10,sticky="W")
    entry_password1=Entry(l_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    entry_password1.grid(row=2,column=1,pady=10,padx=10,sticky="W")
    home3=Button(l_Frame,text="Login",fg='Red',bd=0,relief=RIDGE,font=("monospace",20,"bold"))
    home3.place(x=130,y=140,width=100,height=40)

    mlogin.mainloop()

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

button2=Button(home,text="  HR  ",font=("monospace",20,"bold"),borderwidth=7,activebackground="Sky blue",image=img1,compound=LEFT,relief=GROOVE,command=lambda:hr())
button2.place(x=580,y=210)

img3=PhotoImage(file="reg1img.png")
button2=Button(home,text="REGISTER",font=("monospace",20,"bold"),borderwidth=7,activebackground="Sky blue",image=img3,compound=LEFT,relief=GROOVE,command=lambda:employee_register())
button2.place(x=400,y=460)

home.mainloop()
