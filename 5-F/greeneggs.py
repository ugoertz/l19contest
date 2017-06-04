import ast
import sys


def center(s, length):
    '''
    There is s.center(), but it is not clear how this behaves if length-len(s)
    is odd ...

    This method centers s within a string of specified length, using space as
    a padding character, and adding one extra space on the right, if necessary.
    '''

    a, b = divmod(length - len(s), 2)
    return ' ' * (a + b) + s + ' ' * a


def binop(left, right, op):
    lf, lvcl = tex(left)
    rt, lvcr = tex(right)
    if lvcl < lvcr:
        lf = [' ' * len(lf[0])] * (lvcr - lvcl) + lf
        lvcl = lvcr
    elif lvcl > lvcr:
        rt = [' ' * len(rt[0])] * (lvcl - lvcr) + rt

    if len(lf) < len(rt):
        lf.extend([' ' * len(lf[0])] * (len(rt) - len(lf)))
    elif len(lf) > len(rt):
        rt.extend([' ' * len(rt[0])] * (len(lf) - len(rt)))
    assert len(lf) == len(rt)

    return [
            lf[i] + (' ' + op + ' ' if i == lvcl else '   ') + rt[i]
            for i in range(len(lf))], lvcl


def power(left, right):
    lf, lvcl = tex(left)
    rt, lvcr = tex(right)
    return (
            [' '*len(lf[0]) + l for l in rt]
            + [l.ljust(len(lf[0])+len(rt[0])) for l in lf],
            lvcl + len(rt))


def minus(E):
    e, lvc = tex(E)
    return [('-' if i == lvc else ' ')+l for i, l in enumerate(e)], lvc


def frac(left, right):
    lf, lvcl = tex(left)
    rt, lvcr = tex(right)
    return (
            [center(l, max(len(lf[0]), len(rt[0]))) for l in lf]
            + ['-'*max(len(lf[0]), len(rt[0])), ]
            + [center(l, max(len(lf[0]), len(rt[0]))) for l in rt],
            len(lf))


def parens(E):
    e, lvc = tex(E)
    return ['(' + l + ')' for l in e], len(e)//2


def tex(a):
    '''
    Returns a pair consisting of list of strings, all of the same length,
    containing the typeset expression and a non-negative integer (the LVC).
    '''

    global source

    if isinstance(a, ast.Name):
        return [a.id, ], 0
    elif isinstance(a, ast.Num):
        # hack to make sure we copy number as given in source
        num = []
        i = a.col_offset
        while source[i] in '.0123456789':
            num.append(source[i])
            i += 1
        return [''.join(num), ], 0
    elif isinstance(a, ast.BinOp):
        if type(a.op) == ast.Add:
            return binop(a.left, a.right, '+')
        elif type(a.op) == ast.Sub:
            return binop(a.left, a.right, '-')
        elif type(a.op) == ast.Mult:
            return binop(a.left, a.right, '*')
        elif type(a.op) == ast.Div:
            return frac(a.left, a.right)
        elif type(a.op) == ast.Pow:
            return power(a.left, a.right)
    elif isinstance(a, ast.Compare):
            return binop(a.left, a.comparators[0], '=')
    elif isinstance(a, ast.UnaryOp):
        if type(a.op) == ast.USub:
            return minus(a.operand)
    elif isinstance(a, ast.Call):
        return parens(a.args[0])


result = []
for source in sys.stdin.readlines():
    source = source.replace('(', 'parens(')
    source = source.replace('{', '(')
    source = source.replace('}', ')')
    source = source.replace('^', '**')
    source = source.replace('=', '==')
    result.append(
            '\n'.join([l.rstrip()
                for l in tex(ast.parse(source, mode='eval').body)[0]]))

print('\n\n'.join(result))

