#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # Remove duplicates from the leaderboard and sort in descending order
    unique_scores = sorted(set(ranked), reverse=True)
                
    result = []
    i = len(unique_scores) - 1  # Start at the end of the unique scores
    
    # Iterate through each player's score
    for score in player:
        # Compare player's score with leaderboard scores
        while i >= 0 and score >= unique_scores[i]:
            i -= 1  # Move up the leaderboard
        
        # Rank is determined by the position in the unique scores
        result.append(i + 2)  # Add 2 because `i` is 0-based, and we need 1-based ranks
    
    return result


r=[100,90,90,80,75,60]
p=[50,65,77,90,102]

print(climbingLeaderboard(r,p))