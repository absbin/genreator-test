
#Global_keyword using fuction globals()

a=10 #global vaiable

print ("id of a is ", id(a))
def something():
    a=11 # local variable
    print("In the finction a= ",a)
    x=globals()['a']# Access to global 
    print("id of x is ", id(x))
    globals()['a']=12

something()
print("Outside the function a= ",a)
