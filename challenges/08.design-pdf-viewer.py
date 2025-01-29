#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    height = -1
    for letter in word:
        height = max(height, h[ord(letter) - 97]) 
    return height * len(word)

'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
h = [1,3, 1 ,3, 1, 4, 1 ,3, 2 ,5 ,5, 5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5 ,5 ,5 ,5 ,5 ,5, 5]
w= "abc"
print(designerPdfViewer(h,w))