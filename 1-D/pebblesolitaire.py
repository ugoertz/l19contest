import sys

cache = {}


def num_pebbles(pos):
    return len([1 for x in pos if x == 'o'])


def move(pos, n, m):
    p = pos[:]

    p[n] = '-'
    p[(n+m)//2] = '-'
    p[m] = 'o'
    return p


def min_number_pebbles(pos):
    assert len(pos) == 23
    try:
        return cache[''.join(pos)]
    except:
        pass

    moves = []
    #  Will be a list of pairs (m, n), each pair meaning that the pebble on
    #  place m moves to place n (and the pebble between m and n is removed).
    #  Here 0 <= m, n < len(pos)

    for i in range(21):  # 21 == len(pos)-2
        if pos[i+1] == 'o':
            if pos[i] == 'o' and pos[i+2] == '-':
                moves.append((i, i+2))
            elif pos[i] == '-' and pos[i+2] == 'o':
                moves.append((i+2, i))

    if not moves:
        np = num_pebbles(pos)
    else:
        np = min(min_number_pebbles(move(pos, *p)) for p in moves)
    cache[''.join(pos)] = np
    return np


for ctr, line in enumerate(sys.stdin):
    if ctr == 0:
        number_test_cases = int(line)
        continue
    if ctr > number_test_cases:
        # trailing lines?
        break

    print(min_number_pebbles(list(line.strip())))


