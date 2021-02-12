# Types_of_arguments


def add(a, b):  # formal argumrts
    c = a + b
    print(c)


add(5, 6)  # actual arguments (positional)


def person(name, age=10):
    print(name)
    print(age + 10)


person("abbas", 25)  # positional
person(age=36, name="Freind")  # actual arguments( keyword)
person(name="unanimous")  # actual arguments( Default)


def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


print("Sum of input numbers is : ", end="")
sum(5, 6, 7, 8, 10)  # actual arguments( Variable length)
