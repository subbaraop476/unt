


import mysql.connector as my

conn = my.connect(user="root",password="root",host="127.0.0.1")
curs = conn.cursor()
curs.execute("create database sathya")
print(conn)
