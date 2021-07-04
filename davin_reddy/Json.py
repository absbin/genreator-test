# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:16:14 2017

@author: ABSBIN
"""

book={}
book['bob']={
        'name': 'bob',
        'address': 'NARA',
        'phone':10917}

book['tom']={
        'name': 'tom',
        'address': 'NweYOrK',
        'phone':10912
        }

import json
s=json.dumps(book)
print(s)

with open("C:/abs/book.txt",'w') as f:
    f.write(s)



f=open('C:\\abs\\book.txt','r')
s=f.read()
print(s)

book2=json.loads(s)
print (book2)



print(book['bob']['address'])
