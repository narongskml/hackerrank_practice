#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    l=len(a)
    freq = [0] * 101  # Since the constraint says numbers are in range 1 to 100
    # Count the frequency of each number in the array
    seta = set(a)
    for num in seta:
        freq[num]=a.count(num)

    mn = min(a)
    mx = max(a)
    max_length=0 
    for i in range(mn, mx+1):   #find long length  i, i+1
        max_length = max(max_length, freq[i] + freq[i - 1])

    return max_length

ar = [1,1,2,2,4,4,5,5,5]

print(pickingNumbers(ar)) # 5  [4,4,5,5,5]

a1 =  [4, 6, 5, 3, 3, 1]

print(pickingNumbers(a1)) # 3 [4,3,3]