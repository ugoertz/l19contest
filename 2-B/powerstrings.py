import sys
import itertools
from math import sqrt
from string import ascii_lowercase


def primes():
    """
    See http://stackoverflow.com/a/3796442.
    """

    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D:
                x += 2*p
            D[x] = p


def prime_divisors(n):
    for p in primes():
        if n % p == 0:
            yield p
            while n % p == 0:
                n = n // p
        if p > n:
            break


def stringlog(s, l=None):
    l = l or len(s)  # consider only the first l letters in s
    for m in prime_divisors(l):
        d = l // m
        for i in range(1, m):
            if s[i*d:(i+1)*d] != s[:d]:
                # s not a power of s[:d]
                break
        else:
            return m * stringlog(s, d)

    return 1


for line in sys.stdin:
    if line.strip() == '.':
        break

    s = memoryview(line.strip().encode('ascii'))
    print(stringlog(s))


