from tkinter import *
import mysql.connector
from Frame import common
class Main_window:
    def __init__(self):
        window = Tk()
        #centering the window to the screen

        common.center(window)
        window.title("Filo")
        window.iconbitmap(r'Frame/login_img/icon.ico')
        window.geometry("1000x600")
        window.configure(bg = "#000000")

        #function of register button
        def regrun():
            regbtn.config(background='#FFFFFF',foreground='#000000',activebackground="white")
            loginbtn.config(background='#000000',foreground='#FFFFFF',activebackground="white")
            regframe=Frame(window,width=1000,height=558,bg='#000000')
            regframe.place(x=0,y=42)
            Label(regframe,text='Register',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=430,y=50)
            Label(regframe,text='Enter Email',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=140)
            Label(regframe,text='Set Password',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=270)

            reg_emailentry = Entry(regframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
            reg_emailentry.place(x=330,y=200,width=350)
            
            reg_passentry = Entry(regframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0,show="*")
            reg_passentry.place(x=330,y=330,width=350)

            #submit button for register
            reg_submit = Button(regframe,text="Submit",borderwidth = 0,highlightthickness = 0,font=("Poppins",15),command = None,background="#FFFFFF",foreground="#000000",activebackground="#FFFFFF",relief = "flat")
            reg_submit.place(x=450,y=450,width=100,height=50)

        #function of login button    
        def loginrun():
            loginbtn.config(background='#FFFFFF',foreground='#000000')
            regbtn.config(background='#000000',foreground='#FFFFFF')
            loginframe=Frame(window,width=1000,height=558,bg='#000000')
            loginframe.place(x=0,y=42)
            Label(loginframe,text='Login',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=440,y=50)
            Label(loginframe,text='Email',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=140)
            Label(loginframe,text='Password',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=270)

            log_emailentry = Entry(loginframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
            log_emailentry.place(x=330,y=200,width=350)
            
            log_passentry = Entry(loginframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0,show="*")
            log_passentry.place(x=330,y=330,width=350)

            login_submit = Button(loginframe,text="Submit",borderwidth = 0,highlightthickness = 0,font=("Poppins",15),command = None,background="#FFFFFF",foreground="#000000",activebackground="#FFFFFF",relief = "flat")
            login_submit.place(x=450,y=450,width=100,height=50)


        #two labels login and register
        regbtn=Button(window,text='Register',command=regrun,font=("Poppins",24),background='#FFFFFF',foreground='#000000',activebackground="white",bd=0,highlightthickness=0,relief='sunken')
        regbtn.place(x=0,y=0,width=500,height=42)
        loginbtn=Button(window,text='Login',command=loginrun,font=("Poppins",24),background='#000000',foreground='#FFFFFF',activebackground="white",bd=0,highlightthickness=0,relief='sunken')
        loginbtn.place(x=500,y=0,width=500,height=42)
        
        #intializing a frame in root window for register
        regrun()

        window.resizable(False,False)
        window.mainloop()