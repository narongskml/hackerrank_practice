'''
David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

Each container contains only balls of the same type.
No two balls of the same type are located in different containers.

Example
containers = [[1, 4], [2, 3]]

David has n=2 containers and 2 different types of balls, both of which are numbered from 0 to n-1=1. 
The distribution of ball types per container are shown in the following

In a single operation, David can swap two balls located in different containers.
The diagram below depicts a single swap operation:

In this case, there is no way to have all green balls in one container and all red in the other 
using only swap operations. Return Impossible.

You must perform  queries where each query is in the form of a matrix, . For each query, 
print Possible on a new line if David can satisfy the conditions above for the given matrix. 
Otherwise, print Impossible.

Function Description
Complete the organizingContainers function in the editor below.

organizingContainers has the following parameter(s):

int containter[n][m]: a two dimensional array of integers that represent the number of balls of each color in each container

Returns: string: either Possible or Impossible


Input Format

The first line contains an integer q, the number of queries.

Each of the next q sets of lines is as follows:

1. The first line contains an integer n , the number of containers (rows) and ball types (columns).
2. Each of the next n lines contains n pace-separated integers describing row containter[i].
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    n = len(container)
    rows = [0] * n
    cols = [0] * n
    for i in range(n):
        for j in range(n):
            rows[i] += container[i][j]
            cols[j] += container[i][j]
            
    rows.sort()
    cols.sort()
    if rows == cols:
        return "Possible"
    else:
        return "Impossible" 
    

organizingContainers([[1, 4], [2, 3]]) #Impossible
organizingContainers([[0, 2], [1, 1]]) #Possible
organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]]) #Impossible
organizingContainers([[4, 5], [3, 6]]) #Possible


