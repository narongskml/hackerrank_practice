#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
        result = []
        while len(arr) > 0:
            min_val = min(arr)
            result.append(len(arr))
            arr = [x - min_val for x in arr if x - min_val > 0]
        return result



cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]) # [8, 6, 4, 1]
cutTheSticks([5, 4, 4, 2, 2, 8]) # [6, 4, 2, 1]