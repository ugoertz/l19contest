import sys
from string import ascii_letters, digits


def connect_hor(x):
    if x == ord('.'):
        return ord('-')
    elif x == ord('|'):
        return ord('+')
    return x


def connect_ver(x):
    if x == ord('.'):
        return ord('|')
    elif x == ord('-'):
        return ord('+')
    return x


def connect(lines):
    width = len(lines[0])
    height = len(lines)
    data = bytearray(''.join(lines), encoding='ascii')

    characters = bytes(digits + ascii_letters + '@', encoding='ascii')
    # (add dummy character to avoid index error when Z is reached)
    ctr = 0

    pos = data.find(characters[ctr])
    ctr += 1

    while True:
        npos = data.find(characters[ctr])
        if npos == -1:
            break
        ctr += 1

        if abs(pos-npos) < width:
            # connect horizontally
            for i in range(min(pos, npos)+1, max(pos, npos)):
                data[i] = connect_hor(data[i])
        else:
            # connect vertically
            for i in range(min(pos, npos)+width, max(pos, npos), width):
                data[i] = connect_ver(data[i])

        pos = npos
    return '\n'.join(data[i*width:(i+1)*width].decode('ascii') for i in range(height))


data = sys.stdin.readlines()
data.reverse()

lines = []
while data:
    l = data.pop().strip()
    if not l:
        # next image
        print(connect(lines))
        lines = []
        print()
    else:
        lines.append(l)

print(connect(lines))
