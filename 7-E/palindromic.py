import sys
from functools import lru_cache

sys.setrecursionlimit(10000)

LIMIT = 10**9 + 7


@lru_cache(maxsize=None)
def num_palindromes(start, end):
    global s
    # print(s[start:end], start, end)
    if all(s[i] == s[start] for i in range(start + 1, end)):
        #  print(s[start:end], start, end, end=' ')
        #  print(2**(end-start) - 1, 'D')
        return 2**(end-start) - 1

    result = num_palindromes(start+1, end) + 1  # +1 for just first letter
    pos = s.rfind(s[start], start+1, end)
    while pos != -1:
        result += num_palindromes(start+1, pos) + 1  # +1 for empty middle
        pos = s.rfind(s[start], start+1, pos)

    #  print(s[start:end], start, end, end=' ')
    #  print(result)
    return result % LIMIT


for _ in range(int(input())):
    s = input().strip()
    print(num_palindromes(0, len(s)))
    num_palindromes.cache_clear()

