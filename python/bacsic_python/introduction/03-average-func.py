#Implement a function that:
#1. Is named avg
#2. Takes a variable number of integer arguments; it is guaranteed that at least one argument will be passed
#3. Returns the average value of the passed arguments as a float

#The implementation will be tested by a provided code stub on several input files. Each input file contains one line with space-separated arguments for the function. The function will be called with those arguments, and the returned result will be printed to the output with exactly 2 decimal places.

#Example
#3 arguments are read and passed to the function: 1, 2, and 3. The average is calculated to be (1 + 2 + 3) / 3 = 2.00. This is then returned as a float to be printed.

#Constraints

#• 1 ≤ number of arguments for the function ≤ 100

#• -100 ≤ value of passed arguments ≤ 100

#Input Format Format for Custom Testing In the first and only line, there are space-separated integers that denote the values to be passed to the function.

#Solution: -

#!/bin/python3

import math
import os
import random
import re
import sys

def avg(*args):
    if not args:
        raise ValueError("At least one argument is required.")
    
    total = sum(args)
    return float(total) / len(args)

# write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()