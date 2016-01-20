#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Python tkinter Label test')
root.minsize(1000, 1000)

s = Style()
s.theme_use('default')

for row in range(0, 9):
    root.grid_rowconfigure(row, weight=10)

for col in range(0, 9):
    root.grid_columnconfigure(col, weight=10)

Label_0_0 = Label(root, text='♖', anchor=N, background='brown')
Label_0_0.grid(row=0, column=0, sticky= S+N+E+W)

Label_0_1 = Label(root, text='♞', anchor=N, background='yellow')
Label_0_1.grid(row=0, column=1, sticky= S+N+E+W)

Label_0_2 = Label(root, text='', anchor=N, background='brown')
Label_0_2.grid(row=0, column=2, sticky= S+N+E+W)

Label_0_3 = Label(root, text='', anchor=N, background='yellow')
Label_0_3.grid(row=0, column=3, sticky= S+N+E+W)

Label_0_4 = Label(root, text='', anchor=N, background='brown')
Label_0_4.grid(row=0, column=4, sticky= S+N+E+W)

Label_0_5 = Label(root, text='', anchor=N, background='yellow')
Label_0_5.grid(row=0, column=5, sticky= S+N+E+W)

Label_0_6 = Label(root, text='', anchor=N, background='brown')
Label_0_6.grid(row=0, column=6, sticky= S+N+E+W)

Label_0_7 = Label(root, text='', anchor=N, background='yellow')
Label_0_7.grid(row=0, column=7, sticky= S+N+E+W)

Label_0_8 = Label(root, text='', anchor=N, background='brown')
Label_0_8.grid(row=0, column=8, sticky= S+N+E+W)

Label_0_9 = Label(root, text='', anchor=N, background='yellow')
Label_0_9.grid(row=0, column=9, sticky= S+N+E+W)

Label_1_0 = Label(root, text='', anchor=N, background='yellow')
Label_1_0.grid(row=1, column=0, sticky= S+N+E+W)

Label_2_0 = Label(root, text='', anchor=N, background='brown')
Label_2_0.grid(row=2, column=0, sticky= S+N+E+W)
