# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:22:39 2017

@author: ABSBIN
"""
#optional arguments
import argparse
if __name__=="__main__":
    parser=argparse.ArgumentParser()
#    parser.add_argument("--number1", help="number one")
#    parser.add_argument("--number2", help="number two")
#    parser.add_argument("--operation", help="operation")
    parser.add_argument("--number1", default =4,help="number one")
    parser.add_argument("--number2", default =5,help="number two")
    parser.add_argument("--operation",default ="add", help="operation")

    
    args=parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    n1=int(args.number1)
    n2=int(args.number2)
    results=None
    
    if args.operation == "add":
        result= n1+n2
    elif args.operation == "sutract":
        result=n1-n2
    elif args.operation == "multiply":
        result=n1*n2
        
    print ("result is : " , result)
        