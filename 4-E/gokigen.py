from collections import defaultdict


class Contradiction(Exception):
    pass

NOBOUND = 5


class Problem:
    """
    A Gokigen Naname problem.
    """

    def __init__(self, n, data):
        self.size = n
        self.data = data
        self.intersections = {}
        for i, line in enumerate(data.split('\n')):
            for j, x in enumerate(line):
                self.intersections[(i, j)] = int(x) if x != '.' else NOBOUND

        self.intersection_status = {(i, j): 0 for i in range(n+1) for j in range(n+1)}
        self.cells = {(i, j): '.' for i in range(n) for j in range(n)}
        self.num_filled = 0

        self.reachable_from = defaultdict(set)
        for i in range(n+1):
            for j in range(n+1):
                self.reachable_from[(i, j)].add((i, j))

    def adds_loop(self, i, j, s):
        first, second = self.st(i, j, s)
        return second in self.reachable_from[first]

    def st(self, i, j, s):
        """Get source and target of s when placed in cell i, j."""

        if s == '/':
            first = i+1, j
            second = i, j+1
        elif s == '\\':
            first = i, j
            second = i+1, j+1
        return first, second

    def fill(self, i, j, s):
        if self.cells[(i, j)] != '.':
            raise Contradiction
        if self.adds_loop(i, j, s):
            raise Contradiction

        # check for contradiction with self.intersections
        if s == '/':
            if self.intersection_status[(i, j+1)] >= self.intersections[(i, j+1)]:
                raise Contradiction
            if self.intersection_status[(i+1, j)] >= self.intersections[(i+1, j)]:
                raise Contradiction

            self.intersection_status[(i, j+1)] += 1
            self.intersection_status[(i+1, j)] += 1
        else:
            if self.intersection_status[(i, j)] >= self.intersections[(i, j)]:
                raise Contradiction
            if self.intersection_status[(i+1, j+1)] >= self.intersections[(i+1, j+1)]:
                raise Contradiction

            self.intersection_status[(i, j)] += 1
            self.intersection_status[(i+1, j+1)] += 1

        self.cells[(i, j)] = s
        self.num_filled += 1

        first, second = self.st(i, j, s)
        for t1 in list(self.reachable_from[first]):
            for t2 in list(self.reachable_from[second]):
                self.reachable_from[t1].add(t2)
                self.reachable_from[t2].add(t1)

    def copy(self):
        p = Problem(self.size, self.data)
        p.intersection_status = self.intersection_status.copy()
        p.cells = self.cells.copy()
        p.reachable_from = defaultdict(set)
        for k, v in self.reachable_from.items():
            p.reachable_from[k] = set(v)
        p.num_filled = self.num_filled
        return p

    def __repr__(self):
        return '\n'.join(''.join(
            self.cells[(i, j)] for j in range(self.size))
            for i in range(self.size))


def solve(pbm):
    try:
        while pbm.num_filled < pbm.size**2:  # solved?
            changed = False
            # Try to fill in some cells which are "forced"

            # Check for intersections where number of free adjacent cells is equal to
            # number of missing extensions, and fill in those cells.
            for i in range(pbm.size+1):
                for j in range(pbm.size+1):
                    if pbm.intersections[(i, j)] == NOBOUND:
                        continue
                    num_free = 0
                    free_cells = []

                    for pt, connecting, disconnecting in [
                            ((i-1, j-1), '\\', '/'),
                            ((i-1, j), '/', '\\'),
                            ((i, j-1), '/', '\\'),
                            ((i, j), '\\', '/'), ]:
                        if not (0 <= pt[0] < pbm.size and 0 <= pt[1] < pbm.size):
                            continue
                        if pbm.cells[pt] == '.':
                            num_free += 1
                            free_cells.append((pt, connecting, disconnecting))

                    if (
                            num_free ==
                            pbm.intersections[(i, j)] - pbm.intersection_status[(i, j)]):
                        for c, s, t in free_cells:
                            pbm.fill(*c, s)
                            changed = True
                    elif pbm.intersections[(i, j)] == pbm.intersection_status[(i, j)]:
                        for c, s, t in free_cells:
                            pbm.fill(*c, t)
                            changed = True

            # Check for all moves that would add a loop (and hence can be eliminated)
            for i in range(pbm.size):
                for j in range(pbm.size):
                    if pbm.cells[(i, j)] != '.':
                        continue
                    if pbm.adds_loop(i, j, '/'):
                        pbm.fill(i, j, '\\')
                        changed = True
                    elif pbm.adds_loop(i, j, '\\'):
                        pbm.fill(i, j, '/')
                        changed = True

            if not changed:
                break

        if pbm.num_filled == pbm.size**2:  # solved?
            for i in range(pbm.size+1):
                for j in range(pbm.size+1):
                    if pbm.intersections[(i, j)] != NOBOUND:
                        if pbm.intersection_status[(i, j)] != pbm.intersections[(i, j)]:
                            return False
            return str(pbm)

        # Continue by backtracking: choose a free cell and try both options ...
        for i in range(pbm.size):
            for j in range(pbm.size):
                if pbm.cells[(i, j)] != '.':
                    continue

                new_pbm = pbm.copy()

                new_pbm.fill(i, j, '/')
                result = solve(new_pbm)
                if result:
                    return result
                else:
                    pbm.fill(i, j, '\\')
                    return solve(pbm)

    except Contradiction:
        return False

    return False


n = int(input())
data = '\n'.join(input() for i in range(n+1))
pbm = Problem(n, data)
print(solve(pbm))

