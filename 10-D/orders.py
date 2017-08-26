n = int(input())

orders = {}
dishes = sorted((int(x), i) for i, x in enumerate(input().split()))

m = int(input())
orders = [int(x) for x in input().split()]
maxorder = max(orders) + 1
data = {0: [0,] * len(dishes), }


for x, i in dishes:

    if x in data:
        if data[x] != 'Ambiguous':
            for i in range(x, maxorder):
                if i-x in data:
                    data[i] = 'Ambiguous'
        continue

    for o in range(x, maxorder):
        if not o - x in data:
            continue
        if o in data or data[o - x] == 'Ambiguous':
            data[o] = 'Ambiguous'
        else:
            data[o] = data[o-x][:]
            data[o][i] += 1


for x in orders:
    if not x in data:
        print('Impossible')
    elif data[x] == 'Ambiguous':
        print('Ambiguous')
    else:
        result = []
        for i in range(len(dishes)):
            result.extend([str(i+1), ] * data[x][i])

        print(' '.join(result))

