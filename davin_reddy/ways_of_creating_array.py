
from numpy import *

arr1=array([1,2,3,4,5.0,6])# all arrays coonverted to float

print("arr1 type is",arr1.dtype)
arr1=array([1,2,3,4,5.0,6],int)# specify the type of array

print("arr1 type is ",arr1.dtype)

arr2=logspace(1,40,5)

print(arr2)
print('%.2f' %arr2[3])
print('%.4f' %arr2[3])