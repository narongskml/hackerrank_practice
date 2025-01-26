# Solution
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:    # add =  from =  to ==
            res += '0';     # add +=  instead =
        else:
            res += '1';     # add +=  instead =

    return res

s = input()
t = input()
print(strings_xor(s, t))
