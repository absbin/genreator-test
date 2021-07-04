# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:25:34 2017

@author: ABSBIN
"""
# this progrAM IS RAN FROM command
import time
import multiprocessing

results=[]

def cal_square(numbers):
    global results
    for i  in numbers:
        time.sleep(1)
        print("square:"+ str(i*i))
        results.append(i*i)        
    print("results square:", results)

def cal_cube(numbers):
    for i  in numbers:
        time.sleep(1)
        print("cube:",i*i*i)
        results.append(i*i*i)
    print("results cube:", results)
    
if __name__ == "__main__":
    arr=[2,3,4,5,6]   
    p1=multiprocessing.Process(target=cal_square, args=(arr,))
    p2=multiprocessing.Process(target=cal_cube,   args=(arr,))        
    p1.start()
    p2.start()    
    p1.join()
    p2.join()    
    print("Done!")
    print("results: ",results)
#print("results square2:", results)            