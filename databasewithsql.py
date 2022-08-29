from mysql.connector import connect
from tkinter import*
def fun():
    try:
        conn=conect(host=t1.get(),user=t2.get(),password=t3.get())
        conn.cursor()
        cur.execute("create database "+str(t4.get()))
        l5.config(text="database created successfully")
    except Exception as e:
        l5.config(text="database not created successfully")
       
win=Tk()
win.title("create database")
win.geometry("400x400")

t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()

l1=Label(win,text="Hostname")
e1=Entry(win,textvariable=t1)
l2=Label(win,text="Username")
e2=Entry(win,textvariable=t2)
l3=Label(win,text="Password")
e3=Entry(win,textvariable=t3)
l4=Label(win,text="database name")
l5=Label(win,text="status")
e4=Entry(win,textvariable=t4)
b1=Button(win,text="connect with database",command=fun)
l1.place(x=50,y=10)
e1.place(x=150,y=10)
l2.place(x=50,y=60)
e2.place(x=150,y=60)
l3.place(x=50,y=110)
e3.place(x=150,y=110)
l4.place(x=50,y=160)
e4.place(x=150,y=160)
l5.place(x=120,y=210)
b1.place(x=120,y=260)      
win.mainloop
