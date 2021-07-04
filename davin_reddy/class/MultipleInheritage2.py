# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:31:48 2017

@author: ABSBIN
"""

class Father():
    def __init__(self):
        print('I am Father')
    def skills(self):
        print('I enjoy gardening')

class Mother():
    def __init__(self):
        print('I am Mother')
    def skills(self):
        print('I enjoy cooking')
        
# class child(Father,Mother):
class child(Mother,Father):
    def __init__(self):
        super().__init__()
        print('I love My family1')
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print('I enjoy sports')
        
c=child()
c.skills()
c.__init__()

