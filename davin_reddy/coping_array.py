
from numpy import *

arr1=array([1,2,3,4,5,6])
arr2=arr1
arr3=arr1.view()
arr4=arr1.copy()
print("val arr1",arr1)
print("val arr2",arr2)
print("id arr1",id(arr1))
print("id arr2",id(arr2))
a=1
b=a
b=2
print("a is",a)
print("b is",b)

print("******************")

# shallow copy

print("arr1",id(arr1))
print("arr3",id(arr3),"Shallow copy")
arr3[0]=9
print("val arr1",arr1)
print("val arr2",arr2)
print("val arr3",arr3,"Shallow copy")
print("******************")
arr4[0]=55
print(" id arr4",id(arr4),"deep copy")
print("arr1",arr1)
print("arr2",arr2)
print("arr3",arr3)
print("arr4",arr4)


