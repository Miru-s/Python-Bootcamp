import tkinter
from tkinter import *
from tkinter.ttk import *
window= tkinter.Tk()
window.title("CodeOS")

window.geometry('350x200')

spin= Spinbox(window, from_=0, to=100, width=5)
spin.pack()

window.mainloop()
