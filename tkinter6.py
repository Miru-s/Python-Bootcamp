import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
window= tkinter.Tk()
window.title("CodeOS")

rad1= Radiobutton(window, text='Python', value=1)
rad2= Radiobutton(window, text='Java', value=2)
rad3= Radiobutton(window, text='C++', value=3)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

window.mainloop()



