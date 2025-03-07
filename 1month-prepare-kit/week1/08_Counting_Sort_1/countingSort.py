#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# นับ ตัวเลข 1-100 กรณี ซ้ำ ให้เพิ่มค่า 

def countingSort(arr):
    # Write your code here
    totalLen=len(arr)
    countItem = [0]*100
    for i in range(0,totalLen):
        tValue = arr[i]
        countItem[tValue] += 1
        
    return countItem
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
