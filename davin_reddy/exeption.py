# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:46:54 2017

@author: ABSBIN
"""

x=input('Input a number 1:')
y=input('Input a number 2:')

try:
    z=int(x)/int(y)
except Exception as e:
    print ('ecption is occured', type(e).__name__)
    z=None
except Exception as e:
    print ('eception type : ', type(e).__name__)
    z=None

print("Division is : ", z) 
    



