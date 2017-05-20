import sys
from collections import defaultdict, deque

sys.setrecursionlimit(11000)

data = deque(sys.stdin.readlines())


def paths_reaching(y, incoming, cache):
    if not incoming[y]:
        return 1  # starting node
    try:
        return cache[y]
    except:
        result = sum(paths_reaching(yy, incoming, cache) for yy in incoming[y])
        cache[y] = result
        return result


while data:
    incoming = defaultdict(list)
    gates = []
    cache = {}

    number_nodes = int(data.popleft())
    end_nodes = set(range(number_nodes))

    number_edges = int(data.popleft())

    for i in range(number_edges):
        x, y = [int(a) for a in data.popleft().split()]
        incoming[y].append(x)
        try:
            end_nodes.remove(x)
        except:
            pass

    number_gates = int(data.popleft())
    for i in range(number_gates):
        gates.append(int(data.popleft()))

    winning = sum(paths_reaching(y, incoming, cache) for y in gates)
    losing = sum(paths_reaching(y, incoming, cache) for y in end_nodes - set(gates))
    print('winning paths', winning)
    print('total paths', winning + losing)

