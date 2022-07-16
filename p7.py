from tkinter import *
#tkinter module GUI application
fruits=["dragon fruits","Apple","banana","grapes","pine apple","papaya"]
win=Tk()
win.title("Demo GUI 1")
win.geometry("400x400")
for i in range(1,10):
    rb1=Radiobutton(win,text="Option "+str(i))
    rb1.pack(side=TOP)
win.mainloop()





