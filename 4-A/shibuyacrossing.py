from collections import Counter, deque


def len_max_increasing_subsequence(n, l):
    """
    l is a list containing a permutation of 1, ..., n.
    Returns the maximal length of an increasing subsequence in l.
    """

    d = [0] * n
    # at position x, store length of maximal increasing subsequence ending in x

    for i, x in enumerate(l):
        try:
            d[x] = 1 + max(d[j] for j in range(x))
        except ValueError:  # max does not accept empty sequence
            d[0] = 1

    return max(d)


num_smaller_nbs = Counter()
n, m = [int(x) for x in input().split()]

for i in range(m):
    a, b = input().split()
    num_smaller_nbs[int(b)-1] += 1

# find permutation of this permutation graph
p = deque()
for i in range(n):
    p.insert(i-num_smaller_nbs[i], i)

print(len_max_increasing_subsequence(n, reversed(p)))
