import sys

def fib(n):
    l = [0, 1]
    for ctr in range(n-1):
        l.append(l[-1]+l[-2])
    return l



for ctr, line in enumerate(sys.stdin):
    try:
        N, K = [int(x) for x in line.split()]
        fibs = fib(N)
        index = N

        while index > 2:
            if K <= fibs[index-2]:
                index -= 2
            else:
                K -= fibs[index-2]
                index -= 1

        assert 1 <= index <= 2
        print(['N', 'A'][index-1])

    except:
        pass


