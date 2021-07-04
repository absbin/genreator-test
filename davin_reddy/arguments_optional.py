# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:59:47 2017

@author: ABSBIN
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:02:49 2017

@author: ABSBIN
"""

import argparse

if __name__=="__main__":
    
    parser=argparse.ArgumentParser()
    parser.add_argument('-n1','--number1',default=5,help="first number")
    parser.add_argument('--number2',default=10,help="second number")
    parser.add_argument("--operation",default="add", help="operation",\
                        choices=['add','subtract','multiply'])
    
    args=parser.parse_args()
    print (args.number1)
    print (args.number2)
    print (args.operation)

    n1=int(args.number1)
    n2=int(args.number2)
    result = None
    if args.operation == "add":
        result=n1+n2
    elif args.operation == "subtract":
        result=n1-n2
    elif args.operation == "multiply":
        result=n1*n2


    print("Result:",result)