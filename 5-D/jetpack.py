from array import array

class Node:

    def __init__(self, s, parent=None):
        self.s = s  # the move (rise/fall) to reach this node from its parent
                    # == '' for root node
        self.parent = parent


def add_move(ctr, item, new_reachable, pos, direction):
    if lines[pos][ctr+1] != '.' or pos in new_reachable:
        return
    new_reachable[pos] = Node(direction, parent=node)


length = int(input())

lines = []
for i in range(10):
    lines.append(input())
lines.reverse()  # number lowest line by 0

reachable = Node('')
leaves = {0: reachable, }  # leaves at depth ctr

for ctr in range(length-1):
    new_leaves = {}  # dict  pos: node
    for r, node in leaves.items():
        if r < 9:
            add_move(ctr, node, new_leaves, r+1, 1)
        elif r == 9:
            add_move(ctr, node, new_leaves, r, 1)
        if r > 0:
            add_move(ctr, node, new_leaves, r-1, 0)
        elif r == 0:
            add_move(ctr, node, new_leaves, r, 0)
    leaves = new_leaves


for k in leaves:
    movelist = []
    n = leaves[k]

    while n.parent:
        movelist.append(n.s)
        n = n.parent

    moves = []
    st = 0
    c = 0
    for i, m in enumerate(reversed(movelist)):
        if m == 1:
            if c == 0:
                st = i
            c += 1
        elif c:  # does this end a rise?
            moves.append('%d %d' % (st, c))
            c = 0
    if c:  # add final rise, if appropriate
        moves.append('%d %d' % (st, c))

    break # only need to consider one leaf

print(len(moves))
print('\n'.join(moves))

