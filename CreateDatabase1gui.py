from mysql.connector import connect
from tkinter import *
def fun():
    try:
        conn=connect(host=t1.get(),user=t2.get(),password=t3.get())
        cur=conn.cursor()
        cur.execute("create database "+str(t4.get()))
       l4.config(text="database created successfully")
        
    except Exception as e:
        l4.config(text="database not created successfully")
    
root=Tk()
root.geometry("400x400")
root.title("Connect with database")
t1=StringVar();
t2=StringVar();
t3=StringVar();
t4=StringVar();
l1=Label(root,text="HostName :")
l2=Label(root,text="UserName :")
l3=Label(root,text="Password :")
ldb=Label(root,text="New Database name :")
l4=Label(root,text="status")
e1=Entry(root,textvariable=t1)
e2=Entry(root,textvariable=t2)
e3=Entry(root,textvariable=t3)
e4=Entry(root,textvariable=t4)

b1=Button(root,text="connect with database",command=fun)
l1.place(x=50,y=10)
e1.place(x=150,y=10)
l2.place(x=50,y=60)
e2.place(x=150,y=60)
l3.place(x=50,y=110)
e3.place(x=150,y=110)
ldb.place(x=50,y=160)
e4.place(x=150,y=160)
l4.place(x=120,y=210)
b1.place(x=120,y=260)
root.mainloop()
