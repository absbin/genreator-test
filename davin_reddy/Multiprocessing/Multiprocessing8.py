# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:34:59 2017

@author: ABSBIN
"""
# this progrAM IS RAN FROM command

import multiprocessing

def cal_square(numbers,res):
    global results
    for i  in numbers:
        print("square:"+ str(i*i))
        res.append(i*i)        
        print("results square inside loop:", res)
    print("results square:", res)

def cal_cube(numbers,res):
    for i  in numbers:
        print("cube:",i*i*i)
        res.append(i*i*i)
        print("results cube inside loop:", res)
    print("results cube:", res)
    
if __name__ == "__main__":
    arr=[2,3,4]   
    results=multiprocessing.Manager().list()
    p1=multiprocessing.Process(target=cal_square, args=(arr,results))
    p2=multiprocessing.Process(target=cal_cube,   args=(arr,results))        
    p1.start()
    p2.start()    
    p1.join()
    p2.join()    
    print("Done!")
    print("results: ",results)
#print("results square2:", results)            



