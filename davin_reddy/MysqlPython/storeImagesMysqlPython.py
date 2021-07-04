
import mysql.connector
from PIL import Image

MyDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Tutorial"
)

MyCursor = MyDB.cursor()
MyCursor.execute(
    "create table if not exists Images (id integer(45) not null auto_increment primary key,Photo longblob not null)"
)

def InsertBlob(FilePath):
    with open(FilePath, "rb") as File:
        BinaryData = File.read()
    SQLStatement = "insert into Images (photo) values (%s)"
    MyCursor.execute(SQLStatement, (BinaryData,))
    MyDB.commit()


def RetrieveBlob(ID):
    SQLStatement2 = "select * from Images where id= '{0}'"
    MyCursor.execute(SQLStatement2.format(str(ID)))
    MyResult = MyCursor.fetchone()[1]
    StoreFilePath = "ImageOutput/Img{0}.png".format(str(ID))
    print(MyResult)
    with open(StoreFilePath, "wb") as File:
        File.write(MyResult)
        File.close()
    im = Image.open(open(StoreFilePath, 'rb'))
    im.show()


print("1.Insert Image\n2.Read Image; \nPlease select 1 or 2.")
MenuInput = input()
if int(MenuInput) == 1:
    UserFilePath = input("Enter File path:")
    InsertBlob(UserFilePath)
elif int(MenuInput) == 2:
    UserIDChoice = input("Enter ID:")
    RetrieveBlob(UserIDChoice)
