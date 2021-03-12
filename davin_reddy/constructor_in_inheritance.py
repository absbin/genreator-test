class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2-{} is working haha".format(self.__class__.__name__))

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")

b1 = B()
b1.feature1()
print(type(b1).__name__)
b1.feature2()
print("---------------------")

class C:
    def __init__(self):
        print("in C init")

    def feature1(self):
        print("Feature 1-{} is working".format(self.__class__.__name__))

    def feature4(self):
        print("Feature 4-C is working")

a = 5  # global

class D(C, A):# Micro Resolution Order
    def __init__(self):
        super().__init__()
        print("in D init")

    def feature1(self):
        return super().feature2()
    a = 2
    @classmethod
    def feat(cls):
        print("in feat")
        a = 1  # local
        print("a={}".format(a))
        print("Global a={}".format(globals()["a"]))
c1 = C()
c1.feature1()

print("*************************")
d1 = D()
d1.feature1()
d1.feature2()

print("==============")
d1.feat()
D.feat()