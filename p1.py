from tkinter import Tk,Listbox
#tkinter module GUI application
win=Tk()
win.title("Demo GUI")
li=Listbox(win)
for i in range(1,10+1):
    li.insert(i,"Apple"+str(i))
li.pack()
win.mainloop()





