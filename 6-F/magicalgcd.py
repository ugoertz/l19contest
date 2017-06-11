from math import gcd
from functools import lru_cache
from itertools import groupby


@lru_cache(maxsize=None)
def cachedgcd(t0, t1):
    return gcd(t0, t1)


N = int(input())

for i in range(N):
    n = int(input())
    a = [int(x) for x in input().split()][:10000]
    b = [(x[0], len(list(x[1]))) for x in groupby(a)]

    # start with best result for "length 1" subsequence (already taking multiple
    # equal entries into account)
    result = max(x[0]*x[1] for x in b)

    # now look at longer subsequences
    bb = b[:]
    for ll in range(1, len(b)):  # subsequences of length ll+1
        bbb = []
        for j in range(len(b)-ll):
            t = gcd(bb[j][0], bb[j+1][0]), bb[j][1]+b[j+ll][1]
            result = max(result, t[0]*t[1])
            bbb.append(t)
        bb = bbb
    print(result)

