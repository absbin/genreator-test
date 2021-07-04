# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:38:21 2017
 
@author: ABSBIN
"""

class RemoteControl():
    def __init__(self):
        self.channels=['abs','HBo','bbc','spain']
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]   

r=RemoteControl()    
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

        