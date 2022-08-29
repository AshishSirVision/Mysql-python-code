#MYSQL   CONNECT    PYTHON
#MYSQL-CONNECTOR-PYTHON
#pip3 mysql-connector-python
#IDLE python interactive mode--->file-->open-->script--> click on location bar--type cmd

import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="")
print(conn)

