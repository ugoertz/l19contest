import sys

queens_cache = {}

# Encode board as list l where l[i] is the row of the queen in the i-th column

def options(size, board):
    result = []
    for i in range(size):
        # check whether we can add a queen at (i, len(board)),
        # i.e., in row i and in the first unoccupied column

        if i in board:
            # conflict because of queen in that row
            continue

        for j in range(len(board)):
            if abs(board[j]-i) == len(board) - j:
                # conflict because of diagonal
                break
        else:
            result.append(i)

    return result


def queens(size, board=None):
    if board is None:
        try:
            return queens_cache[size]
        except KeyError:
            pass
        brd = []
    else:
        brd = board

    result = []
    if len(brd) == size:
        return [brd, ]

    for o in options(size, brd):
        result.extend(queens(size, brd+[o, ]))

    if board is None:
        queens_cache[size] = result
    return result


def num_queens_holes(size, holes):
    result = 0
    for board in queens(size):
        fail = False
        for i, j in holes:
            if board[i] == j:
                fail = True
                break
        else:
            result += 1
    return result


data = sys.stdin.readlines()
ctr = 0

while data[ctr].strip() != '0 0':
    size, num_holes = [int(x) for x in data[ctr].split()]
    ctr += 1

    holes = []
    for i in range(num_holes):
        holes.append(tuple(int(x) for x in data[ctr].split()))
        ctr += 1

    print(num_queens_holes(size, holes))



