txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
print(txt.upper())

print(txt.strip(),'*****')
txt2 = "banana     "
print(txt2.capitalize())


a,b=1,2
dict1=dict(bob=a,fred=b)

txt3='\nthis is {bob} and that is {fred}\n'.format(**dict1)
print(txt3)
