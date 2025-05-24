#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
'''
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example
q = [1,2,3,5,4,6,7,8]
If person 5 bribes person 4, the queue will look like this: 1,2,3,5,4,6,7,8. Only 1 bribe is required. Print "1".

q=[4,1,2,3]
Person 4 had to bribe  3 people to get to the current position. Print "Too chaotic".

Function Description

Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):

int q[n]: the positions of the people after all bribes
Returns

No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than 2 people.
'''
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):  # from right to left 
        # check q[i] move more than 2
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        # check infront of q[i] in range [q[i]-2, i]
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:  # if number > current q[i]
                bribes += 1  # count
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
