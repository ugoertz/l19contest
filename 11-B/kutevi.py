from math import gcd

N, K = [int(x) for x in input().split()]

x = 360
known = [int(x) for x in input().split()]
for a in known:
    x = gcd(x, a)

challenge = [int(x) for x in input().split()]
for y in challenge:
    if y % x == 0:
        print('YES')
    else:
        print('NO')

