from functools import lru_cache

R, S, K = [int(x) for x in input().split()]
lines = []
for i in range(R):
    lines.append(input())

@lru_cache(maxsize=None)
def num_flies(ii, j):
    '''Num of flies in row segment of length (K-2) located at (ii, j).'''
    return lines[ii][j:j+K-2].count('*')

def number_of_flies_at(i, j):
    '''Num of flies in square of size (K-2)*(K-2) located at (i, j).'''
    return sum(num_flies(ii, j) for ii in range(i, i+K-2))

best = 0
for i in range(1, R - K + 2):
    for j in range(1, S - K + 2):
        nof = number_of_flies_at(i, j)
        if nof > best:
            best = nof
            besti, bestj = i, j

print(best)

for l in lines[:besti-1]:
    print(l)
l = lines[besti-1]
print(l[:bestj-1] + '+' + '-' * (K-2) + '+' + l[bestj+K-1:])
for l in lines[besti:besti+K-2]:
    print(l[:bestj-1] + '|' + l[bestj:bestj+K-2] + '|' + l[bestj+K-1:])
l = lines[besti+K-2]
print(l[:bestj-1] + '+' + '-' * (K-2) + '+' + l[bestj+K-1:])
for l in lines[besti+K-1:]:
    print(l)

