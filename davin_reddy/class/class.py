# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:08:00 2017

@author: ABSBIN
"""

class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name + " plays tennis")
        elif self.occupation=="actor":
            print(self.name+' shoots film')
    def speaks(self):
        print(self.name,'Says Hello')
        
tom=Human("Tom cruise","actor")
tom.do_work()
tom.speaks()
       

tom=Human("Maria","tennis player")
tom.do_work()
tom.speaks()
               
        
        