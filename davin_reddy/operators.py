print(5/3,'float division')
print(5//3,'int division')
print(0b0101,'biniary')

def bi(n):print(n,'in  binary:','{0:b}'.format(n))
bi(5)
bi(50)

x=0x55
bi(x)
bi(x<<4)
bi(x>>4)
bi(~x)