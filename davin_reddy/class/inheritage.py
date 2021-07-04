# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:38:29 2017

@author: ABSBIN
"""

class Vehicle:
    def general_usage(self):
        print('General use is transprtation')

class Car(Vehicle):
    def __init__(self):
        print ('I am a Car')
        self.wheels=4
        self.has_roof=True
    def specific_usage(self):
        self.general_usage()
        print('Specific use: to commue to work, vacation\n')
        
        
        

class MotorCycle(Vehicle):
    def __init__(self):
        print ('I am a MotorCycle')
        self.wheels=2
        self.has_roof=False
    def specific_usage(self):
        self.general_usage()
        print('Specific use: to trip\n')
        
        
        
c=Car()
c.specific_usage()
print('\n******************************\n')
m=MotorCycle()
m.specific_usage()