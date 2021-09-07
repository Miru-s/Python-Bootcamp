from tkinter import *
import tkinter

window = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(window, text = "Music", variable = CheckVar1)
C2 = Checkbutton(window, text = "Video", variable = CheckVar2)
C1.pack()
C2.pack()
window.mainloop()
