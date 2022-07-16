from tkinter import *
#tkinter module GUI application
fruits=["dragon fruits","Apple","banana","grapes","pine apple","papaya"]
win=Tk()
win.title("Demo GUI 1")
win.geometry("400x400")
li=Listbox(win,foreground="blue",bg="tomato")
index=1
for fruit in fruits:
    li.insert(index,fruit+str(index))
    index=index+1
li.pack(side=RIGHT)
win.mainloop()





