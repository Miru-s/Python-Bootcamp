import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.messagebox
window= tkinter.Tk()
window.title("CodeOS")

def clicked():
   messagebox.showinfo('Message', 'You look great today')

btn= Button(window, text='Enter', command=clicked)
btn.pack()

window.mainloop()



