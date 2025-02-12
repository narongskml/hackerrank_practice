#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#Complete the sumXor function in the editor below.

#sumXor has the following parameter(s):
#- int n: an integer

#Returns
#- int: the number of values found  for which n+x = n^x, where  is the bitwise XOR operator.

def sumXor(n):
    # Write your code here
    if (n == 0) :
        return 1
        
    count = bin(n).count('0') - 1 if n != 0 else 1
    return 2 ** count 
