# find first num % i ==0

nums=[1,12,15,21,25,27]

for num in nums:
    if num%5==0:
        print (num)
        break #Go out of the loop
    else:
        print("Not Found")


nums=[1,12,151,21,251,27] 
for num in nums:
    print("*")
    if num%5==0:
        print (num)
        break
else:
    print("*****Not Found*****")