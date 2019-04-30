# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:23:00 2018

@author: kbs1
"""
## Packages
'''Import all the necessary packages and modules'''

from PyPDF2 import PdfFileWriter, PdfFileReader
import numpy as np # package for playing with matrices
import matplotlib.pyplot as plt
import sys, os # python modules for interacting with computer
from tkinter import filedialog # interface for opening a file explorer
from tkinter import * # * imports all files in tkinter 
import pandas as pd # useful for keeping cell structure and 2d data manipulation
import glob # helps find path 
## Data Directory GUI
'''Getting data directory so data can easily be imported 
using this format data = hs.load('*.dm3', stack=True) to import all dm3s in folder as a stack'''

root = Tk() # Tk() is a function in tkinter that opens a window
root.directory = filedialog.askdirectory() # opens explorer window so you can find the folder of choice
#root.file = fieldialog.askopenfilename()
root.withdraw() # closes the tkinter window since it's unnecessary
oldcwd = os.getcwd() # saves old called working directory (place where data is drawn from) as oldcwd use os.chdir(oldcwd) to go back
os.chdir(root.directory) # sets new directory
newcwd = os.getcwd() # saves new directory name as newcwd

path = root.directory + '/*.pdf' # creates path to data set folder directory. Change .csv to file type as needed
file_list=glob.glob(path)
output = PdfFileWriter()
for file in file_list:
    
    infile = PdfFileReader(file, 'rb')
    #print(file)

    for i in range(infile.getNumPages()):
        #print(i)
        p = infile.getPage(i)
        output.addPage(p)

with open('Cerutti - Words of the Day Combined.pdf', 'wb') as f:
    output.write(f)