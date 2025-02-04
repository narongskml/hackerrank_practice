#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#
'''
There are a number of people who will be attending ACM-ICPC World Finals. 
Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, 
presented as binary strings, determine the maximum number of topics a 2-person team can know. 
Each subject has a column in the binary string, and a '1' means the subject is known while '0' 
means it is not. Also determine the number of teams that know the maximum number of topics. 
Return an integer array with two elements. The first is the maximum number of topics known, 
and the second is the number of teams that know that number of topics.
Example
n=3
topic=['10101', '11100', '11010']

These are all possible teams that can be formed:
Members Subjects
(1,2)   [1,2,3,4,5]
(1,3)   [1,3,4,5]
(2,3)   [1,2,3,4]

In this case, the first team will know all 5 subjects. 
They are the only team that can be created that knows that many subjects, '
so [5,1] is returned.
return int[2]  :the maximum topics and the number of teams that know that many topics
'''

def acmTeam(topic):
    # Write your code here
    n = len(topic)
    m = len(topic[0])
    max_topics = 0
    max_teams = 0
    for i in range(n):
        for j in range(i+1, n):
            team_topics = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            if team_topics > max_topics:
                max_topics = team_topics
                max_teams = 1
            elif team_topics == max_topics:
                max_teams += 1
    return [max_topics, max_teams]


acmTeam(['10101', '11100', '11010']) # [5, 1]
acmTeam(['10101', '11100', '11010','00101']) # [5, 2]

