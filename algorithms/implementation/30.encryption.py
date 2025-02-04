'''
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L  be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:
    [sqrt(L)] <= row <= column <= [sqrt(L)], where [x] is the smallest integer greater than or equal to x.

Function Description

Complete the encryption function in the editor below.

encryption has the following parameter(s):

string s: a string to encrypt

Returns
string: the encrypted text

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(' ', '')
    L = len(s)
    row = math.floor(math.sqrt(L))
    col = math.ceil(math.sqrt(L))
    
    if row * col < L:
        row += 1
        col -= 1
        if row * col < L:
            col += 1
    result = ''
    for i in range(col):
        result += s[i::col] + ' '
    return result.strip()


encryption('if man was meant to stay on the ground god would have given us roots') #imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau



