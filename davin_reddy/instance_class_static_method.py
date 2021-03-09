a = 1  # gloal variable


class Student:
    school = "Telusko"  # Static variable
    global a
    a = 2

    def __init__(self, m1, m2, m3):
        # instance variable
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        a = 3  # local variable
        print("local a=", a)
        print("Global a=", globals()["a"])

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is Student class in  abc module")


@staticmethod
def total_info():
    print("this is totalInfo in  abc module")


s1 = Student(1, 2, 3)
s2 = Student(4, 5, 6)
print("m1:", s1.m1)
print(s1.avg())
s1.school = "Taha+++++++++"
print(s1.school)
print(Student.get_school())
print("-------------------------------------")
print(s1.school)
print(s2.school)
Student.school = "Abbas"
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print(s1.school)
print(s2.school)
print("***********" + s2.get_school())
print("***********", s2.get_school())
print(Student.get_school())
print(Student.info())
print(s1)
print(s1.info())