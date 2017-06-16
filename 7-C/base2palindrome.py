from math import log, floor

M = int(input())
n = floor(log(M+1, 2))  # number of digits of "first half"
odd_length = M + 1 < 2**n + 2**(n-1)

M = M + 1 - 2**n
if not odd_length:
    M -= 2**(n-1)

s = bin(2**(n-1) + M)[2:]
if odd_length:
    s += ''.join(reversed(s[:-1]))
else:
    s += ''.join(reversed(s))
print(int(s, 2))

