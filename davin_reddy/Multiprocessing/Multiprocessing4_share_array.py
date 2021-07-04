# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:34:59 2017

@author: ABSBIN
"""
# this progrAM IS RAN FROM command
import multiprocessing
def cal_square(numbers,result):
    for indx,n  in enumerate(numbers): 
        result[indx]=n*n        
        
if __name__=="__main__":
    arr=[2,3,4]
    result=multiprocessing.Array('i',3)
    p=multiprocessing.Process(target=cal_square, args=(arr,result))  
    p.start()    
    p.join()    
    print(result[:])
    print("result is :",str(result))  
          