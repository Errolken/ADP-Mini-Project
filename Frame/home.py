from tkinter import *
from PIL import ImageTk,Image
from Frame import login
import mysql.connector

class Mainhome:
    def __init__(self):
        w=Tk()
        w.geometry('1400x700') 
        w.configure(bg='#000000')
        w.resizable(False, False) 
        w.title("Filo")
        w.iconbitmap(r'Frame/home_img/icon.ico')
        def default_home():
            homeframe=Frame(w,width=1400,height=658,bg='#262626')
            glabel=Label(w,text='Home',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42) 
            homeframe.place(x=0,y=42)

        def toggle_win():
            global menu
            menu=Frame(w,width=300,height=700,bg='#D2E6FB')
            menu.place(x=0,y=0)

            def bttn(x,y,text,bcolor,fcolor,cmd):
                def on_entera(e):
                    myButton1['background']=bcolor
                    myButton1['foreground']='#262626'
                
                def on_leavea(e):
                    myButton1['background']=fcolor
                    myButton1['foreground']='#262626'

                myButton1= Button(menu,text=text,width=25,height=1,fg='#262626',border=0,font=("Poppins",15),bg=fcolor,activebackground='#262626',activeforeground=bcolor,command=cmd)
                myButton1.bind("<Enter>",on_entera)
                myButton1.bind("<Enter>",on_leavea)

                myButton1.place(x=x,y=y)

            def funds():
                menu.destroy()
                glabel=Label(w,text='Transfer Funds',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                f3=Frame(w,width=600,height=658,bg='#ACD6FF')
                f3.place(x=0,y=42)
    
            def trans_history():
                menu.destroy()
                f4=Frame(w,width=1400,height=658,bg='#262626')
                glabel=Label(w,text='Transaction History',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                f4.place(x=0,y=42)

            def home():
                menu.destroy()
                default_home()

            def manage_cards():
                menu.destroy()
                print("hello")


            def manage_profile():
                menu.destroy()
                f6=Frame(w,width=1400,height=658,bg='#262626')
                glabel=Label(w,text='Profile',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                f6.place(x=0,y=42)

            def contact_us():
                menu.destroy()
                f7=Frame(w,width=1400,height=658,bg='#262626')
                f7.place(x=0,y=42)
                glabel=Label(w,text='Contact Us',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)

            def logout():
                w.destroy()
                login.Main_window('login')

            bttn(0,80,'Home','#D2E6FB','#D2E6FB',home)
            bttn(0,150,'Transfer Funds','#D2E6FB','#D2E6FB',funds)
            bttn(0,220,'Transaction History','#D2E6FB','#D2E6FB',trans_history)
            bttn(0,290,'Manage Cards','#D2E6FB','#D2E6FB',manage_cards)
            bttn(0,360,'Manage Profile','#D2E6FB','#D2E6FB',manage_profile)
            bttn(0,430,'Contact Us','#D2E6FB','#D2E6FB',contact_us)
            bttn(0,650,'Logout','#D2E6FB','#D2E6FB',logout)
                
            def dele():
                menu.destroy()

                
            global menubtn
            menubtn=ImageTk.PhotoImage(Image.open('Frame/home_img/close.png'))

            Button(menu,image=menubtn,command=dele,border=0,background='#D2E6FB',activebackground='#D2E6FB').place(x=5,y=10)

        default_home()

        img1=ImageTk.PhotoImage(Image.open('Frame/home_img/open.png'))
        Button(w,command=toggle_win,image=img1,border=0,bg='#000000',activebackground='#000000').place(x=5,y=5)

        app_width=1400 
        app_height=700
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x=(screen_width / 2) - (app_width/2)
        y=(screen_height / 2) - (app_height/2)
        w.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        w.deiconify()
        w.mainloop()