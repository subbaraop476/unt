

import mysql.connector as my

conn = my.connect(user="root",password="root",host="127.0.0.1",database="sathya")
print(conn)
curs = conn.cursor()
print(curs)