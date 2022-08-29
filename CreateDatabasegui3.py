from mysql.connector import connect
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
def fun():
    try:
        conn=connect(host=t1.get(),user=t2.get(),password=t3.get())
        cur=conn.cursor()
        cur.execute("create database "+str(t4.get()))
        #l4.config(text="database created successfully")
        msg="database created successfully"
        showinfo(title='Information',message=msg)
    except Exception as e:
        #l4.config(text="database not created successfully")
        msg="database not created successfully"
        showinfo(title='Information',message=msg)
def fun2():
    try:
        conn=connect(host=t1.get(),user=t2.get(),password=t3.get())
        cur=conn.cursor()
        cur.execute('''show databases''')
        for dt in cur:
            trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0]))
    except Exception as e:
        #l4.config(text="database not created successfully")
        pass
root=Tk()
root.geometry("400x400")
root.title("Connect with database")

t2=StringVar();
t2.set("root")
t3=StringVar();
t4=StringVar();
host_name=["localhost","127.0.0.1","192.168.1.12"]
t1=StringVar();
t1.set("--select servers--")
l1=Label(root,text="HostName :")
l2=Label(root,text="UserName :")
l3=Label(root,text="Password :")
ldb=Label(root,text="New Database name :")
l4=Label(root,text="status")
e1=OptionMenu(root,t1,*host_name)
e2=Entry(root,textvariable=t2)
e3=Entry(root,textvariable=t3,show = "*")
e4=Entry(root,textvariable=t4)
trv = ttk.Treeview(root, selectmode ='browse')
trv["columns"] = ("1")
# Defining heading
trv['show'] = 'headings'
# width of columns and alignment 
trv.column("1", width = 80, anchor ='c')
# Headings  
# respective columns
trv.heading("1", text ="Database")


b1=Button(root,text="create database",command=fun)
b2=Button(root,text="show database",command=fun2)

l1.place(x=50,y=10)
e1.place(x=150,y=10)
l2.place(x=50,y=60)
e2.place(x=150,y=60)
l3.place(x=50,y=110)
e3.place(x=150,y=110)
ldb.place(x=50,y=160)
e4.place(x=150,y=160)
l4.place(x=120,y=210)
b1.place(x=50,y=260)
b2.place(x=150,y=260)

trv.place(x=120,y=310)
root.mainloop()
