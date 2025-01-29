
#!/bin/python3

import math
import os
import random
import re
import sys

#  Medium 
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
#https://en.wikipedia.org/wiki/Magic_square way 3 x 3 metrix
magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]
def formingMagicSquare(s):
    # Write your code here
    # Flatten the input 3x3 matrix into a 1D list
    s_flat = [num for row in s for num in row]

    # Calculate the minimum cost to transform the input into a magic square
    min_cost = float('inf')
    for magic in magic_squares:
        cost = sum(abs(s_flat[i] - magic[i]) for i in range(9))  # sum cost each point  in each magic way
        min_cost = min(min_cost, cost)  #find min cost
    
    return min_cost







s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s))
v = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
print(formingMagicSquare(v))

l = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
print(formingMagicSquare(l))
'''  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

'''


        