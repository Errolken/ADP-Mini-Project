from tkinter import *
def center(window):
    app_width=1000 
    app_height=600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x=(screen_width / 2) - (app_width/2)
    y=(screen_height / 2) - (app_height/2)
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    window.deiconify()