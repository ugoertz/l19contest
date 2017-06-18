import sys
from functools import lru_cache

sys.setrecursionlimit(10000)

LIMIT = 10**9 + 7


@lru_cache(maxsize=None)
def num_palindromes(s):
    if all(s[i] == s[0] for i in range(1, len(s))):
        return 2**len(s) - 1

    result = num_palindromes(s[1:]) + 1  # +1 for just first letter
    pos = s.rfind(s[0], 1, len(s))
    while pos != -1:
        result += num_palindromes(s[1:pos]) + 1  # +1 for empty middle
        pos = s.rfind(s[0], 1, pos)

    return result % LIMIT


for _ in range(int(input())):
    s = input().strip()
    print(num_palindromes(s))

