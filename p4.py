from tkinter import Tk,Listbox
#tkinter module GUI application
fruits=["dragon fruits","Apple","banana","grapes","pine apple","papaya"]
win=Tk()
win.title("Demo GUI")
li=Listbox(win)
for i in range(0,len(fruits)):
    li.insert(i,fruits[i])
   
li.pack()
win.mainloop()





