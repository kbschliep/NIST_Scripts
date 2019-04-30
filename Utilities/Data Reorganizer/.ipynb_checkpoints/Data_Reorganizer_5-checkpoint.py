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
        
        def Output():
            global level2
            basename=os.path.splitext(path)[0]
            out_fn = basename + '_Reordered.csv'
            print('file output at '+out_fn)
            
            np.savetxt(out_fn, data_array_reordered, delimiter=",")
            level1.destroy()
            level2.destroy()
            level2.mainloop()
            
            
        def Reorder_Text():
            global text, path, data_by_line, data, data_delimited, data_array, lines, it_row, it_col, Header_size, Row_size, Column_size, last, data_array_reordered, iteration_length
            
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
                
                a+=1

            data_array = np.asarray(data_delimited)   
            
            if Column_size>data_array.shape[1]:
#                global Column_size
                
                Column_size=int(data_array.shape[1])
            
            reordered_shape_move = int(np.ceil(data_array.shape[0]/ Row_size))
            reordered_shape_col = int(Column_size*reordered_shape_move) 
            reordered_shape = np.append(Row_size,reordered_shape_col)
            data_array_reordered = np.empty(reordered_shape)
            iteration_length=np.arange(np.ceil(data_array.shape[0]/Row_size))
            for i in iteration_length:
                
                if i==iteration_length[-1]:
#                    print('i last')
                    last=int(data_array.shape[0])
                    last_size= int(last-i*Row_size)
                    it_row = int((i+1)*Row_size)
                    it_col = int((i+1)*Column_size)
                    data_array_reordered[0:last_size,int(i*Column_size):it_col]=data_array[int(i*Row_size):it_row,0:Column_size]
                
                else:
#                    print('i not last')
                    it_row = int((i+1)*Row_size)
                    it_col = int((i+1)*Column_size)
#                    print(it_row)
                    data_array_reordered[0:Row_size,int(i*Column_size):it_col]=data_array[int(i*Row_size):it_row,0:Column_size]
                
#            print(i)
            
            text.insert('1.0', data_array_reordered)
            
        
        def remove_header():
            global Header_size, path, text, data, Row_size, Column_size, Row_Entry, Column_Entry, level2
           
            Header_size = int(Header_Entry.get())
            data = pd.read_csv(path, delim_whitespace=True, skiprows=Header_size)
            data = data.values
#            data = open(path, 'r+')
#            data_by_line = data.readlines()
            level1.withdraw()
            level2 = Tk()
            
            pane = Frame(level2)
            pane.pack()
            
            
            Row_Entry = Entry(pane)
            Row_Entry.grid(row=0, column=0)
            Column_Entry= Entry(pane)
            Column_Entry.grid(row=1,column=1)
            
            Label1 = Label(pane, text='Rows')
            Label1.grid(row=0, column=1)
            
            Label1 = Label(pane, text='Columns')
            Label1.grid(row=1, column=1)
            
            S = Scrollbar(level2)
            S.pack(side=RIGHT, fill=Y)
            S.config(command=text.yview)
            
            close = Button(pane, text="Close", command=level2.destroy)
            close.grid(row=2, column=2)
            Reorder = Button(pane, text="Reorder", command=Reorder_Text)
            Reorder.pack()
            Output_button =Button(level2, text="Output", command=Output)
            Output_button.pack()
            
            text = Text(level2, width=100, height=50)
            text.pack(side=BOTTOM, fill=Y)
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
        
        pane = Frame(level1)
        pane.pack()
        
        Header_Entry = Entry(pane)
        Header_Entry.pack(side=LEFT)
        
        Frame_Label=Label(pane, text='Header Size')
        Frame_Label.pack(side=LEFT)
        
        text = Text(level1, width=100, height=50)
        S = Scrollbar(level1)
        S.config(command=text.yview)
        S.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, fill=X)
        text.config(yscrollcommand=S.set)
        text.insert('1.0', data_by_line)
        
        Enter = Button(pane, text="Enter", command=remove_header)
        Enter.pack(side=LEFT)      

        close = Button(pane, text="Close", command=level1.destroy)
        close.pack(side=LEFT)
 
        
        
        
        
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

