

idno = int(input("IDNO : "))
name = input("Name : ")
salary  = float(input("Salary : "))

import mysql.connector as my
conn = my.connect(user="root",password="root",host="127.0.0.1",database="sathya")
curs = conn.cursor()
curs.execute("insert into Employee values (%s,%s,%s)",(idno,name,salary))
conn.commit()
conn.close()
print("Data Inserted")