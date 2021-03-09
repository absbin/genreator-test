# We stored data in test_database in student tabel  at MySql database which is running
import mysql.connector
print("Hello world")
mydb = mysql.connector.connect(
    host="localhost", user="Abbas", password="1234")
mycursur = mydb.cursor()
mycursur.execute("show databases")

for i in mycursur:
    print(i)

mycursur.execute("use test_database")
mycursur.execute("select * from student")  # or below line
mycursur.fetchall()

for i in mycursur:
    print(i)

print("Done!")
