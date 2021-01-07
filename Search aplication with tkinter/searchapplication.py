from tkinter import *
import wikipedia
def wiki():
    key=input_entry.get()
    output_textbox.delete(1.0,END)
    try:
        answer=wikipedia.summary(key)
        output_textbox.insert(INSERT,answer)
    except:
        output_textbox.insert(INSERT, "Please check Your Internet connection or Enter valid key")
root=Tk()
root.title("Search Apllication")
input_frame=Frame(root)
input_entry=Entry(input_frame)
input_entry.pack()
input_button=Button(input_frame,text="Search",command=wiki)
input_button.pack()
input_frame.pack(side=TOP)
output_frame=Frame(root)
scroll_bar=Scrollbar(output_frame,)
scroll_bar.pack(side=RIGHT,fill=Y)
output_textbox=Text(output_frame,wrap=WORD,yscrollcommand=scroll_bar.set)
output_textbox.pack(side=LEFT)
scroll_bar.config(command=output_textbox.yview())

output_frame.pack()
root.mainloop()