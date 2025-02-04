'''
You will be given a square chess board with one queen and a number of obstacles placed on it. 
Determine how many squares the queen can attack.

A queen is standing on an  n x n chessboard. The chess board's rows are numbered from 1 to n, 
going from bottom to top. Its columns are numbered from 1 to n, 
going from left to right. Each square is referenced by a tuple, (r,c) describing the row, r, and column, c, 
where the square is located.
 
The queen is standing at position (rq, cq). In a single move, she can attack any square in any of the eight directions
 (left, right, up, down, and the four diagonals). In the diagram below, 
 the green circles denote all the cells the queen can attack from (4,4):

 There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. 
 For example, an obstacle at location (3,5) in the diagram above prevents the queen from attacking cells (3,5),(2,6), 
 (1,7)  :

 Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at (rq,cq). 
 In the board above, there are  such squares.

 Function Description

Complete the queensAttack function in the editor below.

queensAttack has the following parameters:
- int n: the number of rows and columns in the board
- nt k: the number of obstacles on the board
- int r_q: the row number of the queen's position
- int c_q: the column number of the queen's position
- int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle

Returns
- int: the number of squares the queen can attack

Input Format

The first line contains two space-separated integers n and k, the length of the board's sides and the number of obstacles.
The next line contains two space-separated integers  rq and c, the queen's row and column position.
Each of the next k lines contains two space-separated integers r[i] and c[i], the row and column position of obstacle i.

Constraints
- 1 <= n <= 10^9
- 0 <= k <= 100
- 1 <= rq, cq, r[i], c[i] <= n


'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n  is number of rows and columns in the board
#  2. INTEGER k  is the number of obstacles on the board
#  3. INTEGER r_q   is the row number of the queen's position
#  4. INTEGER c_q   is the column number of the queen's position
#  5. 2D_INTEGER_ARRAY obstacles
#
#  return the number of squares the queen can attack

def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    obstacles = set(tuple(map(tuple, obstacles)))
    directions = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)] # up-left, up, up-right, left, right, down-left, down, down-right

    # Count the number of squares the queen can attack in each direction
    for dy, dx in directions:
        y, x = r_q, c_q
        while True:
            y += dy
            x += dx
            if not (1 <= y <= n):
                break
            if not (1 <= x <= n):
                break
            if (y,x) in obstacles:
                break
            count +=1
    
    return count

print(queensAttack(1, 0, 1, 1, []))  # 0
print(queensAttack(4, 0, 4, 4, []))  # 9
print(queensAttack(5, 3, 4, 3, [(5, 5), (4, 2), (2, 3)]))  # 10













