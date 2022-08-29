#MYSQL   CONNECT    PYTHON
#MYSQL-CONNECTOR-PYTHON
#pip3 mysql-connector-python
#IDLE python interactive mode--->file-->open-->script--> click on location bar--type cmd

from mysql.connector import connect

conn=connect(host="localhost",user="root",password="")
print(conn)

#USING CONNECT REFERENCE CALL CURSOR FUNCTION
#AND CREATE OBJECT OF CURSOR
cur=conn.cursor();

#with the help cursor we can call execute function
#it able to perform any sql query
cur.execute("show databases")
print(cur.rowcount)
for i in cur:
    print(i)

