from tkinter import *
from tkinter.filedialog import askopenfilename
def NewFile():
    print("new file !")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")
root=Tk()
root.title("menu bar")
root.geometry("200x200")
me=Menu(root);
root.config(menu=me)
fileme=Menu(me);

me.add_cascade(label="File",menu=fileme)
fileme.add_command(label="New",command=NewFile)
fileme.add_command(label="Open",command=OpenFile)
fileme.add_separator()
fileme.add_command(label="Exit",command=root.quit)
helpme=Menu(me)
me.add_cascade(label="Help",menu=helpme)
helpme.add_command(label="About IDLE",command=About)
root.mainloop()
