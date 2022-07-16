from tkinter import *
#tkinter module GUI application
fruits=["dragon fruits","Apple","banana","grapes","pine apple","papaya"]
win=Tk()
win.title("Demo GUI 1")
win.geometry("400x800")
size=len(fruits)
for i in range(1,size):
    rb1=Checkbutton(win,text=fruits[i]+str(i),height=2,width=15)
    rb1.pack(side=LEFT)
win.mainloop()





