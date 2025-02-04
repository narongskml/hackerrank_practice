'''Given a set of distinct integers, print the size of a maximal subset of  where the sum of any  numbers
 in  is not evenly divisible by .
#Example
 
One of the arrays that can be created is . Another is . After testing all permutations, 
the maximum length solution array has  elements.

Function Description

Complete the nonDivisibleSubset function in the editor below.

nonDivisibleSubset has the following parameter(s):

int S[n]: an array of integers
int k: the divisor
Returns

int: the length of the longest subset of  meeting the criteria
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Count the number of elements in each modulo group
    count = [0]*k
    for i in range(len(s)):
        count[s[i]%k] += 1
    
    # Initialize the result with the maximum number of elements in the first modulo group (0)
    result = min(count[0], 1)
    
    # Iterate over the modulo groups from 1 to k//2
    for i in range(1, k//2+1):
        if i != k-i:  # Skip the middle element if k is odd
            result += max(count[i], count[k-i]) 

    # If k is even, add one more to the result to account for the single middle element
    if k%2 == 0:
        result += 1 
    return result



nonDivisibleSubset(3,[1,7,2,4]) #3


