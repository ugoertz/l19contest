import sys

for ctr, line in enumerate(sys.stdin):
    try:
        size = int(line)
        if size <= 1:
            print(size)
        else:
            print(2 * size - 2)
    except:
        pass


