class Student:

    school='Telusko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value

    @classmethod
    def get_school(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("this is Student class in  abc module")




s1=Student(1,2,3)
s2=Student(4,5,6)

print("m1:",s1.m1)
print(s1.avg())
print(s2.avg())
print(s2.school)
print(s2.get_school())
print(Student.get_school())
print(Student.info())
print(s1.info())
print(s1)
