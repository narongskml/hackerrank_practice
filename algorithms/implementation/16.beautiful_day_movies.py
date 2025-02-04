#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    beauti_day=0
    for day in range(i, j + 1):
        if abs(day - int("".join(list(reversed(str(day)))))) % k == 0:
            beauti_day += 1
    return beauti_day