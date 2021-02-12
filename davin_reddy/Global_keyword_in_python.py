# Global_keyword

a = 10  # global vaiable
b = 20  # global vaiable
print("Outside the function b= ", b)


def something():
    a = 11  # local variable
    print("In the finction a= ", a)

    global b
    b = 21
    print("In the finction b= ", b)


something()
print("Outside the function a= ", a)
print("Outside the function b= ", b)
