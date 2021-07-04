# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:42:34 2017

@author: ABSBIN
"""
import time
import threading

def cal_square(numbers):
    print("calculate the square of numbers ")
    for i  in numbers:
        time.sleep(.2)
        print("square:",i*i)
        
        
def cal_cube(numbers):
    print("calculate the cube of numbers")
    for i  in numbers:
        time.sleep(.2)
        print("cube:",i*i*i)
        
arr=[2,3,4] 
       
t=time.time()    
t1=threading.Thread(target=cal_square, args=(arr,))
t2=threading.Thread(target=cal_cube  , args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("\nelapsed time is : ", time.time()-t)
print(" Hah I am done with all my work now")            