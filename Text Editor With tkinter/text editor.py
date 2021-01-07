from tkinter import *
from tkinter import filedialog
import os

class TextEditor:
    def __init__(self,master):
        self.url=0
        self.master=master
        # creating main menu
        main_menu=Menu(master)

        # add icon section
        self.new_icon = PhotoImage(file="icons2/new.png")
        self.open_icon = PhotoImage(file="icons2/open.png")
        self.save_icon = PhotoImage(file="icons2/save.png")
        self.save_as_icon = PhotoImage(file="icons2/save_as.png")
        self.exit_icon = PhotoImage(file="icons2/exit.png")
        self.copy_icon=PhotoImage(file="icons2/copy.png")
        self.cut_icon=PhotoImage(file="icons2/cut.png")
        self.paste_icon=PhotoImage(file="icons2/paste.png")
        self.clear_icon=PhotoImage(file="icons2/clear_all.png")
        self.find_icon=PhotoImage(file="icons2/find.png")
        self.tool_hide_icon=PhotoImage(file="icons2/tool_bar.png")
        #creating file menu

        file_menu=Menu(main_menu,tearoff=0)

        file_menu.add_command(label="New", image=self.new_icon,compound=LEFT,accelerator="Ctrl+N",command=self.new)
        file_menu.add_command(label="Open", image=self.open_icon,compound=LEFT,accelerator="Ctrl+O",command=self.open)
        file_menu.add_command(label="Save", image=self.save_icon,compound=LEFT,accelerator="Ctrl+S",command=self.save)
        file_menu.add_command(label="Save As", image=self.save_as_icon,compound=LEFT,accelerator="Ctrl+Alt+S",command =self.save_as)
        file_menu.add_command(label="Exit", image=self.exit_icon,compound=LEFT,accelerator="Ctrl+Q",command=self.exit)
        main_menu.add_cascade(label="File",menu=file_menu)

        #creating Edit menu

        edit_menu = Menu(main_menu, tearoff=0)

        edit_menu.add_command(label="Copy",image=self.copy_icon,compound=LEFT,accelerator="Ctrl+C",command=self.copy)
        edit_menu.add_command(label="Cut",image=self.cut_icon,compound=LEFT,accelerator="Ctrl+X",command=self.cut)
        edit_menu.add_command(label="Paste",image=self.paste_icon,compound=LEFT,accelerator="Ctrl+V",command=self.paste)
        edit_menu.add_command(label="Clear all",image=self.clear_icon,compound=LEFT,accelerator="Ctrl+Alt+X",command=self.clear_all)
        edit_menu.add_command(label="Find",image=self.find_icon,compound=LEFT,accelerator="Ctrl+F")

        main_menu.add_cascade(label="Edit",menu=edit_menu)

        # creating View Menu

        view_menu=Menu(main_menu,tearoff=0)
        view_menu.add_command(label="Tool Bar",image=self.tool_hide_icon,compound=LEFT)


        main_menu.add_cascade(label="View",menu=view_menu)

        #creating top toor bar

        tool_bar=Label(master,text="here",bg="blue")
        tool_bar.pack(side=TOP,fill=X)



        #creating top toor bar

        bottom_bar=Label(master,text="here",bg="blue")
        bottom_bar.pack(side=BOTTOM,fill=X)

        #creating text jone
        scroll_bar = Scrollbar(master)
        self.text_jone=Text(master,yscrollcommand=scroll_bar.set,relief=FLAT,wrap=WORD)
        scroll_bar.pack(fill=Y,side=RIGHT)
        self.text_jone.pack(fill=BOTH,expand=1)
        scroll_bar.config(command=self.text_jone.yview())


        master.config(menu=main_menu)

    #function jone
    def new(self,event=None):
        self.url=0
        self.text_jone.delete(1.0,END)

    def open(self,event=None):
        self.url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("Text", "*.txt"), ("All File", "*.*")))
        try:
            with open(self.url, "r") as f:
                text=f.read()
                self.text_jone.delete(1.0, END)
                self.text_jone.insert(INSERT,text)
        except:
            self.url=0
            return

    def save(self,event=None):
        if self.url !=0:
            with open(self.url,"w") as f:
                f.write(self.text_jone.get(1.0,END))


    def save_as(self,event=None):
        path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=(("Text", "*.txt"), ("All File", "*.*")))
        try:
            with open(path,"w") as f:
                f.write(self.text_jone.get(1.0,END))
                f.close()

        except:
            return

    def exit(self,event=None):
        self.master.quit()

    def copy(self,event=None):
        try:
            self.text_jone.clipboard_clear()
            self.text_jone.clipboard_append(self.text_jone.selection_get())
        except:
            return
    def cut(self,event=None):
        try:
            self.copy()
            self.text_jone.delete("sel.first","sel.last")
        except:
            return

    def paste(self):
        try:
            self.text_jone.insert(INSERT,self.text_jone.clipboard_get())
        except:
            return

    def clear_all(self):
        self.text_jone.delete(1.0,END)




def main():
    root=Tk()
    root.title("Text Editor")
    ob=TextEditor(root)
    root.mainloop()

if __name__=="__main__":
    main()

