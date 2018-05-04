# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:06:53 2018

@author: kbs1
"""

from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    global a
    a=int(e.get())
    b=a*a
    print(b)

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()

