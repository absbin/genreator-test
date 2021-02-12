import numpy  as np
#working_with_matrix
arr1=np.array([[1,2,3,7,8,9]
            ,[4,5,6,22,33,44]])

print(arr1)

print(arr1.ndim)
print(arr1.size)
arr2=arr1.flatten()
print(arr2)
arr3=arr2.reshape(2,2,3)
print(arr3)

matrix1=np.matrix(arr1)
print("matrix1 is :",matrix1)
matrix2=np.matrix('1,2,3,7,8,9;4,5,6,22,33,44')
print("matrix2 is :",matrix2)
print("Max matrix2 is :",matrix2.max())