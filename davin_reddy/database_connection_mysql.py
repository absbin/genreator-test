# We stored data in test_database in student tabel  at MySql database which is running
import mysql.connector
print("Hello world")
mydb = mysql.connector.connect( host="localhost", user="Abbas", password="1234")
mycursur = mydb.cursor()
mycursur.execute("show databases")
print("------!")
for i in mycursur:
    print(i)
print("+++++++!")
mydb = mysql.connector.connect( host="localhost", user="Abbas", password="1234",database="test_database")
mycursur = mydb.cursor()
mycursur.execute("select * from student")  # or below line
for i in mycursur:
    print(i)
print("*********!")

# mycursur.execute("use test_database")
mycursur.execute("select * from student")  # or below line
result= mycursur.fetchall()
for i in result:
    print(i)
print("OOOOOOOOOO!")

# mycursur.execute("use test_database")

mycursur.execute("select * from student")  # or below line
result= mycursur.fetchone()
for i in result:
    print(i)
print("Add-Delet Add-Delet Add-Delet Add-Delet!")
mydb = mysql.connector.connect( host="localhost", user="Abbas", password="1234",database="test_database")
mycursur = mydb.cursor()
mycursur.execute("insert into student values ('c','c3'), ('d','d4');")

mycursur.execute("delete from student where name='d'")

mycursur.execute("select * from student")  # or below line
result= mycursur.fetchall()
for i in result:
    print(i)

print("Done!")