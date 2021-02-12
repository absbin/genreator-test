#array in python

from array import array

vals= array('i',[1,2,3,4,5]) # integer
vals2= array('u',['a','b','c','d']) # unicode array
vals3= array(vals.typecode,[a for a in vals]) # When I dont know the typecode

print(vals)
print(vals.typecode) 


for i in range(5):
    print(i,vals[i])

for i in range(5):
    print(vals3[i])
