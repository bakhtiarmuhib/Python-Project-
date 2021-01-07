from tkinter import *
from tkinter import filedialog
import os


def get_file():
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("Text","*.txt"),("All File","*.*")))
    try:
        with open(url,"r") as f:
            text.delete(1.0,END)
            text.insert(1.0,f.read())
    except:
        return

root=Tk()
text=Text(root)
text.pack()
button=Button(root,text="print",command=get_file)
button.pack()
root.mainloop()
