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

pages_to_keep = [1,3,5,7,9,11,13,15,17,19,21] # page numbering starts from 0
infile = PdfFileReader('NewPDF.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i in pages_to_keep:
        p = infile.getPage(i)
        output.addPage(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)