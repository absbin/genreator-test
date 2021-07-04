# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:42:34 2017

@author: ABSBIN
"""
import time

def cal_square(numbers):
    print("calculate the square of numbers ")
    for i  in numbers:
        time.sleep(.2)
        print(i*i,'\n')
        
        
def cal_cube(numbers):
    print("calculate the cube of numbers")
    for i  in numbers:
        time.sleep(.2)
        print(i*i*i,'\n')
        

arr=[2,3,4] 
       
t=time.time()    
cal_square(arr)
cal_cube(arr)

print("elapsed time is", time.time()-t)
print(" Hah I am done with all my work now")            