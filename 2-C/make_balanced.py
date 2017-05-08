import sys
from random import randint, shuffle

s = []
filename = sys.argv[1]
open_par = 0

for i in range(randint(10000, 200000)):
    if open_par:
        s.append(['(', ')'][randint(0, 1)])
    else:
        s.append('(')
    open_par += (1 if s[-1] == '(' else -1)

s += ')' * open_par
print(len(s))

results = []
while s:
    a = randint(10, 300)
    results.append(s[:a])
    s = s[a:]

shuffle(results)

with open(filename, 'w') as f:
    f.write('%d\n' % len(results))
    for r in results:
        f.write(''.join(r)+'\n')

