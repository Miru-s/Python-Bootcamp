import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
combo = Combobox(window)

combo['value']=(1,2,3,4,5, "Text")
combo.current(3)
combo.grid(column=0, row=0)

window.mainloop()
