#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
def flippingBits2(n):
    result = 0
    for i in range(31,-1,-1):
        if n//(2**i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += 2**i * x
    return result

def flippingBits(n):
    # Write your code here
    b=''
    
    while n>0:
        b+=str(n%2)
        n=n//2
    re=''
    for i in range(len(b)-1,-1,-1):
        re+=b[i]
    re=(32-len(re))*'0'+re
    flip=''
    for i in re:
        if i=='1':
            flip+='0'
        else:
            flip+='1'
    
    other=0
    j=31
    for i in range(0,len(flip)):
        other+=int(flip[i])*(2**j)
        j-=1
    return other
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
