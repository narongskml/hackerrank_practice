#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # Extract the AM/PM part
    period = s[-2:]
    # Extract the hour part
    hour = int(s[:2])
    # Extract the rest of the time
    rest_of_time = s[2:-2]
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM case
        if hour != 12:
            hour += 12
    
    # Format the hour to be two digits
    return f"{hour:02}{rest_of_time}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
