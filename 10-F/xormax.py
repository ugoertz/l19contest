n = int(input())
d = {}

for xx in input().split():
    a = int(xx)
    while a > 0:
        f = a.bit_length()
        try:
            a ^= d[f]
        except KeyError:
            d[f] = a
            break

result = 0
for f in range(60, 0, -1):
    try:
        result = max(result, result ^ d[f])
    except KeyError:
        pass
print(result)
