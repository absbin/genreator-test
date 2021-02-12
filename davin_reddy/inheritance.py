class A:
    def feature1(self):
        print("This is the Feature1.")
    def feature2(self):
        print("This is the Feature2.")

class B(A):# single=level inheritance
    def feature3(self):
        print("This is the Feature3.")
    def feature4(self):
        print("This is the Feature4.")

class C(B):# Multi=level inheritance
    def feature5(self):
        print("This is the Feature5.")



o1=A()
o2=B()
o3=C()
o1.feature1()
o1.feature2()
print("222222")
o2.feature1()
o2.feature2()
o2.feature3()
o2.feature4()
print("333333")
o3.feature1()
o3.feature2()
o3.feature3()
o3.feature4()
o3.feature5()


