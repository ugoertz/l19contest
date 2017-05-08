import sys
from collections import defaultdict


def open_required(e):
    m = 0
    open_par = 0
    for i in e:
        if i == '(':
            open_par += 1
        elif i == ')':
            open_par -= 1
        else:
            raise Exception('Unexpected symbol')
        if open_par < m:
            m = open_par
    return -m


def maximal_balanced(expressions):

    reachable = defaultdict(int)  # dict: {open_par: max reachable length, }
    reachable[0] = 0

    for dummy, open_requ, ct, len_e in expressions:
        items = list(reachable.items())
        for k, v in items:
            if open_requ <= k:
                new_k = k + ct
                vpl = v + len_e
                if vpl > reachable[new_k]:
                    reachable[new_k] = vpl

    return reachable[0]


expr_open = []
expr_middle = []
expr_close = []
result = 0

for ctr, x in enumerate(sys.stdin.readlines()):
    if ctr == 0:
        number_of_expr = int(x)
        continue
    elif ctr > number_of_expr:
        break

    xs = x.strip()
    orxs = open_required(xs)
    ct = xs.count('(') - xs.count(')')
    if orxs == 0 and ct == 0:  # balanced, so use this anyway
        result += len(xs)
        continue

    data = (ct + orxs, orxs, ct, len(xs))

    # split this up since expressions in expr_open (and expr_close, resp.)
    # commute, so we only have to sort the middle list
    if data[1] == 0:
        expr_open.append(data)
    elif data[0] == 0:
        expr_close.append(data)
    else:
        expr_middle.append(data)

expr_middle = sorted(expr_middle, reverse=True)

print(result + maximal_balanced(expr_open + expr_middle + expr_close))

