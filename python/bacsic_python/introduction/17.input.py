#In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

x, k = map(int,input().split(" "))
print(eval(input()) == k)


# input 
# 1 4
# x**3 + x**2 + x + 1

#Output: True