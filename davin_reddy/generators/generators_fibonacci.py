# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:35:18 2017

@author: ABSBIN
"""
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib() :
    if  f<50:
        print(f)