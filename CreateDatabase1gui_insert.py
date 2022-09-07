from mysql.connector import connect
from tkinter import *
from tkinter import ttk
def fun():
    try:
        conn=connect(host="localhost",user="root",password="",database="db1")
        cur=conn.cursor()
        cur.execute("insert into %s values(%d,'%s',%d);"%(t1.get(),int(t2.get()),t3.get(),float(t4.get())))
        l4.config(text="data inserted successfully")
        conn.commit()
    except Exception as e:
        l4.config(text="data inserted not successfully"+str(e))
def fun2():
    try:
        conn=connect(host="localhost",user="root",password="",database="db1")
        cur=conn.cursor()
        cur.execute("select * from books")
        for dt in cur:
            trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2]))
            print(help(trv.insert))


    except Exception as e:
        l4.config(text="data inserted not successfully"+str(e))
        pass
    

root=Tk()
root.geometry("400x400")
root.title("Connect with database")
t1=StringVar();
t2=StringVar();
t3=StringVar();
t4=StringVar();
l1=Label(root,text="TableName :")
l2=Label(root,text="id :")
l3=Label(root,text="name :")
ldb=Label(root,text="price :")
l4=Label(root,text="status")
e1=Entry(root,textvariable=t1)
e2=Entry(root,textvariable=t2)
e3=Entry(root,textvariable=t3)
e4=Entry(root,textvariable=t4)

trv=ttk.Treeview(root,selectmode='browse')
trv["columns"]=("1","2","3")
trv["show"]="headings"

trv.column("1",width=80,anchor='c')
trv.column("2",width=80,anchor='c')
trv.column("3",width=80,anchor='c')
trv.heading("1",text="id")
trv.heading("2",text="name")
trv.heading("3",text="price")

b1=Button(root,text="Add values in table",command=fun)
b2=Button(root,text="show table",command=fun2)
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
b2.place(x=120,y=310)

trv.place(x=200,y=360)
root.mainloop()
