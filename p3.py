from tkinter import Tk,Listbox
#tkinter module GUI application
win=Tk()
win.title("Demo GUI")
li=Listbox(win)
li.insert(1,"Apple")
li.insert(2,"Mango")
li.insert(3,"Grapes")
    
li.pack()
win.mainloop()





