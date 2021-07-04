# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:04:38 2017

@author: ABSBIN
"""

exp=[1000,2000,3000,4000,5000]
total=0
for items in exp:
    total=total+items
    print ('total is = ' + str(total))

for i in range(len(exp)  )  :
    total=total + exp[i]
    print('tatal is = ' + str (total))
    