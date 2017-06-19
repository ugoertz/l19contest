from functools import lru_cache
import sys

sys.setrecursionlimit(10000)


@lru_cache(maxsize=None)
def acs(i, j):
    '''
    Number of all common subsequences of s[:i] and reversed(s)[:j] (incl. empty).
    '''

    global s
    if i == 0 or j == 0:
        return 1
    if s[i-1] == s[len(s)-j]:
        return acs(i-1, j) + acs(i, j-1)

    return acs(i-1, j) + acs(i, j-1) - acs(i-1, j-1)


for _ in range(int(input())):
    s = input().strip()

    # odd length palindromes
    num = sum(acs(i, len(s)-i-1) for i in range(len(s)))  # center s[i]

    # even length palindromes
    num += sum(acs(i, j) for i in range(len(s)-1) for j in range(len(s)-i-1) if s[i] == s[len(s)-j-1])

    print(num % (10**9+7))
    acs.cache_clear()


