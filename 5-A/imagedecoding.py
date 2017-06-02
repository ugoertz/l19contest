import sys

switch = {'#': '.', '.': '#', }

def print_line(inp):
    data = inp.split()
    ch = data[0]
    l = 0
    for i in data[1:]:
        for j in range(int(i)):
            print(ch, end='')
        l += int(i)
        ch = switch[ch]
    print()
    return l

data = sys.stdin.readlines()
data.reverse()

while data:
    height = int(data.pop())
    if height == 0:
        break

    length = -1
    decoding_error = False
    for i in range(height):
        l = print_line(data.pop())
        if length == -1:
            length = l
        elif length != l:
            decoding_error = True
    if decoding_error:
        print('Error decoding image')
    if len(data) > 1:  # Another image coming? Then print separating line
        print()
