#array in python

from array import *
n=int(input("Enter the lentgth of aaray: "))

arr= array('i',[])
for i in range(n):
    x=int(input("Enter the array  :  "))
    arr.append(x)

print(arr)

val=int(input("Enter a valua to search in array: "))
print(arr.index(val))



