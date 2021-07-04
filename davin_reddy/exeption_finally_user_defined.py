# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:45:42 2017

@author: ABSBIN
"""

try:
    f=open("C:\\abs\\book.txt")
    x=1/0
except FileNotFoundError as e:
    print("inside except")
finally:
    f.close()
    print("cleaning up the file haha")
    
    
    