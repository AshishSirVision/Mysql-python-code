from tkinter import *
def mouseClick(ev):
    print("Hello")


def display():
    print("hi")

win=Tk()
lbl_un=Label(win,text="USERNAME : ");
lbl_un.pack()
e_un=Entry(win,text="");
e_un.pack()

btn=Button(win,text="LOGIN ",command=display);
btn.pack()
lbl_un.bind("<Button>",mouseClick)

win.mainloop()





