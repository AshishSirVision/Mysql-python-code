from tkinter import Tk,Listbox
#tkinter module GUI application
fruits=["dragon fruits","Apple","banana","grapes","pine apple","papaya"]
win=Tk()
win.title("Demo GUI 1")
win.geometry("400x400")
li=Listbox(win,foreground="blue",bg="tomato")
for fruit in fruits:
    li.insert(1,fruit)
   
li.pack()
win.mainloop()





