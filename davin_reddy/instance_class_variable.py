wheel = 13


class Car:

    wheel = 4
    print(type(wheel))

    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()
print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil, c2.wheel)
Car.wheel = 5
print("************************")
c2.com = "ikco"
print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil, c2.wheel)
print("************************")

c1.wheel =6
Car.wheel=4 
print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil, c2.wheel)
