#!/bin/python3
'''

ให้ชุดตัวเลข [2, 4] และ [16, 32, 96] เราต้องหาตัวเลขที่ตรงตามเงื่อนไขสองข้อ:

ตัวเลขในชุดแรก [2, 4] ต้องเป็นตัวหารของตัวเลขที่เรากำลังพิจารณา

ตัวเลขที่เรากำลังพิจารณาต้องเป็นตัวหารของตัวเลขในชุดที่สอง [16, 32, 96]

เริ่มจากเงื่อนไขแรก:

ตัวเลขต้องหารด้วย 2 และ 4 ลงตัว ตัวเลขที่เล็กที่สุดที่ตรงตามเงื่อนไขนี้คือ 4 ตัวเลขอื่นๆ ที่เป็นผลคูณของ 4 (เช่น 8, 12, 16, ฯลฯ) ก็จะตรงตามเงื่อนไขนี้เช่นกัน

ตอนนี้เรามาตรวจสอบเงื่อนไขที่สองสำหรับตัวเลขเหล่านี้:

4: 4 เป็นตัวหารของ 16, 32, และ 96

8: 8 เป็นตัวหารของ 16, 32, และ 96

12: 12 ไม่เป็นตัวหารของ 16, 32, และ 96

16: 16 เป็นตัวหารของ 16, 32, และ 96

ดังนั้นตัวเลขที่ตรงตามเงื่อนไขทั้งสองข้อคือ 4, 8, และ 16 นี่คือตัวเลขที่อยู่ระหว่างสองชุดนี้
'''



import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    max_a= max(a)
    min_b= min(b)
    counter = 0
    for i in range(max_a,min_b+1):
        counter+= (all([i % ax==0 for ax in a]) and all (bx%i==0 for bx in b)>0)
        # add counter if  item in array a is factor of array b 

    return counter
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
'''
a=[2,4]   #--> 4, 8, 12, 16
b=[16,32,96]
print(getTotalX(a,b))