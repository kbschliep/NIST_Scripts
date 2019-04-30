# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys, os # python modules for interacting with computer
from tkinter import filedialog # interface for opening a file explorer
from tkinter import * # * imports all files in tkinter 
from tkinter import ttk
        
class Reorganizer_GUI:
            
    def __init__(self, master):
        self.master = master
        master.title("Data Reorganizer")

        self.label = Label(master, text="Data Reorganizer")
        self.label.pack()

        self.File_button = Button(master, text="Single File", command=self.file)
        self.File_button.pack()
        

        self.Folder_button = Button(master, text="Folder", command=self.folder)
        self.Folder_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
 
    def file(self):
        global data_by_line, Header_size, path
        def remove_header():
            global Header_size
            
            Header_size = int(Header_Entry.get())
            
            data = open(path, 'r+')
            data_by_line = data.readlines()
            level2 = Tk()
            S = Scrollbar(level2)
            close = Button(level2, text="Close", command=level2.destroy)
            close.pack()
            text = Text(level2, width=100, height=50)
            S.pack(side=RIGHT, fill=Y)
            text.pack(side=LEFT, fill=Y)
            S.config(command=text.yview)
            text.config(yscrollcommand=S.set)
            text.insert('1.0', data_by_line[Header_size:-1])
            level1.mainloop()
            
        root.file = filedialog.askopenfile() # opens explorer window so you can find the folder of choice
        path = root.file.name
        data = open(path, 'r+')
        data_by_line = data.readlines()
        
        level1 = Tk()
        
        Header_Entry = Entry(level1)
        Header_Entry.pack()

        

        text = Text(level1, width=100, height=50)
        S = Scrollbar(level1)
        close = Button(level1, text="Close", command=level1.destroy)
        close.pack()
        Enter = Button(level1, text="Enter", command=remove_header)
        Enter.pack()
        S.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, fill=Y)
        S.config(command=text.yview)
        text.config(yscrollcommand=S.set)
        text.insert('1.0', data_by_line)
        
        level1.mainloop()
       
        
        
        
#        level2 = Tk()
#        
#        Header = Entry(level2)
#        
#        child_button = Button(level2, Text="Remove Header",command=remove_header)
#        child_button.pack()


    def folder(self):
        print("Not done yet")
        
    
    
    
root = Tk() # Tk() is a function in tkinter that opens a window
my_gui = Reorganizer_GUI(root)


#root.file = filedialog.askopenfile() # opens explorer window so you can find the folder of choice
##root.directory =  os.path.split(root.file)[0]
#
##oldcwd = os.getcwd() # saves old called working directory (place where data is drawn from) as oldcwd use os.chdir(oldcwd) to go back
##os.chdir(root.directory) # sets new directory
##newcwd = os.getcwd() # saves new directory name as newcwd
#path = root.file.name
#file = open(path, 'r+')
#file_by_line = file.readlines()
#file_by_line[0:10]
#Header_size = int(input("Number of lines in Header: "))
#Header = file_by_line[0:Header_size]
#print(Header)
root.mainloop()
root.withdraw() # closes the tkinter window since it's unnecessary
# ## Data Directory GUI
#'''Getting data directory so data can easily be imported 
#using this format data = hs.load('*.dm3', stack=True) to import all dm3s in folder as a stack'''

