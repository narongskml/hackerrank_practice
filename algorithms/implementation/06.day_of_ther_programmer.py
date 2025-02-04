#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
#Given a year, , find the date of the 256th day of that year 
#according to the official Russian calendar during that year. 
#Then print it in the format dd.mm.yyyy, where dd is the two-digit day,
#mm is the two-digit month, and yyyy is .
def dayOfProgrammer(year):
    # Write your code here
    isleafyear = False
    if (year==1918):
        return "26.09.1918"
    if (year%400==0):
        isleafyear=True
    elif (year%4==0 and year%100!=0):
        isleafyear=True
    
    if (year>=1700 and year<=1918):  #Julian calendar  leap year every 4 year
        if (year%4==0):
            isleafyear=True
    #leap year for 29 day for feb
    if (isleafyear):
        return "12.09."+str(year)
    else:
        return "13.09."+str(year)


print (dayOfProgrammer(1918))