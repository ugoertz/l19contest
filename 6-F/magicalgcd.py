from math import gcd
from itertools import groupby


N = int(input())

for i in range(N):
    n = int(input())
    a = [int(x) for x in input().split()]

    result = max(x[0] * len(list(x[1])) for x in groupby(a))

    g = a[0]
    for x, _ in groupby(a):
        if g == 1:
            break
        g = gcd(g, x)
    result = max(result, g * len(a))

    for i, x in enumerate(a):
        # Compute r = largest magical gcd of connected subsequences ending at
        # index i

        r = x
        g = x
        for j, y in enumerate(reversed(a[:i])):
            if g * (i+1) < result:
                # no chance that going further could help
                break
            g = gcd(g, y)
            r = max(r, g * (j+2))

        result = max(result, r)

    print(result)

