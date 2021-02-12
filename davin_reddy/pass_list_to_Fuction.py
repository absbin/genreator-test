
def count(lst):
    odd=0
    even=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[1,2,3,4,5,6,7,8,9]

even,odd=count(lst)
print("Even numbers are {} and odd numbers ar {}".format(even,odd))