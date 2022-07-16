from tkinter import *
#tkinter module GUI application
fruits=["dragon fruits","Apple","banana","grapes","pine apple","papaya"]
win=Tk()
win.title("Demo GUI 1")
win.geometry("400x400")
for i in range(1,len(fruits)):
    rb1=Radiobutton(win,value=i,text=fruits[i]+str(i))
    rb1.pack(side=TOP)
win.mainloop()





