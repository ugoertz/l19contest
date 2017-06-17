def length(c):
    return c[1][0] - c[0][0] + c[1][1] - c[0][1] + 1


def potential(c, size):
    return 2*min(c[0][0]+c[0][1], 2*size-c[1][0]-c[1][1]-2) + length(c)


for ctr1 in range(int(input())):
    lines = []
    size = int(input())
    for ctr2 in range(size):
        lines.append(input().strip())

    candidates = []
    candidates.extend([
        ((i, j), (i+1, j), 'D')
        for i in range(size-1) for j in range(size)
        if lines[i][j] == lines[i+1][j]])
    candidates.extend([
        ((i, j), (i, j+1), 'R')
        for i in range(size) for j in range(size-1)
        if lines[i][j] == lines[i][j+1]])
    candidates.extend([
            ((i, j), (i, j), '') for i in range(size) for j in range(size)])

    cands = [(potential(c, size), ) + c for c in candidates]
    candidates = [c[1:] for c in sorted(cands)]

    best = ((0, 0), (0, 0), '')
    seen = set(c[:2] for c in candidates)

    while candidates:
        c = candidates.pop()
        # is the candidate better than current best?
        if length(c) > length(best):
            best = c
        elif potential(c, size) <= length(best):
            continue

        # try to extend candidate to a candidate with potential larger than
        # current best
        for change in [
                ((-1, 0), (1, 0), 'D', 'D'),
                ((-1, 0), (0, 1), 'D', 'R'),
                ((0, -1), (1, 0), 'R', 'D'),
                ((0, -1), (0, 1), 'R', 'R')
                ]:
            cc = (
                    tuple(map(lambda x, y: x+y, change[0], c[0])),
                    tuple(map(lambda x, y: x+y, change[1], c[1])))
            if not (cc[0][0] >= 0 and cc[0][1] >= 0 and
                    cc[1][0] < size and cc[1][1] < size):
                continue
            if lines[cc[0][0]][cc[0][1]] != lines [cc[1][0]][cc[1][1]]:
                continue
            if cc in seen:
                continue
            else:
                seen.add(cc)

            candidates.append(cc + (change[2] + c[2] + change[3], ))

    pos = best[0]
    result = [lines[pos[0]][pos[1]]]

    for x in best[2]:
        if x == 'R':
            pos = pos[0], pos[1] + 1
        else:
            pos = pos[0] + 1, pos[1]
        result.append(lines[pos[0]][pos[1]])
    print(''.join(result), best[0][0]+1, best[0][1]+1, best[2]+'S')
