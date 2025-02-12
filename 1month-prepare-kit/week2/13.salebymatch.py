#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
#There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.
#Example
#There is one pair of color  and one of color . 
# There are three odd socks left, one of each color. The number of pairs is .


def sockMerchant(n, ar):
    # Write your code here
    sock_dict = {}
    # Count socks
    for i in ar:
        if i in sock_dict:
            sock_dict[i] += 1
        else:
            sock_dict[i] = 1
    pairs = 0
    # Count pairs
    for i in sock_dict:
        pairs += sock_dict[i] // 2
    return pairs
