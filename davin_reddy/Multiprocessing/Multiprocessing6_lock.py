# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 13:02:02 2017
@author: ABSBIN
"""
import time
import multiprocessing
def deposit(balance):
    for i in range(100):        
        # time.sleep(.01)
        balance.value+=1
def withraw(balance):
    for i in range(100):
        # time.sleep(.01)        
        balance.value-=1   
    
if __name__=="__main__":
    balance=multiprocessing.Value('i',200)
    d=multiprocessing.Process(target=deposit, args=(balance,))
    w=multiprocessing.Process(target=withraw, args=(balance,))

    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)