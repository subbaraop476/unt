
import mysql.connector as my
conn = my.connect(user="root",password="root",host="127.0.0.1",database="sathya")
curs = conn.cursor()
curs.execute("insert into employee values(101,'Ravi',125000.00)")
conn.commit()
conn.close()
print("Data Inserted")