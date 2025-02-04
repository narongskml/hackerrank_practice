#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    maxh = max(height)
    if (k>maxh):
        return 0
    else:
        return maxh-k

k = 4
h = [1,6,3,5,2]
print (hurdleRace(k,h))  # expect 2