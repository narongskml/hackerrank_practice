# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())  #no of shoes.
shoe_size = map(int, input().split())  # lis of all shoe size
N = int(input()) #no of customer

counter = Counter(shoe_size)
total_amt =0
for l in range(N):
        size, price = map(int, input().split())
        if(counter[size]!=0):
            total_amt+=price    #accrue earning amt
            counter[size]-=1    #decres shoe from stock     
        
print(total_amt)
