
class Car:

    wheel=4
    def __init__(self):
        self.mil=10
        self.com="BMW"


c1=Car()
c2=Car()

Car.wheel=5

c2.com="ikco"
print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)