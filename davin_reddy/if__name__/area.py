# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:51:52 2017

@author: ABSBIN
"""

    
def calculate_area(base=10,height=5):
    print("__name__ is: ",__name__)
    return 1/2*(base*height)

if __name__=="__main__":
    print('I am in area.py')
    a=calculate_area(12,20)
    print("area: " ,a )