# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:26:05 2017

@author: ABSBIN
"""
import time
from multiprocessing import Pool

def f(n):
    sum=0
    for x in range(2000):
        sum += x*x
    return sum

if __name__=="__main__":
    
    t1=time.time()
    p=Pool()
    # result=p.map(f,range(40000))
    result=p.map(f,range(40))
    p.close()
    p.join()
    
    print("Pool took: ", time.time()-t1)
    
    result=[]
    t2=time.time()
    # for i in range(40000):
    for i in range(40):
        result.append(f(i))
    print("Serial processing took:", str(time.time()-t2))
    