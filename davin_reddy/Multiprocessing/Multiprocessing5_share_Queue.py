# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:34:59 2017

@author: ABSBIN
"""
# this progrAM IS RUN FROM command
import multiprocessing
def cal_square(numbers,q):
    for n in numbers: 
        q.put(n*n )
        
if __name__=="__main__":
    arr=[2,3,4]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=cal_square, args=(arr,q))  
    p.start()    
    p.join()
    while q.empty() is False:
        print(q.get())  
          