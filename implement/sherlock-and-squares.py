#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    n = math.ceil(math.sqrt(a))   #minimum number or square root of a
    
    m = math.floor(math.sqrt(b)) #maximum number or square root of b

    return m - n + 1  # find diff is count of squares

print(squares(3,9)) #2
print(squares(17,24)) #0
print(squares(1,100)) #10
print(squares(1,1000)) #31
print(squares(1,1000000000000000000))  #1000000000000000000

