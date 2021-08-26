from tkinter import *
import tkinter
from tkinter.ttk import *

from time import strftime


root = Tk()
root.title("Clock")

def time():
    String = strftime('%H:%M')
    label.config(text=String)
    label.after(1000, time)


label = Label(root, font=("Liberation Sans",80), background = "black", foreground = "cyan")
label.pack(anchor="center")
time()

mainloop()