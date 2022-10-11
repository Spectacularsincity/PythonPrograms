import mysql.connector
from MySQLdb import connect

mydb = connect(host='localhost',user='root',passwd='1234',database='telusko')

mycursor=mydb.cursor() #work as pointers to work on particular location

mycursor.execute("select * from Student") # pgm to show the databases in our mysql

#result=mycursor.fetchall()
result=mycursor.fetchone()

for i in result:
    print(i)


