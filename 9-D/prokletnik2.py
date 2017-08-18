from functools import lru_cache
from bisect import bisect_left
from math import log, floor

N = int(input())
a = [int(x) for x in input().split()]
Q = int(input())
cache = {}

LEFTMAX = 0
LEFTMIN = 1
RIGHTMAX = 2
RIGHTMIN = 3
MINMAX = 4
MAXMIN = 5


maxsl = [list(range(len(a))), ]
while len(maxsl[-1]) > 1:
    l = []
    for i in range(len(maxsl[-1])//2):
        if a[maxsl[-1][2*i]] >= a[maxsl[-1][2*i+1]]:
            l.append(maxsl[-1][2*i])
        else:
            l.append(maxsl[-1][2*i+1])
    maxsl.append(l)
maxsr = [list(range(len(a))), ]
while len(maxsr[-1]) > 1:
    l = []
    for i in range(len(maxsr[-1])//2):
        if a[maxsr[-1][2*i]] > a[maxsr[-1][2*i+1]]:
            l.append(maxsr[-1][2*i])
        else:
            l.append(maxsr[-1][2*i+1])
    maxsr.append(l)


minsl = [list(range(len(a))), ]
while len(minsl[-1]) > 1:
    l = []
    for i in range(len(minsl[-1])//2):
        if a[minsl[-1][2*i]] <= a[minsl[-1][2*i+1]]:
            l.append(minsl[-1][2*i])
        else:
            l.append(minsl[-1][2*i+1])
    minsl.append(l)
minsr = [list(range(len(a))), ]
while len(minsr[-1]) > 1:
    l = []
    for i in range(len(minsr[-1])//2):
        if a[minsr[-1][2*i]] < a[minsr[-1][2*i+1]]:
            l.append(minsr[-1][2*i])
        else:
            l.append(minsr[-1][2*i+1])
    minsr.append(l)


@lru_cache(maxsize=None)
def indexminl(L, R):
    '''
    The left-most index for a where the global minimum of the interval [a_L,
    ..., a_R] is assumed.
    '''

    if L == R:
        return L

    for i in range(16, -1, -1):
        if L % 2**i == 0:
            if L + 2**i - 1 == R:
                return minsl[i][L // 2**i]
            if L + 2**i - 1 < R:
                im = indexminl(L + 2**i, R)
                if a[minsl[i][L // 2**i]] <= a[im]:
                    return minsl[i][L // 2**i]
                else:
                    return im
    print('imin', L, R)


@lru_cache(maxsize=None)
def indexmaxl(L, R):
    '''
    The left-most index for a where the global maximum of the interval [a_L,
    ..., a_R] is assumed.
    '''

    # print('imax start', L, R)

    assert L <= R
    if L == R:
        return L

    for i in range(16, -1, -1):
        if L % 2**i == 0:
            if L + 2**i - 1 == R:
                return maxsl[i][L // 2**i]
            if L + 2**i - 1 < R:
                # print(i, L, R, indexmax(L + 2**i, R))
                im = indexmaxl(L + 2**i, R)
                if a[maxsl[i][L // 2**i]] >= a[indexmaxl(L + 2**i, R)]:
                    return maxsl[i][L // 2**i]
                else:
                    return indexmaxl(L + 2**i, R)
    print('imax', L, R)


@lru_cache(maxsize=None)
def indexminr(L, R):
    '''
    The right-most index for a where the global minimum of the interval [a_L,
    ..., a_R] is assumed.
    '''

    if L == R:
        return L

    for i in range(16, -1, -1):
        if L % 2**i == 0:
            if L + 2**i - 1 == R:
                return minsr[i][L // 2**i]
            if L + 2**i - 1 < R:
                im = indexminr(L + 2**i, R)
                if a[minsr[i][L // 2**i]] < a[im]:
                    return minsr[i][L // 2**i]
                else:
                    return im
    print('iminr', L, R)


@lru_cache(maxsize=None)
def indexmaxr(L, R):
    '''
    The right-most index for a where the global maximum of the interval [a_L,
    ..., a_R] is assumed.
    '''

    # print('imax start', L, R)

    assert L <= R
    if L == R:
        return L

    for i in range(16, -1, -1):
        if L % 2**i == 0:
            if L + 2**i - 1 == R:
                return maxsr[i][L // 2**i]
            if L + 2**i - 1 < R:
                # print(i, L, R, indexmax(L + 2**i, R))
                im = indexmaxr(L + 2**i, R)
                if a[maxsr[i][L // 2**i]] > a[indexmaxr(L + 2**i, R)]:
                    return maxsr[i][L // 2**i]
                else:
                    return indexmaxr(L + 2**i, R)
    print('imaxr', L, R)


def max_magic(L, R, info=None):
    '''
    Returns length of maximal magic subsequence between L, R.
    '''

    # print('mm', L, R)

    if L == R:
        return 1
    if L == R - 1:
        return 2

    try:
        return cache[L, R]
    except KeyError:
        pass

    if info == LEFTMAX:
        il = indexminl(L, R)
        if il == L:
            best = R - L + 1
        else:
            ir = indexminr(L, R)
            best = ir - L + 1
            if R - il >= best:
                best = max(best, max_magic(il, R, LEFTMIN))
    elif info == RIGHTMAX:
        ir = indexminr(L, R)
        if ir == R:
            best = R - L + 1
        else:
            il = indexminl(L, R)
            best = R - il + 1
            if ir - L >= best:
                best = max(best, max_magic(L, ir, RIGHTMIN))
    elif info == LEFTMIN:
        il = indexmaxl(L, R)
        if il == L:
            best = R - L + 1
        else:
            ir = indexmaxr(L, R)
            best = ir - L + 1
            if R - il >= best:
                best = max(best, max_magic(il, R, LEFTMAX))
    elif info == RIGHTMIN:
        ir = indexmaxr(L, R)
        if ir == R:
            best = R - L + 1
        else:
            il = indexmaxl(L, R)
            best = R - il + 1
            if ir - L >= best:
                best = max(best, max_magic(L, ir, RIGHTMAX))
    else:
        il = indexmaxl(L, R)
        ir = indexmaxr(L, R)
        best = max(max_magic(il, R, LEFTMAX), max_magic(L, ir, RIGHTMAX))

    cache[L, R] = best
    return best


for i in range(Q):
    L, R = [int(x)-1 for x in input().split()]
    print(max_magic(L, R))


