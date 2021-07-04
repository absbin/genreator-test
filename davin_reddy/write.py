# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:57:05 2017

@author: ABSBIN
"""


#f=open("C:\\abs\\funny.txt",'w')
f=open('''C:/abs/funny.txt''',"w")
f.write("I Love ppoython")
f.close()


f=open('C:/abs/funny.txt',"a")
f.write("\nI Love ALL")
f.close()


f=open('''C:/abs/funny.txt''',"r")
print(f.read())
f.close()

print("\n*************************\n")
f=open('''C:/abs/funny.txt''',"r")
for line in f:
    print(line)
f.close()

print("\n++++++++++++++++++++++++++++++++++++++++++\n")
f=open('''C:/abs/funny.txt''',"r")
for line in f:
    tokens=line.split(' ')
    print(str(tokens))
f.close()

print("\n*************************\n")
f=open('''C:/abs/funny.txt''',"r")
f_out=open('''C:/abs/funny_wc.txt''',"w")
for line in f:
    tokens=line.split(' ')
    f_out.write(" wordcount: " +str(len(tokens))+'     '+line)
f.close()
f_out.close()
print(f.close())