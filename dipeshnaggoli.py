from mysql.connector import *
from tkinter import*
def fun():
    try:
        conn=connect(host=t1.get(),user=t2.get(),password=t3.get())
        cur=com.cursor()
        cur.execute("create database"+str(t4.get()))
        l4.config(text="database careated successfully")
    except Exception as e:
        l4.config(text="database not created successfully")

win=Tk()
win.geometry("400x400")
win.title("Connect with database")
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()

l1=Label(win,text="HostName")
e1=Entry(win,textvariable=t1)
l2=Label(win,text="userName")
e2=Entry(win,textvariable=t2)
l3=Label(win,text="Password")
e3=Entry(win,extvariable=t3)
l4=Label(win,text="new database name:")
e4=Entry(win,textvariable=t4)

    
