

import mysql.connector as my
conn = my.connect(user="root",password="root",host="127.0.0.1",database="sathya")
curs = conn.cursor()
curs.execute("create table employee(idno integer,name varchar(50),salary integer)")
print("Table Created")
conn.close()
