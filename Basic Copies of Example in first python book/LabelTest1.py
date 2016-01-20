#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Python tkinter Label test')
root.minsize(100, 200)

s = Style()
s.theme_use('default')

for row in range(0, 3):
    root.grid_rowconfigure(row, weight=1)

for col in range(0, 3):
    root.grid_columnconfigure(col, weight=1)

Label_1 = Label(root, text='NotePad', anchor=N, background='red')
Label_1.grid(row=0, column=1, sticky=N+E+W)

Label_2 = Label(root, text='licensed under Gpl Version 3 Lucas', anchor=CENTER, background='green')
Label_2.grid(row=3, column=1, sticky=S)

Label_3 = Label(root, text="""the freedom to use the software for any purpose,
the freedom to change the software to suit your needs,
the freedom to share the software with your friends and neighbors, and
the freedom to share the changes you make.""", anchor=CENTER, background='green')
Label_3.grid(row=0, column=2, sticky=SE)

root.mainloop()
