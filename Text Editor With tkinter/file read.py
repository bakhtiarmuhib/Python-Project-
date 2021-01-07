from tkinter import *
from tkinter import filedialog

import os


url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("Text","*.txt"),("All File","*.*")))

with open(url,"r")  as f:
    print(f.read())