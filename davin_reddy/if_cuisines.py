# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:34:09 2017

@author: ABSBIN
"""

Iranian=['kabab', 'abgosht','kashk' ]
Indian=['samosa','daal','naan']
Italian=['pizza','pasta','risoto']

dish=input('Enter a dish :')

if dish in Iranian:
    print ('Iranian cuisine')
elif dish in Indian:
    print ('Indian cuisine')
elif dish in Italian:
    print('Italian cuisine')    
else:
    print("I don't know")
    
    
    
