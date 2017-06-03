from collections import namedtuple

Node = namedtuple('Node', ['s', 'pos', 'parent', 'depth'])

length = int(input())

lines = []
for i in range(10):
    lines.append(input())
lines.reverse()  # number lowest line by 0

stack = []
current = Node('', 0, None, 0)
seen = set()  # do not visit positions twice

while current.depth < length-1:
    rise = min(current.pos + 1, 9)
    fall = max(current.pos - 1, 0)
    cdp1 = current.depth + 1
    if lines[rise][cdp1] == '.' and not (rise, cdp1) in seen:
            stack.append(Node(1, rise, current, cdp1))
            seen.add((rise, cdp1))
    if lines[fall][cdp1] == '.' and not (fall, cdp1) in seen:
            stack.append(Node(0, fall, current, cdp1))
            seen.add((fall, current.depth+1))
    current = stack.pop()


movelist = []
n = current

while n.parent:
    movelist.append(n.s)
    n = n.parent

moves = []
st = 0
c = 0
for i, m in enumerate(reversed(movelist)):
    if m == 1:  # rising
        if c == 0:
            st = i
        c += 1
    elif c:  # does this end a rise?
        moves.append('%d %d' % (st, c))
        c = 0
if c:  # add final rise, if appropriate
    moves.append('%d %d' % (st, c))


print(len(moves))
print('\n'.join(moves))

