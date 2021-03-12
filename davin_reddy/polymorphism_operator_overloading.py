#synthetic sugar:(+)    (>)   (str)

a=5
b=6
print(a+b)#synthetic sugar
print(int.__add__(a,b))

a='5'
b='6'
print(a+b)
print(str.__add__(a,b))
print("*********************")
# Define operators like ADD (+) for special objects
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):#Add(+) operator overloading
        a1=self.m1+other.m1
        a2=self.m2+other.m2
        s3=Student(a1,a2)
        return s3

    def __gt__(self,other):#grater than(>) operator overloading
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
            
    def __str__(self):
        # return self.m1, self.m2
        return '{} , {}'.format(self.m1,self.m2)   
    @staticmethod
    def feaure1():#static method
        print ("This is feature 1 in staticmethod.")
    @classmethod
    def feaure2(cls):#class method
        print ("This is feature 2 in classmethod.")        

s1=Student(1,2)
s2=Student(3,4)

s3=s1+s2#===> __add__
print("s3=",s3)
print("5+6=",5+6)
print("5+6=",'5'+'6')
print("by >>>  Student.__add__(s1,s2): ",Student.__add__(s1,s2))
print("by >>>  S1.__add__(S2): ",s1.__add__(s2))
Student.feaure1()
Student.feaure2()

if s1>s2:#===> __gt__
    print("s1 wins.")
else :
    print("s2 wins.")

a=9
print(a.__str__())#===> __str__
print(s1.__str__())
