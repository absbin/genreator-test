# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:50:48 2017

@author: ABSBIN
"""
class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle(self):
        print("(user defined exception >  ",
              'take detour)  :  ', self.msg)


try:
    raise Accident('crash between two cars')
except Accident as e:
    e.handle()
    
