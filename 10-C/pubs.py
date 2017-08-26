from collections import defaultdict
import sys


n, m = (int(x) for x in input().split())

neighbors = defaultdict(set)

for i in range(m):
    a, b = (int(x)-1 for x in input().split())
    neighbors[a].add(b)
    neighbors[b].add(a)


todo = set(range(n))
result = [None, ] * n

while todo:
    i = todo.pop()

    if len(neighbors[i]) == 0:
        print('Impossible')
        sys.exit()

    result[i] = 1
    stack = [(i, 1)]

    while stack:
        ii, v = stack.pop()
        for j in neighbors[ii]:
            if result[j] is not None:
                continue
            result[j] = 1 - v
            todo.remove(j)
            stack.append((j, 1 - v))


print(' '.join(('pub' if x else 'house') for x in result))

