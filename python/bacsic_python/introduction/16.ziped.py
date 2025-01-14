#Student ID → ___1_____2_____3_____4_____5__               
#Subject 1   |  89    90    78    93    80
#Subject 2   |  90    91    85    88    86  
#Subject 3   |  91    92    83    89    90.5
#            |______________________________
#Average        90    91    82    90    85.5    << Output
# calc average score  using zip function

n, x = map(int, input().split())

score = []
for _ in range(x):
    score.append(map(float, input().split()))

for i in zip(*score):
    print(sum(i) / len(i))