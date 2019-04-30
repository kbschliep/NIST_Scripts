# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys, os # python modules for interacting with computer
from tkinter import filedialog # interface for opening a file explorer
from tkinter import * # * imports all files in tkinter 
from tkinter import ttk
import numpy as np
import pandas as pd
        
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
        global data_by_line, Header_size, path, text, data
        
        def Reorder_Text():
            global text, path, data_by_line, data, data_delimited, data_array, lines, Header_size, Row_size, Column_size
            
            Row_size=int(Row_Entry.get())
            Column_size=int(Column_Entry.get())
            
            text.delete('1.0', END)
            data = pd.read_csv(path, skiprows=Header_size, delim_whitespace=True)
            data = data.values
#            data = open(path, 'r+')
#            data_by_line = data.readlines()
            data_delimited=[]
            a = 0
            for lines in data:
                
                data_delimited.append(lines)
#                data_delimited[a].split()
#                data_delimited.append(data_by_line[a].replace()) 
                
                a+=1
                print(a)
            data_array = np.asarray(data_delimited)   
            reordered_shape_columns = data_array.shape[0]/ Row_size
            reordered_shape = np.append(reordered_shape_columns,Column_size)
            data_array_reordered = np.empty(reordered_shape)
            for i in range(np.ceil(data_array.shape[0]/Row_size)):
                print(i)
            
            text.insert('1.0', data_array_reordered)
            
        
        def remove_header():
            global Header_size, path, text, data
            Header_size = int(Header_Entry.get())
            data = pd.read_csv(path, delim_whitespace=True, skiprows=Header_size)
            data = data.values
#            data = open(path, 'r+')
#            data_by_line = data.readlines()
            level1.withdraw()
            level2 = Tk()
            
            Row_Entry = Entry(level2)
            Row_Entry.pack()
            Column_Entry= Entry(level2)
            Column_Entry.pack()
            
            S = Scrollbar(level2)
            close = Button(level2, text="Close", command=level2.destroy)
            close.pack()
            Reorder = Button(level2, text="Reorder", command=Reorder_Text)
            Reorder.pack()
            text = Text(level2, width=100, height=50)
            S.pack(side=RIGHT, fill=Y)
            text.pack(side=LEFT, fill=Y)
            S.config(command=text.yview)
            text.config(yscrollcommand=S.set)
            text.insert('1.0', data_by_line[Header_size:-1])
            level1.mainloop()
        
        root.file = filedialog.askopenfile() # opens explorer window so you can find the folder of choice
        path = root.file.name
#        data = pd.read_csv(path, delim_whitespace=True)
#        data = data.values
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
        
        
#        level1.mainloop()
       
        
        
        
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

