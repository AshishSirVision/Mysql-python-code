from mysql.connector import connect
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
def fun():
    if(t1.get() in ["localhost","127.0.0.1"]):
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
    else:
        showinfo(title='Information',message="plz try again")
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
def fun3():
    try:
        conn=connect(host=t1.get(),user=t2.get(),password=t3.get(),database=t4.get())
        cur=conn.cursor()
        cur.execute('''show tables''')
        for dt in cur:
            trv2.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0]))
    except Exception as e:
        #l4.config(text="database not created successfully")
        pass
def fun4():
    try:
        conn=connect(host=t1.get(),user=t2.get(),password=t3.get(),database=t4.get())
        cur=conn.cursor()
        cur.execute('''desc emp''')
        for dt in cur:
            print(dt[1])
            trv3.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
            
    except Exception as e:
        #l4.config(text="database not created successfully")
        pass
def fun5():
    try:
        conn=connect(host=t1.get(),user=t2.get(),password=t3.get(),database=t4.get())
        cur=conn.cursor()
        cur.execute('''select * from books''')
        for dt in cur:
            trv4.insert("", 'end',iid=dt[0],text=dt[0],values=(dt[0],dt[1]))
    except Exception as e:
        #l4.config(text="database not created successfully")
        print(e)
        
    

root=Tk()
root.geometry("700x400")
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
####################
trv2 = ttk.Treeview(root, selectmode ='browse')
trv2["columns"] = ("1")
# Defining heading
trv2['show'] = 'headings'
# width of columns and alignment 
trv2.column("1", width = 80, anchor ='c')
# Headings  
# respective columns
trv2.heading("1", text ="Tables")
####################
trv3 = ttk.Treeview(root, selectmode ='browse')
trv3["columns"] = ("1","2","3","4","5","6")
# Defining heading
trv3['show'] = 'headings'
# width of columns and alignment 
trv3.column("1", width = 80, anchor ='c')
trv3.column("2", width = 80, anchor ='c')
trv3.column("3", width = 80, anchor ='c')
trv3.column("4", width = 80, anchor ='c')
trv3.column("5", width = 80, anchor ='c')
trv3.column("6", width = 80, anchor ='c')



# Headings  
# respective columns
trv3.heading("1", text ="Field")
trv3.heading("2", text ="Type")
trv3.heading("3", text ="NULL")
trv3.heading("4", text ="Key")
trv3.heading("5", text ="default")
trv3.heading("6", text ="Extra")

####################
trv4 = ttk.Treeview(root, selectmode ='browse')
trv4["columns"] = ("1","2")
# Defining heading
trv4['show'] = 'headings'
# width of columns and alignment 
trv4.column("1", width = 80, anchor ='c')
trv4.column("2", width = 80, anchor ='c')

# Headings  
# respective columns
trv4.heading("1", text ="id")
trv4.heading("2", text ="name")


b1=Button(root,text="create database",command=fun)
b2=Button(root,text="show database",command=fun2)
b3=Button(root,text="show tables",command=fun3)
b4=Button(root,text="desc tables",command=fun4)
b5=Button(root,text="select table",command=fun5)

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
b3.place(x=250,y=260)
b4.place(x=350,y=260)
b5.place(x=450,y=260)

trv.place(x=120,y=310)
trv2.place(x=220,y=310)
trv3.place(x=320,y=310)
trv4.place(x=250,y=10)


root.mainloop()
