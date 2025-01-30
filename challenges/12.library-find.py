#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here 
    if y1 < y2:
        return 0 
    if y1 > y2:
        return 10000
    if y1==y2 :
        if m1 < m2:
            return 0
        if m1 > m2:
            return 500 * (m1-m2)
        if m1 == m2:
            if d1 > d2:
                return 15 * (d1-d2)
            if d1 <= d2:
                return 0
        
   

libraryFine(9,6,2015,6,6,2015) #45
libraryFine(9,6,2015,9,6,2015) #0
libraryFine(9,6,2015,6,6,2014) #10000
libraryFine(9,6,2015,6,5,2015) #500
libraryFine(9,6,2015,5,6,2015) #150
libraryFine(9,6,2015,9,5,2015) #30
libraryFine(9,6,2015,8,6,2015) #15
