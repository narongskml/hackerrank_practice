#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    res = {}
    for i in range(5):
       res[i+1]=arr.count(i+1)
    mx= max(res.values())  #find max freq 

    for item,c in res.items():   #find first key is count = max fres
        if c==mx:
            return item
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
'''

print (migratoryBirds([1, 2 ,3, 4 ,5 ,4 ,3, 2,1 ,3 ,4]))