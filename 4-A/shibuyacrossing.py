from collections import defaultdict


maximum_clique_size = 1


def BronKerbosch(R, P, X, listP=None):
    """
    See https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

    Some modifications to avoid recursive calls which cannot give rise to
    a maximum clique.

    Optionally, can pass listP which is a list containing the elements of the
    set P; then the iteration over the elements in P will occur in the order of
    that list. (The idea is that we look at vertices with many neighbors first.)
    """

    global maximum_clique_size
    if len(P) == len(X) == 0:
        maximum_clique_size = max(len(R), maximum_clique_size)
        # print(R)
    else:
        listP = listP or list(P)
        for v in listP:
            if len(nbs[v]) >= maximum_clique_size:
                # only follow up on this if there is a chance to find a larger
                # clique
                BronKerbosch(R | set([v, ]), nbs[v] & P, nbs[v] & X)
                P.remove(v)
                X.add(v)


nbs = defaultdict(set)
num_nbs = defaultdict(int)
n, m = [int(x) for x in input().split()]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    nbs[a].add(b)
    nbs[b].add(a)
    num_nbs[a] += 1
    num_nbs[b] += 1

P = set(range(1, n+1))
listP = [x[1] for x in sorted(
    ((num_nbs[a], a) for a in P), reverse=True
    )]

BronKerbosch(set(), P, set(), listP)
print(maximum_clique_size)

