
from functools import reduce

nums=[3,2,5,6,7,8,9]

even_nums=list(filter(lambda a:a%2==0,nums))

print(even_nums)

doubles=list(map(lambda a:a*2,even_nums))

print(doubles)

sum=reduce(lambda a,b:a+b,doubles)

print(sum)

