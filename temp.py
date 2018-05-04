# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys, os # python modules for interacting with computer
from tkinter import filedialog # interface for opening a file explorer
from tkinter import * # * imports all files in tkinter 

 ## Data Directory GUI
'''Getting data directory so data can easily be imported 
using this format data = hs.load('*.dm3', stack=True) to import all dm3s in folder as a stack'''


root = Tk() # Tk() is a function in tkinter that opens a window
root.file = filedialog.askopenfile() # opens explorer window so you can find the folder of choice
#root.directory =  os.path.split(root.file)[0]
root.withdraw() # closes the tkinter window since it's unnecessary
#oldcwd = os.getcwd() # saves old called working directory (place where data is drawn from) as oldcwd use os.chdir(oldcwd) to go back
#os.chdir(root.directory) # sets new directory
#newcwd = os.getcwd() # saves new directory name as newcwd
path = root.file.name
file = open(path, 'r+')
file_by_line = file.readlines()
print(file_by_line)
Header_size = int(input("Number of lines in Header: ")