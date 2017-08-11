
def matching_par(c, n):
    '''Find parenthesis in c matching the open parenthesis at position n.'''
    ctr = n+1
    i = 1
    while ctr < len(c):
        if c[ctr] == ')':
            i -= 1
        elif c[ctr] == '(':
            i += 1
        if i == 0:
            return ctr
        ctr += 1


def evaluate_circuit(c, start=0, end=None):
    global Rs
    end = end or len(c)

    d = []

    typ = None
    i = start
    while i < end and c[i] != ')':
        if c[i+1] == 'R':
            d.append(Rs[int(c[i+2]) - 1])
            typ = typ or c[i+3]
            i += 3
        elif c[i+1] == '(':
            m = matching_par(c, i+1)
            d.append(evaluate_circuit(c, i+1, m))
            typ = typ or c[m + 1]
            i = m + 1

    if typ == '-':
        return sum(d)
    elif typ == '|':
        return 1 / sum(1/x for x in d)


N = int(input())
Rs = [float(x) for x in input().split()]

print('%.5f' % evaluate_circuit(input()))

