import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#https://www.hackerrank.com/challenges/one-month-preparation-kit-counter-game/problem
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
def Game(x):
    if ((x & (x-1) == 0) and x != 0): 
        return (int(x/2))
    else:
        i = 1
        while i < x: 
            i *=2
        i/=2
        return(int(x-i))

def counterGame(n):
    # Write your code here
    #find start by Louise 
    if (n==1):
        return "Richard"
    
    counter =1
    game = n
    while (game>1):
        game = Game(game)
        counter+=1

    if (counter%2==0):
        return "Louise" 
    else:
        return "Richard"
    

print (counterGame(132))