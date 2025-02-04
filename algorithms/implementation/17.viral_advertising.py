#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    likes = [2]
    for a in range(n - 1):
        likes.append((likes[-1] * 3) // 2)
    return sum(likes)