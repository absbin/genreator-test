# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:27:09 2017

@author: ABSBIN
"""

try:
   # print(1)
    raise MemoryError('memooory errrror')
except MemoryError as e:
    print(e)

print('******************')    
try:
   # print(1)
    raise Exception('memooory errrror')
except Exception as e:
    print(e)

print('******************')    
try:
    print(1)
    #raise Exception('memooory errrror')
except Exception as e:
    print(e)       

print('++++++++++++++++++++')    
try:
    1/0
except Exception as e:
    print(e)       