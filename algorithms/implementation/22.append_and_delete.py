#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING source
#  2. STRING target
#  3. INTEGER operations
#

def appendAndDelete(s, t, k):
    # Write your code here
    # Step 1: Find the length of the common prefix
    common_length = 0
    min_length = min(len(s), len(t))
    
    for i in range(min_length):
        if s[i] == t[i]:
            common_length += 1
        else:
            break   
    # Step 2: Calculate the total operations required
    deletions = len(s) - common_length
    appends = len(t) - common_length
    required_operations = deletions + appends    
    
    # Step 3: Check if the transformation is possible
    if k >= required_operations:
        # If we have enough operations, check if the remaining operations are even or zero
        if (k - required_operations) % 2 == 0:
            return "Yes"
        # If we have more operations than needed, we can delete and append repeatedly
        elif k >= len(s) + len(t):
            return "Yes"
    return "No"

source="hackerhappy"
target="hackerrank"
operations=9
print(appendAndDelete(source, target, operations))  # Output: Yes
source="aba"
target="aba"       
operations=7
print(appendAndDelete(source, target, operations))   # Output: Yes
source="ashley"
target="ash"
operations=2
print(appendAndDelete(source, target, operations))    # Output: No







