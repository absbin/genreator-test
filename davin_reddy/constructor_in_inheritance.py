class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")

b1=B()
b1.feature1()

class C():
    def __init__(self):
        print("in C init")

    def feature1(self):
        print("Feature 1-C is working")

    def feature4(self):
        print("Feature 4 is working")

class D(C,A):
    def __init__(self):
        super().__init__()
        print("in D init")
    def feat():
        return super().feature2()
c1=C()
c1.feature1()

print("**************")
d1=D()
d1.feature2()