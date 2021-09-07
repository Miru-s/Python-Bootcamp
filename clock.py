from tkinter import *
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("Clock")
root.geometry("300x400")
root.configure(background="#000000")

def time():
    string = strftime('%H:%M:%S  %p')
    label.config(text=string)
    label.after(1000, time)

label= Label(root, font=("ds-digital,80"), background = "black", foreground = "cyan")
label.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
time()

mainloop()
