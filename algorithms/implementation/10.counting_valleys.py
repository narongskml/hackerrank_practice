#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    pos = 0
    min_v = 0
    valley_count=0
    for c in path:
        if c=="U":
            pos+=1
        else:
            pos-=1                # find current position 
        
        if (pos<0):
            if (pos<min_v):       # find minimum of valley
                min_v=pos
        elif (pos==0):
            if (min_v<0):         # find path if from valley to groud=zero and reset then add couting valley 
                valley_count+=1
                min_v=0
                
    return valley_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
