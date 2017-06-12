import itertools
from math import sqrt


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


bases = [4, 5, 6, 7, 9, 11, ]
P = primes()
for i in range(5):
    # discard first 5 primes
    p = next(P)

while p < 2**16:
    p = next(P)
    bases.append(p)


while True:
    n = int(input())
    if n == 0:
        break

    # no such base cases
    if n in [1, 2, 4, 5, 6, ]:
        print('No such base')
        continue

    # general case
    n = n - 3
    for b in bases:
        if n % b == 0:
            print(b)
            break
    else:
        # n has no prime factors 5 <= p <= 2**16
        if n % 2 == 0:
            n = n // 2
        if n % 3 == 0:
            n = n // 3
        print(n)

