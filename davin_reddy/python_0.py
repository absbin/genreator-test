# -*- coding: utf-8 -*-
"""
A game:
    how to Guess a Number

Created on Tue Dec 26 09:05:21 2017

@author: ABSBIN

"""
    
    
import sys
import numpy as np

def main():
    print("Hello World!")
    print("Guess number between 1 to 100")
    randomNumber=35
    randomNumber=np.random.randint(1,100)
    
    
    found=False
    while not found:
        userGuess= int(input("Your guess: "))
        if userGuess == randomNumber:
            print("you got it!")
            found= True
        elif userGuess >randomNumber:
            print("You guess is Higher")
        else:
            print(" You guess is Lower")
            

if __name__=="__main__":
    main()
