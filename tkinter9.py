import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
window= tkinter.Tk()
window.title("CodeOS")

tkinter.Label(window, text= "Username").grid(row=0, column=0)
tkinter.Entry(window).grid(row=0, column=1)

tkinter.Label(window, text= "Password").grid(row=1, column=0)
tkinter.Entry(window).grid(row=1, column=1)

tkinter.Checkbutton(window, text="Keep me Logged in").grid(column=1, row=2)

def CallBack():
   tkinter.messagebox.showinfo( "Welcome" , "Hellooooooooooo")
tkinter.Button(window, text='Login', command=CallBack ).grid(column=1, row=3)

window.mainloop()
