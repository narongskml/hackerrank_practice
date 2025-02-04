#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0
    while True:
        i = (i + k) % n
        e -= 1
        if c[i] == 1:
            e -= 2
        if i == 0:
            return e

c=[0, 0, 1, 0, 0, 1, 1, 0]
k=2
print(jumpingOnClouds(c, k))  # Output: 92
c=[1 ,1 ,1 ,0 ,1 ,1 ,0, 0 ,0 ,0]
k=3
print(jumpingOnClouds(c, k))  # Output: 80

