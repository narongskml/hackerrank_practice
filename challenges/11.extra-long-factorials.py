#!/bin/python3
#The factorial of the integer , written , is defined as: n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
#Complete the extraLongFactorials function in the editor below. It should print the result and return.
# extraLongFactorials has the following parameter(s):

# n: an integer
# constrain 1<= n <= 100
import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    return math.factorial(n)

print(extraLongFactorials(25))  # Output: 15511210043330985984000000