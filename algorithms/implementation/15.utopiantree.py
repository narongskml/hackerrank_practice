#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    if(n%2==0):
        return int(pow(2,(n/2) +1) -1)
    else:
        return int(pow(2,((n+1)/2) +1) -2 )
