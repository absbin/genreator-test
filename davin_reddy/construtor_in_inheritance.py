class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("This is the Feature1.")


class B(A):# single=level inheritance
    def __init__(self):
        print("In B init")
    def feature2(self):
        print("This is the Feature2.")


class C(A):# Multi=level inheritance
    def __init__(self):
        super().__init__()
        print("In C init")
    def feature3(self):
        print("This is the Feature3.")

class D(B,A):# MRO (Method resolution Order:Left fto Right)
    def __init__(self):
        super().__init__()
        print("In D init")
    def feature(self):
        super().feature2()



o1=A()
o2=B()
print("+++++++++Super().__init__()+++++++++++++")
o3=C()
print("*********MRO*************")
o4=D()
o4.feature()



