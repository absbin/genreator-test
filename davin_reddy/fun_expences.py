# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:49:27 2017

@author: ABSBIN
"""
def calculate_total(exp):
    total=0
    for items in exp:
        total=total+items
    return total  
    print ('total for' +exp + ' is = ' + str(total))
    

ali_exp=[1000,2000,3000,4000,5000]
abbas_exp=[2000,3000,4000,5000,6000]


ali_total=calculate_total(ali_exp)
abbas_total=calculate_total(abbas_exp)

print("ali's total expenses list is", ali_total)
print("abbas's total expenses list is", abbas_total)





