import sys

l, w, n, r = [int(x) for x in input().split()]
r *= 2  # we do not want to use half-integers as coordinates (l/2, w/2 etc.),
        # so multiply everything else by 2
cranes = set()
reachable = set()
max_reachable = -1
for i in range(n):
    x, y = (int(z)*2 for z in input().split())
    s = tuple(center for center in [(-l, 0), (l, 0), (0, -w), (0, w)]
            if (center[0]-x)**2 + (center[1]-y)**2 <= r**2)
    reachable |= set(s)
    max_reachable = max(len(s), max_reachable)
    cranes.add(s)

if max_reachable == 4:
    print(1)
elif len(reachable) != 4:
    print('Impossible')
elif max_reachable == 1:
    print(4)
elif max_reachable == 3:
    print(2)
else:
    # max_reachable == 2, so need to check whether have two disjoint sets in cranes
    cranes2 = [s for s in cranes if len(s) == 2]
    for s1 in cranes2:
        for s2 in cranes2:
            if len(set(s1) | set(s2)) == 4:
                print(2)
                sys.exit()
    print(3)




