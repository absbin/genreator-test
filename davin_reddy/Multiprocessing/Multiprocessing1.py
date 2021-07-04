# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:34:59 2017

@author: ABSBIN
"""
# this progrAM IS RAN FROM command
import time
import multiprocessing
#global 
def cal_square(numbers):
    for i  in numbers:
        print("square:"+ str(i*i))        

def cal_cube(numbers):
    for i  in numbers:
        print("cube:",i*i*i)
        
if __name__=="__main__":
    t1=time.time()
    arr=[2,3,4]   
    p1=multiprocessing.Process(target=cal_square, args=(arr,))
    p2=multiprocessing.Process(target=cal_cube,   args=(arr,))        
    p1.start()
    p2.start()    
    p1.join()
    p2.join()    
    print("Done! in :", str(time.time()-t1))            