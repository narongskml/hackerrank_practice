#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    strn=str(n)
    counter=0
    for i in strn:
        if int(i)!=0:
            if n%int(i)==0 :
                counter+=1
    return counter
    
print(findDigits(1012))  # Output: 3
print(findDigits(12))  # Output: 2
print(findDigits(123456789))  # Output: 3