pow3 = [str(3**i) for i in range(70)]

while True:
    n = int(input())
    if n == 0:
        break

    # the desired set "reflects" the binary representation of n-1
    n = n - 1
    if n == 0:  # handle this separately because of spacing in output
        print('{ }')
        continue

    i = 0
    res = []
    while n:
        if n % 2:
            res.append(pow3[i])
        n = n // 2
        i += 1
    print('{ ' + ', '.join(res) + ' }')
