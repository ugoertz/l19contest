
d = {'-': '|', '|': '-', }

length = None

while True:
    lg = int(input())
    if lg == 0:
        break
    elif length:
        print()  # separator
    length = lg

    lines = []
    for i in range(length):
        lines.append(input())
    max_length = max(len(l) for l in lines)

    lines = [l.ljust(max_length) for l in lines]
    out = []
    for i in range(max_length):
        for j in range(length-1, -1, -1):
            try:
                out.append(d[lines[j][i]])
            except KeyError:
                out.append(lines[j][i])
        out.append('\n')
    out = [x.rstrip() for x in ''.join(out[:-1]).split('\n')]
    print('\n'.join(out))
