
class Student:

    school="Telesku"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self): #instance method
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is Student calss in abc module")


s1=Student(1,2,3)
s2=Student(4,5,6)

print(s1.avg())
print(s2.avg())

print(Student.getschool())
Student.info()
    
    

