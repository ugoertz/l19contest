def howmanyzeros(n):
    r = 1
    sn = str(n)
    for i, d in enumerate(reversed(sn)):
        if i == len(sn) - 1:
            break
        if d == '0' and i > 0:
            r += (n // 10**(i+1) - 1) * 10**i + n % 10**i + 1
        else:
            r += (n // 10**(i+1)) * 10**i

    return r


while True:
    n, m = [int(x) for x in input().split()]
    if m < 0:
        break

    if n == 0:
        print(howmanyzeros(m))
    else:
        print(howmanyzeros(m) - howmanyzeros(n-1))

