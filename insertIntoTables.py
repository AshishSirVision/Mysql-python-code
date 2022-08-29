#MYSQL   CONNECT    PYTHON
#MYSQL-CONNECTOR-PYTHON
#pip3 mysql-connector-python
#IDLE python interactive mode--->file-->open-->script--> click on location bar--type cmd

from mysql.connector import connect

conn=connect(host="localhost",user="root",password="",database="db1")

cur=conn.cursor()
cur.execute("insert into student values(111,'tom',18)")
conn.commit()
print("data inserted successfully")
