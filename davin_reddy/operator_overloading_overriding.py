print(5+6)#synthetic sugar
print(int.__add__(5,6))
print(str.__add__('5','6'))

print(int.__gt__(5,6))
print(5>6)

f=lambda a,b:a+b
result=print(f(5,6))