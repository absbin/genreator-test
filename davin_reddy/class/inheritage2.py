# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 07:26:09 2017

@author: ABSBIN
"""

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        print('main class')
    def Name(self):
        return self.firstname + " " + self.lastname
        #print('main class')

class Employee(Person):
    def __init__(self, first, last, staffnum):
        # Person.__init__(self,first, last)  # Avoid this.
        super().__init__(first, last)
        self.staffnumber = staffnum
        print('inherited1 class')
    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber
        print('inherited2 class')

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")
print('\n******************************\n')
print(x.Name())
print(y.GetEmployee())