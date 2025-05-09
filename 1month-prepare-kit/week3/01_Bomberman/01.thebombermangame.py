#!/bin/python3
'''
 ny bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
Bomberman then repeats steps 3 and 4 indefinitely.
Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after  seconds.

For example, if the initial grid looks like:
...
.O.
...
it looks the same after the first second. After the second second, Bomberman has placed all his charges:
OOO
OOO
OOO

At the third second, the bomb in the middle blows up, emptying all surrounding cells:
O.O
...
O.O
Function Description

Complete the bomberMan function in the editory below.

bomberMan has the following parameter(s):

int n: the number of seconds to simulate
string grid[r]: an array of strings that represents the grid
Returns

string[r]: n array of strings that represent the grid in its final state
'''

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        return grid
    
    # Convert grid to 2D list for easier manipulation
    rows = len(grid)
    cols = len(grid[0])
    grid = [list(row) for row in grid]
    
    # If n is even, grid is fully bombed
    if n % 2 == 0:
        return ['O' * cols for _ in range(rows)]
    
    # Helper function to simulate one detonation cycle
    def detonate(grid):
        # Create a full bomb grid
        full = [['O' for _ in range(cols)] for _ in range(rows)]
        
        # For each bomb in original grid, clear it and its neighbors
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'O':
                    full[i][j] = '.'  # Clear bomb
                    # Clear four neighboring cells if valid
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            full[ni][nj] = '.'
        return full
    
    # For n >= 3, pattern repeats every 4 seconds after initial state
    # n=3: first detonation
    # n=5: second detonation
    # n=7: third detonation (same as n=3)
    # n=9: fourth detonation (same as n=5)
    n = n - 1  # Account for initial state
    if n % 4 == 2:  # n=3,7,11... (first detonation pattern)
        return [''.join(row) for row in detonate(grid)]
    else:  # n=5,9,13... (second detonation pattern)
        # Need two detonations: first detonate initial bombs, then detonate result
        first = detonate(grid)
        return [''.join(row) for row in detonate(first)]


if __name__ == '__main__':
    n=1
    grid=[
        "......."
        ,"...O.O."
        ,"....O.."
        ,"..O...."
        ,"OO...OO"
        ,"OO.O..."
    ]

    result = bomberMan(n,grid)
    for row in result:
        print(row)