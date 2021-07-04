
def update(x):
    print(id(x))
    x=8
    print("x",x)
    print(id(x))

a=10
print("a",a)
print(id(a))
update(a)
print("a",a)

print("*******List as input********")
def update2(x):

    print(id(x))
    x[1]=8
    print("x",x)
    print(id(x))

a=[10,20,30]
print("a",a)
print(id(a))
update2(a)
print("a",a)