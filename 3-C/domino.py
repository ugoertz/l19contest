from collections import defaultdict


num_test_cases = int(input())


def rec_add(k, knocked_over, d):
    stack = [k, ]

    while stack:
        kk = stack.pop()
        if kk not in knocked_over:
            stack.extend(d[kk])
            knocked_over.add(kk)


for testcase in range(num_test_cases):
    n, m, l = [int(x) for x in input().split()]
    knocked_over = set()
    d = defaultdict(list)

    for i in range(m):
        a, b = [int(x) for x in input().split()]
        d[a].append(b)
    for i in range(l):
        k = int(input())
        rec_add(k, knocked_over, d)

    print(len(knocked_over))


