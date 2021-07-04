# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:31:48 2017

@author: ABSBIN
"""

class Father():
    def gardening(self):
        print('I enjoy gardening')

class Mother():
    def cooking(self):
        print('I enjoy cooking')
        
# class child(Father,Mother):
class child(Mother,Father):
    def sports(self):
        print('I enjoy sports')
        
c=child()
c.gardening()
c.cooking()
c.sports()